
from HelloOllama import SmartAgent as blud
sarmaluta=blud ()
question=input ("Question Sarmaluta: ").strip()
while question != '/pa':
    if question != "":
        print (sarmaluta.answer(question))
    question=input("Question blud? ").strip()
