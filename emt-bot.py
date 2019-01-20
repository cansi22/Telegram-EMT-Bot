# python3
import telegram.ext
import json
from urllib import request
import untangle
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters

#Emojis
runner_emoji = u'\U0001F3C3'
sad_emoji = u'\U0001F625'
working_emoji = u'\U000026A0'
bus_emoji = u'\U0001F68C'
train_emoji =u'\U0001F689'
emt_emoji = u'\U0001F687'   

#User Data
TOKEN = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"		#Telegram Bot Token
idClient_EMT = "WEB.SERV.xxxxxxxxxxxxxxxxxxxxxxx"			#EMT id Client
passKey_EMT = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"		#EMT pass key
message_delete = ''



def busEUniRenfe(bot, update):
    bus = 'E'
    parada = '4702'
    print (emt(bus,parada))
    bot.send_message(update.message.chat_id,emt(bus,parada))

def busERenfeuni(bot,update):
    bus = 'E'
    parada = '1027'
    print (emt(bus,parada))
    bot.send_message(update.message.chat_id,emt(bus,parada))
    emt_button(bot, update)

def busECondeUni(bot,update):
    bus = 'E'
    parada = '2603'
    print (emt(bus,parada))
    bot.send_message(update.message.chat_id,emt(bus,parada))

def busEUniConde(bot,update):
    bus = 'E'
    parada = '4281'
    print (emt(bus,parada))
    bot.send_message(update.message.chat_id,emt(bus,parada))

def parada(bot,update,parada):
    bot.send_message(update.message.chat_id,"Introduza el numero de parada")
    print("Parada " + parada)
    print (emt_parada(parada))
    bot.send_message(update.message.chat_id,emt_parada(parada))

def busCasa(bot, update):
    print("Bus Rocio")
    with urllib.request.urlopen(url_12041)as url:
        json12041 = json.loads(url.read().decode())
        print(json12041)
    update.message.reply_text(json12041)
    update.message.reply_text(working_emoji + "En desarrollo" + working_emoji)

def busTj(bot, update):
    print("Bus Tj")
    #with urllib.request.urlopen(url_12041)as url:
    #    json12041 = json.loads(url.read().decode())
    #    print(json12041)
    update.message.reply_text(working_emoji + "En desarrollo" + working_emoji)

def atras (bot, update):
    bot.deleteMessage (update.message.chat.id,update.message.message_id)
    start (bot,update)

def emt(bus,stop):#Funcion que comprueba el tiempo restante del ultimo bus, pasando como parametros el numero de linea y la parada
    url_emt = 'https://servicios.emtmadrid.es:8443/geo/servicegeo.asmx/getArriveStop?idClient=' +  idClient_EMT + '&passKey=' + passKey_EMT + '&idStop=' + stop + '&statistics=&cultureInfo='

    parsed_data = untangle.parse(url_emt)

    #Comprobamos que haya algun bus disponble en la parada
    lista1 = parsed_data.Arrives
    if lista1 =="":
        return (bus_emoji + "Linea " + bus + " no disponible")

    lista = parsed_data.Arrives.Arrive

    #Array con los numeros de linea ordenados
    lines = [str(Arrive.idLine.cdata) for Arrive in lista]
    
    #Array con los tiempo de llegada ordenados
    time = [int(Arrive.TimeLeftBus.cdata)for Arrive in lista]
    
    #Array con la distacia a la parada ordenados
    distance =[str(Arrive.DistanceBus.cdata)for Arrive in lista]

    #Array con los destinos de lso buses ordenados
    destination =[str(Arrive.Destination.cdata)for Arrive in lista]

       
    #Buscamos la posicion del bus "bus" en la lista
    #Si el bus está en la lista lo indicamos
    if (bus in lines):
        min = int (time[lines.index(bus)]/60)
        #Segun el tiempo restante cambia el texto de salida
        if min==1:
            return bus_emoji + "Linea " + lines [lines.index(bus)] + " destino " + destination[lines.index(bus)] + " Queda menos de 1 minuto. Se encuentra a " + distance[lines.index(bus)] + " metros" + runner_emoji + runner_emoji
        elif min==0:
            return bus_emoji + "Linea " + lines [lines.index(bus)] + " destino " + destination[lines.index(bus)] + " Está en la parada" + sad_emoji + sad_emoji
        elif min>20:
            return bus_emoji + "Linea " + lines [lines.index(bus)] + " destino " + destination[lines.index(bus)] + " Quedan mas de 20 minutos. Se encuentra a " + distance[lines.index(bus)] + " metros"
        else:
            return bus_emoji + "Linea " + lines [lines.index(bus)] + " destino " + destination[lines.index(bus)] + " Quedan " + str(min) + " minutos. Se encuentra a " + distance[lines.index(bus)] + " metros"
    #Si no esta sacamos un error de no disponible
    else:
        return (bus_emoji + "Linea " + bus + " no disponible")

