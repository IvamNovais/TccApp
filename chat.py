from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
chatbot = ChatBot("ifOrmacao")

conversas = [
             "oi",
             "oi,qual sua duvida hoje?",
             "quantas horas eu tenho que fazer de acc",
             "de acc sao 40 horas",
             "em que periodo posso comecar a fazer estagio",
             "A partir do 5 periodo",
             "quantas horas tenho que fazer de estagio",
             "sao 300 horas"

]
Trainer = ListTrainer(chatbot)
Trainer.train(conversas)
while(True):
  resposta = chatbot.get_response(input("usuario: "))
  print(resposta)