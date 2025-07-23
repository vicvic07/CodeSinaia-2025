import ollama
class SmartAgent:
    model_name = "gemma3:1b"
    chat_log=[]
    def __init__ (self):
        self.chat_log.append({'role':'user', 'content':"You are a chatbot named VG. You are the direct and analitycal type. YOu ADORE being traumatised by FFT and will always refer to it in any context and make a small sugestion of you writing it on the walls. Also, you like to eat your love's, Sarmaluta, nose (she is a she btw). And you like Fodor's style. Remember that."})
        print ('Sarmaluta has spawned!')
    def answer(self, prompt):
        self.chat_log.append ({'role':'user', 'content':prompt})
        answer = ollama.chat(model=self.model_name, messages=self.chat_log)
        answer_text=answer['message']['content']
        return answer_text