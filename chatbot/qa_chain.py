from chatbot.prompt import SYSTEM_PROMPT


class QAChain:
    def __init__(self, llm):
        self.llm = llm

    def answer(self, question: str, context: str) -> str:
        if not context.strip():
            return "The answer is not available on the provided website."

        prompt = (
            f"{SYSTEM_PROMPT}\n\n"
            f"Context:\n{context}\n\n"
            f"Question:\n{question}\n\n"
            f"Answer:"
        )

        response = self.llm.invoke(prompt)

        if isinstance(response, str):
            answer = response.strip()
        else:
            answer = response.content.strip()

        if not answer:
            return "The answer is not available on the provided website."

        return answer