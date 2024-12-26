import google.generativeai as genai

class MindBotAPI:
    def __init__(self, api_key):
        """
        Initializes the MindBotAPI with your Gemini API key.

        Args:
            api_key: Your Google Gemini API key.
        """
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    def ask(self, question):
        """
        Sends a question to the Gemini API and returns the response.

        Args:
            question: The question to ask the Gemini model.

        Returns:
            str: The text response from the Gemini API.
        """
        try:
            response = self.model.generate_content(question)
            return response.text
        except Exception as e:
            return f"Error: {e}"