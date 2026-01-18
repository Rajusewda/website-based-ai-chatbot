from langchain_text_splitters import RecursiveCharacterTextSplitter


def chunk_text(
    text: str,
    source_url: str,
    title: str,
    chunk_size: int = 500,
    chunk_overlap: int = 100
) -> list[dict]:

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )

    chunks = splitter.split_text(text)

    documents = []
    for chunk in chunks:
        documents.append({
            "content": chunk,
            "metadata": {
                "source": source_url,
                "title": title
            }
        })

    return documents