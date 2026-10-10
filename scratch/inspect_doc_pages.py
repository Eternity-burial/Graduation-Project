import sys
sys.stdout.reconfigure(encoding='utf-8')
import win32com.client as win32
import os

word = win32.gencache.EnsureDispatch('Word.Application')
word.Visible = False
doc_path = os.path.abspath(r"开题报告\开题报告_claude版.docx")
doc = word.Documents.Open(doc_path, ReadOnly=True)

try:
    page_count = doc.ComputeStatistics(2) # 2 = wdStatisticPages
    word_count = doc.ComputeStatistics(0) # 0 = wdStatisticWords
    char_count = doc.ComputeStatistics(3) # 3 = wdStatisticCharacters
    char_no_spaces = doc.ComputeStatistics(4) # 4 = wdStatisticCharactersWithSpaces
    print(f"Document Statistics:")
    print(f"  Pages: {page_count}")
    print(f"  Words: {word_count}")
    print(f"  Characters: {char_count}")
    print(f"  Characters with spaces: {char_no_spaces}")
finally:
    doc.Close(False)
    word.Quit()
