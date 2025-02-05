from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import (CharacterTextSplitter,
                                      RecursiveCharacterTextSplitter)

q1_pdf = "OpenSourceLicenses.pdf"
q2_pdf = "勞動基準法.pdf"


def hw02_1(q1_pdf):
    pdf_loader = PyPDFLoader(q1_pdf)
    ct_splitter = CharacterTextSplitter(chunk_overlap=0)
    chunks = ct_splitter.split_documents(pdf_loader.load())

    return chunks[len(chunks) - 1]

def hw02_2(q2_pdf):
    pdf_loader = PyPDFLoader(q2_pdf)
    pages = pdf_loader.load()

    # 解決分頁內截斷問題
    full_text = "\n".join([page.page_content for page in pages])

    regex_pattern = r"第 (?:[1-9][0-9]|.*) (?:條|章)"
    rct_splitter = RecursiveCharacterTextSplitter(
        chunk_overlap=0,
        chunk_size=20,
        separators=[regex_pattern],
        is_separator_regex=True)

    rct_chunks = rct_splitter.split_text(full_text)

    # debug print
    #print(f"Total chunks: {len(rct_chunks)}")
    #count = 0
    #for chunk in rct_chunks:
    #    count = count + 1
    #    print(f"chunk:{count} ===============")
    #    print(chunk[:200])

    return len(rct_chunks)

#print(hw02_1(q1_pdf))
print(hw02_2(q2_pdf))