#Funcion que comprueba el tiempo restante del ultimo bus, pasando como parametros el numero de linea y la parada
def emt_parada(stop):
    
    while parada == null:
        print ("Bucle")
        parada = update
        print (update)
        url_emt = 'https://servicios.emtmadrid.es:8443/geo/servicegeo.asmx/getArriveStop?idClient=' +  idClient_EMT + '&passKey=' + passKey_EMT + '&idStop=' + stop + '&statistics=&cultureInfo='
    
        parsed_data = untangle.parse(url_emt)
    
        lista = parsed_data.Arrives.Arrive
    
        #Array con los numeros de linea ordenados
        lines = [str(Arrive.idLine.cdata) for Arrive in lista]
        
        #Array con los tiempo de llegada ordenados
        time = [int(Arrive.TimeLeftBus.cdata)for Arrive in lista]
        
        #Array con la distacia a la parada ordenados
        distance =[str(Arrive.DistanceBus.cdata)for Arrive in lista]
    
        #Array con los destinos de lso buses ordenados
        destination =[str(Arrive.Destination.cdata)for Arrive in lista]
    
           
        #Buscamos la posicion del bus "bus" en la lista
        for i in range(0,len(lines)):
            min = int (time[lines.index(i)]/60)
            #Segun el tiempo restante cambia el texto de salida
            if min==1:
                return bus_emoji + "Linea " + lines [lines.index(i)] + " destino " + destination[lines.index(i)] + " Queda menos de 1 minuto. Se encuentra a " + distance[lines.index(i)] + " metros" + runner_emoji + runner_emoji
            elif min==0:
                return bus_emoji + "Linea " + lines [lines.index(i)] + " destino " + destination[lines.index(i)] + " Está en la parada" + sad_emoji + sad_emoji
            elif min>20:
                return bus_emoji + "Linea " + lines [lines.index(i)] + " destino " + destination[lines.index(i)] + " Quedan mas de 20 minutos. Se encuentra a " + distance[lines.index(i)] + " metros"
            else:
                return bus_emoji + "Linea " + lines [lines.index(i)] + " destino " + destination[lines.index(i)] + " Quedan " + str(min) + " minutos. Se encuentra a " + distance[lines.index(i)] + " metros"

def emt_button(bot, update):
    bot.deleteMessage (update.message.chat.id,update.message.message_id)
    keyboard = [[InlineKeyboardButton("E Uni->Renfe", callback_data='Euni'),
                 InlineKeyboardButton("E Renfe->Uni", callback_data='ERenfe')],
                 [InlineKeyboardButton("E Uni->Conde", callback_data='EConde'),
                 InlineKeyboardButton("E Conde->Uni", callback_data='ECondeUni')],
                 [InlineKeyboardButton("Introducir numero parada: PROXIMAMENTE", callback_data='atras')],
                 [InlineKeyboardButton("Atras", callback_data='atras')]]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Elije la linea de EMT:',reply_markup=reply_markup)

def inter_button(bot, update):
    bot.deleteMessage (update.message.chat.id,update.message.message_id)
    keyboard = [[InlineKeyboardButton(working_emoji + "PROXIMAMENTE DISPONIBLE" + working_emoji, callback_data='atras')],
                 [InlineKeyboardButton("Atras", callback_data='atras')]]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Elije la linea de Interurbano:',reply_markup=reply_markup)

def cercanias_button(bot, update):
    bot.deleteMessage (update.message.chat.id,update.message.message_id)
    keyboard = [[InlineKeyboardButton(working_emoji + "PROXIMAMENTE DISPONIBLE" + working_emoji, callback_data='atras')],
                 [InlineKeyboardButton("Atras", callback_data='atras')]]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Elije la linea de Cercanias:',reply_markup=reply_markup)

def button(bot, update):
    query = update.callback_query
    text =query.data
    if text == 'ERenfe':
        busERenfeuni(bot,update.callback_query)
    elif text == 'emt':
        emt_button(bot,update.callback_query)
    elif text == 'Euni':
        busEUniRenfe(bot,update.callback_query)
    elif text == 'Casa':
        busCasa(bot,update.callback_query)
    elif text == 'Tj':
        busTj(bot,update.callback_query)
    elif text == 'EConde':
        busECondeUni(bot,update.callback_query)
    elif text == 'ECondeUni':
        busEUniConde(bot,update.callback_query)
    elif text == 'help':
        help(bot,update.callback_query)
    elif text == 'atras':
        atras(bot,update.callback_query)
    elif text == 'inter':
        inter_button(bot,update.callback_query)
    elif text == 'tren':
        cercanias_button(bot,update.callback_query)
    elif text == 'num_parada':
        bot.send_message(update.callback_query.message.chat_id,"Introduza el numero de parada")
        parada(bot,update.callback_query,text)
    else:
        print ("error")

def start(bot, update):
    
    keyboard2 = [[InlineKeyboardButton(emt_emoji +"EMT", callback_data='emt'),
                 InlineKeyboardButton(bus_emoji + "Interurbano", callback_data='inter'),
                 InlineKeyboardButton(train_emoji +  "Cercanias", callback_data='tren')]]

    reply_markup = InlineKeyboardMarkup(keyboard2)
    update.message.reply_text('Elija el servicio:',reply_markup=reply_markup)

def help(bot, update):
    bot.send_message(update.message.chat_id,"Usa /start para iniciar el bot.")
   
#Devuelve la ip publica
def getIP (bot, update):
    if update.message.chat.id == 497827:
        url = "http://icanhazip.com/"
        r = request.urlopen(url)
        bytecode = r.read()
        ip = bytecode.decode()
        print(ip)
        bot.send_message(update.message.chat_id,"La IP publica es " + ip)

    else:
        bot.send_message(update.message.chat_id,"No se puede usar en este chat")

def echo(bot, update):
    text = update.message.text
    print(text)
    if text == "ping":
        bot.send_message(update.message.chat_id, "pong")

def main():
    print("Iniciando el BOT")

    updater = telegram.ext.Updater(token=TOKEN)

    echo_handler = telegram.ext.MessageHandler(telegram.ext.Filters.text, echo)

    updater.dispatcher.add_handler(echo_handler)
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('help', help))
    updater.dispatcher.add_handler(CommandHandler('ip', getIP))
    updater.dispatcher.add_error_handler(error)
    updater.dispatcher.add_handler(CallbackQueryHandler(button))


    # Iniciamos el bot
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
