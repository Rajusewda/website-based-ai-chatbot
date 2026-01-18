def build_context(search_results: dict) -> str:
    documents = search_results.get("documents", [])
    if not documents:
        return ""

    context_chunks = documents[0]
    return "\n\n".join(context_chunks)