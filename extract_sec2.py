import docx

doc = docx.Document(r'D:\tj\Graduation Project\开题报告\PX4研究现状_正式清洁修改版.docx')

with open(r'D:\tj\Graduation Project\section2_analysis.txt', 'w', encoding='utf-8') as f:
    for p_idx in range(21, 47):
        p = doc.paragraphs[p_idx]
        f.write(f'=== Paragraph {p_idx} ===\n')
        full_text = p.text.strip()
        f.write(f'Full text: {full_text}\n\n')
        f.write('Runs breakdown:\n')
        for r_idx, r in enumerate(p.runs):
            rPr = r._r.rPr
            color_val = None
            if rPr is not None:
                c = rPr.xpath('./w:color/@w:val')
                if c:
                    color_val = c[0]
            
            # check bold
            is_b = False
            if rPr is not None:
                b_elem = rPr.xpath('./w:b')
                if b_elem:
                    val = b_elem[0].get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val')
                    if val is None or val in ['1', 'true']:
                        is_b = True
            
            is_blue = (color_val is not None and color_val.lower() in ['0000ff', '0070c0', '418ab3', '1f4e79', '2e75b6', '002060', 'blue'])
            
            tag = 'NORMAL'
            if is_blue and is_b:
                tag = 'BLUE_AND_BOLD (Need Re-confirm Content)'
            elif is_blue:
                tag = 'BLUE (Problematic Expression)'
            elif is_b:
                tag = 'BOLD'
                
            f.write(f'  [{tag}] "{r.text}"\n')
        f.write('\n' + '-'*60 + '\n\n')
print('Done writing section2_analysis.txt')
