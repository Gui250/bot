import telebot

CHAVE_API = "6221388745:AAEUY-VDP7D4BeLvc6527-isbmZ5hpNpHyo"

bot = telebot.TeleBot(CHAVE_API)

@bot.message_handler(commands=["pizza"])
def pizza(mensagem):
    bot.reply_to(mensagem, "Saindo a pizza para sua casa")

@bot.message_handler(commands=["hamburguer"])
def hamburguer(mensagem):
    bot.reply_to(mensagem, "Saindo hamburguer para sua casa")

@bot.message_handler(commands=['salada'])
def salada(mensagem):
    bot.reply_to(mensagem, "Saindo salada para sua casa")


@bot.message_handler(commands=['opcao1'])
def opcao1(mensagem):
    txt = """
    O que você quer? (Clique em uma opção):
    /pizza Pizza 
    /hamburguer Hamburguer
    /salada Salada
    """
    bot.reply_to(mensagem, txt)


@bot.message_handler(commands=['opcao2'])
def opcao2(mensagem):
    bot.reply_to(mensagem, "Para fazer uma reclamação mande uma mensagem para blablabla@gmail.com")



def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
    Escolha uma opção para continuar (Clique no Item): 
    /opcao1 Fazer um pedido 
    /opcao2 Reclamar de um pedido 
    Responder qualquer outra coisa não vai funcionar, clique em uma das opções"""






    bot.reply_to(mensagem, texto)

bot.polling()