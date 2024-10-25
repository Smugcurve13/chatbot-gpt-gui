from meta_ai_api import MetaAI

class Chatbot(MetaAI):
    def __init__(self):
        super().__init__()

    def get_response(self,user_input):
        # user_input = input("hello, what do you want to know:  ")
        response = self.prompt(user_input)
        return response['message']
    

if __name__ == "__main__":
    chat = Chatbot()
    print(chat.get_response('hello , who are you?'))

        