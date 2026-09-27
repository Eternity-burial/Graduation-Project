/**
 * Standalone Literature Reader Application Logic
 * Supports KaTeX math rendering, 100% paired bilingual word highlighting,
 * audio pronunciation, bookmarking, and view toggling.
 */

(function() {
  'use strict';

  let currentPaperId = 'paper1';
  let viewMode = 'bilingual'; // 'bilingual', 'en-only', 'zh-only'
  let currentPinnedWord = null;
  let activePopoverElement = null;

  // Cache DOM elements
  const dom = {
    paperNavList: document.getElementById('paperNavList'),
    tocList: document.getElementById('tocList'),
    readingCanvas: document.getElementById('readingCanvas'),
    articleContent: document.getElementById('articleContent'),
    popover: document.getElementById('vocabPopover'),
    popWord: document.getElementById('popWord'),
    popIpa: document.getElementById('popIpa'),
    popMeaning: document.getElementById('popMeaning'),
    popLevel: document.getElementById('popLevel'),
    btnStar: document.getElementById('btnPopStar'),
    btnPin: document.getElementById('btnPopPin'),
    btnAudioUs: document.getElementById('btnAudioUs'),
    btnAudioUk: document.getElementById('btnAudioUk'),
    lightbox: document.getElementById('lightboxModal'),
    lightboxImg: document.getElementById('lightboxImg'),
    vocabDrawer: document.getElementById('vocabDrawer'),
    drawerList: document.getElementById('drawerList'),
    btnOpenDrawer: document.getElementById('btnOpenDrawer'),
    btnCloseDrawer: document.getElementById('btnCloseDrawer'),
    btnTheme: document.getElementById('btnThemeToggle'),
    btnFontDec: document.getElementById('btnFontDec'),
    btnFontInc: document.getElementById('btnFontInc')
  };

  // Local Storage for Starred Vocab
  function getStarredVocab() {
    try {
      return JSON.parse(localStorage.getItem('starred_literature_vocab') || '{}');
    } catch(e) {
      return {};
    }
  }

  function saveStarredVocab(dict) {
    localStorage.setItem('starred_literature_vocab', JSON.stringify(dict));
    updateDrawer();
  }

  function isWordStarred(word) {
    const dict = getStarredVocab();
    return !!dict[word.toLowerCase()];
  }

  function toggleStarWord(word, meta) {
    const dict = getStarredVocab();
    const key = word.toLowerCase();
    if (dict[key]) {
      delete dict[key];
    } else {
      dict[key] = {
        word: word,
        ipa: meta.ipa || '',
        meaning: meta.meaning || '',
        level: meta.level || 'red',
        paperId: currentPaperId,
        date: new Date().toLocaleDateString()
      };
    }
    saveStarredVocab(dict);
    updatePopoverStarButton(word);
  }

  function updatePopoverStarButton(word) {
    if (!dom.btnStar) return;
    const starred = isWordStarred(word);
    dom.btnStar.innerHTML = starred ? '<i class="fa-solid fa-star"></i>' : '<i class="fa-regular fa-star"></i>';
    dom.btnStar.classList.toggle('starred', starred);
  }

  // Audio Pronunciation via Web Speech API
  function speakWord(text, lang = 'en-US') {
    if (!('speechSynthesis' in window)) {
      alert('Your browser does not support Speech Synthesis.');
      return;
    }
    window.speechSynthesis.cancel();
    const cleanText = text.replace(/[\$\\]/g, ' ').trim();
    const utterance = new SpeechSynthesisUtterance(cleanText);
    utterance.lang = lang;
    utterance.rate = 0.95;
    window.speechSynthesis.speak(utterance);
  }

  // Math Protection & Vocabulary Highlighting
  function renderAnnotatedEnglish(text, vocabList) {
    if (!text) return '';
    // Protect LaTeX math formulas
    const mathPhs = [];
    let s = text.replace(/(\$\$[\s\S]*?\$\$|\$[^\$]+?\$|\\\[[\s\S]*?\\\]|\\\([\s\S]*?\\\))/g, (m) => {
      const idx = mathPhs.length;
      mathPhs.push(m);
      return `___MATH_PH_${idx}___`;
    });

    if (vocabList && vocabList.length > 0) {
      const sorted = [...vocabList].sort((a, b) => (b.word || '').length - (a.word || '').length);
      sorted.forEach(v => {
        if (!v.word) return;
        const esc = v.word.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
        const reg = new RegExp(`\\b(${esc})\\b`, 'gi');
        s = s.replace(reg, (match) => {
          const lvl = v.level || 'red';
          const ipa = (v.ipa || '').replace(/"/g, '&quot;');
          const meaning = (v.meaning || '').replace(/"/g, '&quot;');
          return `<span class="vocab-word level-${lvl}" data-word="${v.word}" data-ipa="${ipa}" data-meaning="${meaning}" data-level="${lvl}">${match}</span>`;
        });
      });
    }

    // Restore LaTeX math formulas
    s = s.replace(/___MATH_PH_(\d+)___/g, (_, i) => mathPhs[parseInt(i)]);
    return s;
  }

  function renderAnnotatedChinese(trans, vocabList) {
    if (!trans) return '';
    const mathPhs = [];
    let s = trans.replace(/(\$\$[\s\S]*?\$\$|\$[^\$]+?\$|\\\[[\s\S]*?\\\]|\\\([\s\S]*?\\\))/g, (m) => {
      const idx = mathPhs.length;
      mathPhs.push(m);
      return `___MATH_PH_${idx}___`;
    });

    if (vocabList && vocabList.length > 0) {
      const occupied = new Array(s.length).fill(false);
      const spans = [];

      const candidates = [];
      vocabList.forEach(v => {
        const word = v.word || '';
        const ipa = (v.ipa || '').replace(/"/g, '&quot;');
        const meaning = (v.meaning || '').replace(/"/g, '&quot;');
        const lvl = v.level || 'red';

        if (v.zh && v.zh.length > 0) {
          candidates.push({ zh: v.zh, word, ipa, meaning, lvl, len: v.zh.length });
        }
      });

      candidates.sort((a, b) => b.len - a.len);

      candidates.forEach(cand => {
        let pos = 0;
        while (pos < s.length) {
          const idx = s.indexOf(cand.zh, pos);
          if (idx === -1) break;
          const end = idx + cand.zh.length;
          let conflict = false;
          for (let k = idx; k < end; k++) {
            if (occupied[k]) { conflict = true; break; }
          }
          if (!conflict) {
            for (let k = idx; k < end; k++) occupied[k] = true;
            spans.push({
              start: idx,
              end: end,
              html: `<span class="vocab-word trans-vocab-word level-${cand.lvl}" data-word="${cand.word}" data-ipa="${cand.ipa}" data-meaning="${cand.meaning}" data-level="${cand.lvl}">${cand.zh}</span>`
            });
          }
          pos = idx + 1;
        }
      });

      if (spans.length > 0) {
        spans.sort((a, b) => a.start - b.start);
        let res = '';
        let last = 0;
        spans.forEach(sp => {
          res += s.substring(last, sp.start);
          res += sp.html;
          last = sp.end;
        });
        res += s.substring(last);
        s = res;
      }
    }

    s = s.replace(/___MATH_PH_(\d+)___/g, (_, i) => mathPhs[parseInt(i)]);
    return s;
  }

  // Render Paper Content
  function loadPaper(paperId) {
    currentPaperId = paperId;
    const data = window.BISHE_DATA ? window.BISHE_DATA[paperId] : null;
    if (!data) {
      dom.articleContent.innerHTML = `<div style="text-align:center;padding:40px;color:red;">Paper dataset not found for: ${paperId}</div>`;
      return;
    }

    // Update active nav item
    document.querySelectorAll('.paper-nav-item').forEach(el => {
      el.classList.toggle('active', el.dataset.paper === paperId);
    });

    // Build TOC
    let tocHtml = '';
    data.sections.forEach((sec, idx) => {
      tocHtml += `
        <li class="toc-item ${idx === 0 ? 'active' : ''}">
          <a href="#${sec.id}" data-sec="${sec.id}">
            <span style="font-weight:700;color:var(--primary-color);">${sec.sectionNumber || idx + 1}</span>
            <span style="overflow:hidden;text-overflow:ellipsis;white-space:nowrap;">${sec.title}</span>
          </a>
        </li>
      `;
    });
    dom.tocList.innerHTML = tocHtml;

    // Build Article HTML
    let html = '';

    // Hero Section
    html += `
      <div class="paper-hero">
        <div class="paper-meta-badge"><i class="fa-solid fa-graduation-cap"></i> 毕业设计精读文献</div>
        <h1>${data.title}</h1>
        <div class="paper-zh-title">${data.chineseTitle || ''}</div>
        
        <div class="meta-grid">
          <div><strong>作者：</strong>${data.authors || 'N/A'}</div>
          <div><strong>发表：</strong>${data.journal || 'N/A'}</div>
          <div><strong>机构：</strong>${data.venue || 'N/A'}</div>
        </div>

        <div class="paper-overview-box">
          <strong>📖 论文导读与核心综述：</strong><br/>
          ${data.overview || ''}
        </div>

        <div class="paper-links-bar">
          ${data.code ? `<a href="${data.code}" target="_blank" class="btn-link-action"><i class="fa-brands fa-github"></i> 开源源码</a>` : ''}
          ${data.video ? `<a href="${data.video}" target="_blank" class="btn-link-action"><i class="fa-solid fa-play"></i> 演示视频</a>` : ''}
          <a href="${getPaperPdfLink(paperId)}" target="_blank" class="btn-link-action"><i class="fa-solid fa-file-pdf"></i> 原版 PDF</a>
        </div>
      </div>
    `;

    // Sections
    data.sections.forEach((sec) => {
      html += `
        <section class="paper-section" id="${sec.id}">
          <div class="section-header">
            <span class="section-badge">${sec.sectionNumber || ''}</span>
            <div>
              <h2>${sec.title}</h2>
              <div class="zh-sec-title">${sec.chineseTitle || ''}</div>
            </div>
          </div>
      `;

      // Embedded Figure
      if (sec.figure && sec.figure.image) {
        html += `
          <div class="figure-card">
            <img src="${sec.figure.image}" alt="${sec.figure.alt || 'Figure'}" class="zoomable-img" />
            <div class="figure-caption">${sec.figure.caption || ''}</div>
          </div>
        `;
      }

      // Paragraphs
      sec.paragraphs.forEach((p) => {
        html += `
          <div class="paragraph-card">
            <div class="paragraph-meta">
              <span class="para-badge">P${p.pIndex}</span>
              ${p.logicRole ? `<span class="para-logic-role">【${p.logicRole}】</span>` : ''}
              ${p.mainIdea ? `<span class="para-main-idea">${p.mainIdea}</span>` : ''}
            </div>
            <div class="paragraph-sentences">
        `;

        p.sentences.forEach((s) => {
          const enHtml = renderAnnotatedEnglish(s.text, s.vocab);
          const zhHtml = renderAnnotatedChinese(s.translation, s.vocab);

          html += `
            <div class="sentence-block" id="sent-${s.id}">
              <div class="sentence-en-row">
                <button class="btn-speak-sent" data-speak="${encodeURIComponent(s.text)}" title="朗读句子"><i class="fa-solid fa-volume-high"></i></button>
                <div class="sentence-en-text">${enHtml}</div>
              </div>
              <div class="sentence-zh-text">${zhHtml}</div>
            </div>
          `;
        });

        html += `
            </div>
          </div>
        `;
      });

      html += `</section>`;
    });

    dom.articleContent.innerHTML = html;

    // Render KaTeX Math
    if (window.renderMathInElement) {
      window.renderMathInElement(dom.articleContent, {
        delimiters: [
          { left: '$$', right: '$$', display: true },
          { left: '$', right: '$', display: false },
          { left: '\\[', right: '\\]', display: true },
          { left: '\\(', right: '\\)', display: false }
        ],
        throwOnError: false
      });
    }

    // Scroll to top
    dom.readingCanvas.scrollTop = 0;
  }

  function getPaperPdfLink(paperId) {
    if (paperId === 'paper1') return 'A Comparative Study of Nonlinear MPC and Differential-Flatness-Based Control for Quadrotor Agile Flight..pdf';
    if (paperId === 'paper2') return 'Adaptive Incremental Nonlinear Dynamic Inversion for Attitude Control of Micro Air Vehicles .pdf';
    if (paperId === 'paper3') return 'Attitude_Control_of_the_Hydrobatic_Intervention_AUV_Cuttlefish_using_Incremental_Nonlinear_Dynamic_Inversion.pdf';
    return '#';
  }

  // Popover Tooltip Logic
  function showPopover(targetEl, word, ipa, meaning, level) {
    activePopoverElement = targetEl;
    dom.popWord.textContent = word;
    dom.popIpa.textContent = ipa ? `/${ipa}/` : '';
    dom.popMeaning.textContent = meaning || '暂无释义';
    dom.popLevel.textContent = level === 'red' ? '🔴 重点核心词' : (level === 'green' ? '🟢 进阶词汇' : '🔵 专业词汇');

    updatePopoverStarButton(word);

    // Position Popover
    const rect = targetEl.getBoundingClientRect();
    const popWidth = 280;
    let left = rect.left + window.scrollX;
    let top = rect.bottom + window.scrollY + 8;

    if (left + popWidth > window.innerWidth - 20) {
      left = window.innerWidth - popWidth - 20;
    }

    dom.popover.style.left = `${left}px`;
    dom.popover.style.top = `${top}px`;
    dom.popover.classList.add('visible');
  }

  function hidePopover() {
    if (currentPinnedWord) return;
    dom.popover.classList.remove('visible');
    activePopoverElement = null;
  }

  // Drawer Update
  function updateDrawer() {
    const dict = getStarredVocab();
    const keys = Object.keys(dict);
    if (keys.length === 0) {
      dom.drawerList.innerHTML = `<div style="text-align:center;padding:40px;color:var(--text-muted);font-size:13px;">暂无收藏生词，点击单词卡片上的 ⭐ 即可收藏。</div>`;
      return;
    }

    let html = '';
    keys.forEach(k => {
      const item = dict[k];
      html += `
        <div class="drawer-item">
          <div class="drawer-item-head">
            <span class="drawer-word">${item.word}</span>
            <div>
              <button class="btn-icon btn-drawer-speak" data-word="${item.word}" title="发音"><i class="fa-solid fa-volume-high"></i></button>
              <button class="btn-icon btn-drawer-del" data-word="${item.word}" title="取消收藏"><i class="fa-solid fa-trash"></i></button>
            </div>
          </div>
          ${item.ipa ? `<div style="font-size:12px;color:var(--text-muted);font-family:var(--font-mono);">/${item.ipa}/</div>` : ''}
          <div class="drawer-meaning">${item.meaning}</div>
        </div>
      `;
    });
    dom.drawerList.innerHTML = html;
  }

  // Event Listeners Setup
  function setupEventListeners() {
    // Navigation items click
    dom.paperNavList.addEventListener('click', (e) => {
      const item = e.target.closest('.paper-nav-item');
      if (!item) return;
      loadPaper(item.dataset.paper);
    });

    // View Mode toggles
    document.querySelectorAll('[data-mode]').forEach(btn => {
      btn.addEventListener('click', () => {
        document.querySelectorAll('[data-mode]').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        viewMode = btn.dataset.mode;
        document.body.className = document.body.className.replace(/mode-[a-z-]+/g, '').trim();
        if (viewMode === 'en-only') document.body.classList.add('mode-en-only');
        if (viewMode === 'zh-only') document.body.classList.add('mode-zh-only');
      });
    });

    // Delegated Vocab Word Hover / Click
    dom.articleContent.addEventListener('mouseenter', (e) => {
      const el = e.target.closest('.vocab-word');
      if (!el || currentPinnedWord) return;
      showPopover(el, el.dataset.word, el.dataset.ipa, el.dataset.meaning, el.dataset.level);
    }, true);

    dom.articleContent.addEventListener('mouseleave', (e) => {
      const el = e.target.closest('.vocab-word');
      if (el && !currentPinnedWord) {
        hidePopover();
      }
    }, true);

    dom.articleContent.addEventListener('click', (e) => {
      const el = e.target.closest('.vocab-word');
      if (el) {
        if (currentPinnedWord === el.dataset.word) {
          currentPinnedWord = null;
          el.classList.remove('active-pinned');
          hidePopover();
        } else {
          document.querySelectorAll('.vocab-word.active-pinned').forEach(p => p.classList.remove('active-pinned'));
          currentPinnedWord = el.dataset.word;
          el.classList.add('active-pinned');
          showPopover(el, el.dataset.word, el.dataset.ipa, el.dataset.meaning, el.dataset.level);
        }
        return;
      }

      // Sentence TTS button
      const speakBtn = e.target.closest('.btn-speak-sent');
      if (speakBtn) {
        const text = decodeURIComponent(speakBtn.dataset.speak);
        speakWord(text, 'en-US');
        return;
      }

      // Image Zoom Lightbox
      const img = e.target.closest('.zoomable-img');
      if (img) {
        dom.lightboxImg.src = img.src;
        dom.lightbox.classList.add('visible');
        return;
      }

      // Click outside to unpin popover
      if (!e.target.closest('#vocabPopover')) {
        currentPinnedWord = null;
        document.querySelectorAll('.vocab-word.active-pinned').forEach(p => p.classList.remove('active-pinned'));
        dom.popover.classList.remove('visible');
      }
    });

    // Popover Buttons
    dom.btnAudioUs.addEventListener('click', () => {
      speakWord(dom.popWord.textContent, 'en-US');
    });

    dom.btnAudioUk.addEventListener('click', () => {
      speakWord(dom.popWord.textContent, 'en-GB');
    });

    dom.btnStar.addEventListener('click', () => {
      const word = dom.popWord.textContent;
      toggleStarWord(word, {
        ipa: dom.popIpa.textContent.replace(/\//g, ''),
        meaning: dom.popMeaning.textContent
      });
    });

    dom.btnPin.addEventListener('click', () => {
      if (currentPinnedWord) {
        currentPinnedWord = null;
        dom.popover.classList.remove('visible');
      } else {
        currentPinnedWord = dom.popWord.textContent;
      }
    });

    // Lightbox Close
    dom.lightbox.addEventListener('click', () => {
      dom.lightbox.classList.remove('visible');
    });

    // Drawer Controls
    dom.btnOpenDrawer.addEventListener('click', () => {
      updateDrawer();
      dom.vocabDrawer.classList.add('open');
    });

    dom.btnCloseDrawer.addEventListener('click', () => {
      dom.vocabDrawer.classList.remove('open');
    });

    dom.drawerList.addEventListener('click', (e) => {
      const speak = e.target.closest('.btn-drawer-speak');
      if (speak) {
        speakWord(speak.dataset.word, 'en-US');
        return;
      }
      const del = e.target.closest('.btn-drawer-del');
      if (del) {
        toggleStarWord(del.dataset.word, {});
        updateDrawer();
      }
    });

    // Theme Toggle
    dom.btnTheme.addEventListener('click', () => {
      const isDark = document.body.getAttribute('data-theme') === 'dark';
      document.body.setAttribute('data-theme', isDark ? 'light' : 'dark');
      dom.btnTheme.innerHTML = isDark ? '<i class="fa-solid fa-moon"></i>' : '<i class="fa-solid fa-sun"></i>';
    });

    // Font size adjustments
    let currentFontSize = 15.5;
    dom.btnFontDec.addEventListener('click', () => {
      if (currentFontSize > 13) currentFontSize -= 1;
      document.querySelectorAll('.sentence-en-text').forEach(el => el.style.fontSize = `${currentFontSize}px`);
    });

    dom.btnFontInc.addEventListener('click', () => {
      if (currentFontSize < 22) currentFontSize += 1;
      document.querySelectorAll('.sentence-en-text').forEach(el => el.style.fontSize = `${currentFontSize}px`);
    });
  }

  // Initialize
  document.addEventListener('DOMContentLoaded', () => {
    setupEventListeners();
    loadPaper('paper1');
  });

})();
