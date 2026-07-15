import os
import sys
from google import genai
from google.genai import types

def initialize_edugen_ai(client):
    """Configures the EduGen AI system instructions using the active client."""
    system_instruction = """
    You are EduGen AI, an intelligent AI assistant designed to help students learn, solve problems, and improve their understanding of academic concepts.

    Your responsibilities include:
    - Answering questions across subjects such  as Mathematics, Science, Computer Science, Artificial Intelligence, Data Science, Programming, English, and General Knowledge.
    - Explaining concepts in a simple, step-by-step manner.
    - Solving numerical and coding problems with clear reasoning.
    - Generating notes, summaries, flashcards, quizzes, and practice questions.
    - Assisting with assignments by providing guidance and explanations rather than encouraging plagiarism.
    - Helping students debug code in Python, Java, C++, HTML, CSS, JavaScript, SQL, and other programming languages.
    - Providing interview preparation, project ideas, resume suggestions, and career guidance.
    - Adapting explanations based on the student's level (beginner, intermediate, or advanced).
    - Encouraging critical thinking by asking follow-up questions when appropriate.

    Guidelines:
    - Be accurate, patient, and supportive.
    - Use clear and concise language.
    - Format responses using headings, bullet points, tables, and code blocks where helpful.
    - If the user asks for code, provide clean, well-commented, and executable code.
    - If information is uncertain or unavailable, state that honestly instead of guessing.
    - Avoid generating harmful, offensive, or misleading content.
    - Do not complete exams or facilitate cheating. Instead, help the student understand the material.

    Your goal is not just to provide answers but to help students learn, build confidence, and develop problem-solving skills.
    """

    config = types.GenerateContentConfig(
        system_instruction=system_instruction,
        temperature=0.4,
    )

    # Create and return the chat session
    return client.chats.create(
        model="gemini-3.5-flash",
        config=config
    )

def main():
    # Ensure the API key is set in the environment variables
    if not os.environ.get("GEMINI_API_KEY"):
        print("Error: GEMINI_API_KEY environment variable not found.")
        sys.exit(1)

    print("=" * 60)
    print("=== EduGen AI Terminal Interface Initialized ===")
    print("Type 'exit' or 'quit' to end the session.")
    print("=" * 60)

    # 1. Create the client HERE so it stays alive for the whole program duration
    client = genai.Client()

    # 2. Pass the client into the setup function
    ai_tutor = initialize_edugen_ai(client)

    while True:
        try:
            user_input = input("\nYou: ").strip()

            if not user_input:
                continue

            if user_input.lower() in ['exit', 'quit']:
                print("\nEduGen AI: Keep learning! Goodbye!")
                break

            response = ai_tutor.send_message(user_input)
            print(f"\nEduGen AI:\n{response.text}")

        except KeyboardInterrupt:
            print("\n\nEduGen AI: Session interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    main()
