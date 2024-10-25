from meta_ai_api import MetaAI

class Chatbot(MetaAI):
    def __init__(self):
        super().__init__()

    def get_response(self, user_input):
        try:
            response = self.prompt(user_input)
            if response and 'message' in response:
                return response  # Returns the entire response for flexibility
            else:
                print("Error: Unexpected response format", response)
                return {"message": "Sorry, I couldn't understand that."}
        except Exception as e:
            print(f"Error in get_response: {e}")
            return {"message": f"Error: {e}"}


if __name__ == "__main__":
    chat = Chatbot()
    print(chat.get_response('hello , who are you?'))

        