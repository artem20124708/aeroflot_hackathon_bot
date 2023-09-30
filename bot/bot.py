import telebot
import requests
import json
import json
from telebot import types
from roadDocs import roadDocsParse

bot = telebot.TeleBot('5483501827:AAH99o-4cJpBJvyGES1nXESQLEO59ynUKpA')

#Стартовое меню
@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Здравствуйте, <b>{message.from_user.first_name}!</b>\nВоспользуйтесь меню.'
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buyTickets_btn = types.KeyboardButton('✈️ Купить билет')
    onlineRegister_btn = types.KeyboardButton('🎫 Онлайн-регистрация')
    bookingStatus_btn = types.KeyboardButton('📔 Статус бронирования')
    onlineTimetable_btn = types.KeyboardButton('🗓 Информация о рейсе')
    tecSupport_btn = types.KeyboardButton('❓ Тех. поддержка')
    specialOffers_btn = types.KeyboardButton('🎁 Спецпредложения')
    business_btn = types.KeyboardButton('💼 Бизнес')
    information_btn = types.KeyboardButton('📌 Информация')
    covidInfo_btn = types.KeyboardButton('🦠 Информация о Covid19')
    markup.add(buyTickets_btn, onlineRegister_btn, bookingStatus_btn, onlineTimetable_btn, tecSupport_btn, specialOffers_btn, business_btn, information_btn, covidInfo_btn)
    bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)

#Сценарий по нажатию кнопок меню
@bot.message_handler(content_types=['text'])
def firstStep(message):
    if message.text == '✈️ Купить билет':
        markup = types.InlineKeyboardMarkup(row_width=1)
        buyTicketsSite_btn = types.InlineKeyboardButton('Сайт Aeroflot', url='https://www.aeroflot.ru/sb/app/ru-ru#/search')
        buyTicketsBot_btn = types.InlineKeyboardButton('Использовать бот (ДЕМО)', callback_data='buyTickets_useBot')
        back_btn = types.InlineKeyboardButton('В меню', callback_data='back')
        markup.add(buyTicketsSite_btn, buyTicketsBot_btn, back_btn)
        bot.send_message(message.chat.id, 'Вы можете воспользоваться <b>ботом</b> или <b>перейти на сайт</b>.', parse_mode='html', reply_markup=markup)
    if message.text == '🎫 Онлайн-регистрация':
        markup = types.InlineKeyboardMarkup()
        onlineRegisterSite_btn = types.InlineKeyboardButton('Онлайн-регистрация', url='https://www.aeroflot.ru/sb/ckin/app/ru-ru#/search_pnrs')
        back_btn = types.InlineKeyboardButton('В меню', callback_data='back')
        markup.add(onlineRegisterSite_btn, back_btn)
        bot.send_message(message.chat.id, 'Чтобы пройти онлайн-регистрацию <b>перейдите на сайт</b>.', parse_mode='html', reply_markup=markup)
    if message.text == '📔 Статус бронирования':
        markup = types.InlineKeyboardMarkup(row_width=1)
        bookingStatusSite_btn = types.InlineKeyboardButton('Сайт Aeroflot', url='https://www.aeroflot.ru/sb/pnr/app/ru-ru#/search')
        bookingStatusBot_btn = types.InlineKeyboardButton('Использовать бот (ДЕМО)', callback_data='bookingStatus_useBot')
        back_btn = types.InlineKeyboardButton('В меню', callback_data='back')
        markup.add(bookingStatusSite_btn, bookingStatusBot_btn, back_btn)
        bot.send_message(message.chat.id, 'Вы можете воспользоваться <b>ботом</b> или <b>перейти на сайт</b>.', parse_mode='html', reply_markup=markup)
    if message.text == '🗓 Информация о рейсе':
        markup = types.InlineKeyboardMarkup(row_width=1)
        onlineTimetableSite_btn = types.InlineKeyboardButton('Сайт Aeroflot', url='https://flights.aeroflot.ru/ru-ru/onlineboard')
        onlineTimetableBot_btn = types.InlineKeyboardButton('Использовать бот', callback_data='onlineTimetable_useBot')
        back_btn = types.InlineKeyboardButton('В меню', callback_data='back')
        markup.add(onlineTimetableSite_btn, onlineTimetableBot_btn, back_btn)
        bot.send_message(message.chat.id, 'Вы можете воспользоваться <b>ботом</b> или <b>перейти на сайт</b>.', parse_mode='html', reply_markup=markup)
    if message.text == '❓ Тех. поддержка':
        markup = types.InlineKeyboardMarkup()
        tecSupportSite_btn = types.InlineKeyboardButton('Сайт Aeroflot', url='https://www.aeroflot.ru/ru-ru/help')
        back_btn = types.InlineKeyboardButton('В меню', callback_data='back')
        markup.add(tecSupportSite_btn, back_btn)
        bot.send_message(message.chat.id, 'Для обращения в тех. поддержку воспользуйтесь <b>формой на сайте</b>.', parse_mode='html', reply_markup=markup)
    if message.text == '🎁 Спецпредложения':
        markup = types.InlineKeyboardMarkup(row_width=1)
        specialOffersRates_btn = types.InlineKeyboardButton('Тарифы и акции', url='https://www.aeroflot.ru/ru-ru/destination_offers')
        specialOffersGiftsCert_btn = types.InlineKeyboardButton('Подарочные сертификаты', url='https://www.aeroflot.ru/giftcert/buy?_preferredLanguage=ru')
        specialOffersForPensioners_btn = types.InlineKeyboardButton('Для пенсионеров', url='https://www.aeroflot.ru/ru-ru/pensioner')
        specialOffersForYouth_btn = types.InlineKeyboardButton('Для молодёжи', url='https://www.aeroflot.ru/ru-ru/youth_fares')
        specialOffersCallCenter_btn = types.InlineKeyboardButton('Соединение с контакт центром', callback_data='callCenter')
        back_btn = types.InlineKeyboardButton('В меню', callback_data='back')
        markup.add(specialOffersRates_btn, specialOffersGiftsCert_btn, specialOffersForPensioners_btn, specialOffersForYouth_btn, specialOffersCallCenter_btn, back_btn)
        bot.send_message(message.chat.id, 'Спецпредложения:', reply_markup=markup)
    if message.text == '💼 Бизнес':
        markup = types.InlineKeyboardMarkup(row_width=1)
        businessTrucking_btn = types.InlineKeyboardButton('Грузовые перевозки', callback_data='businessTrucking')
        businessPass_btn = types.InlineKeyboardButton('Деловой проездной', url='https://www.aeroflot.ru/ru-ru/special_offers/business_travel')
        businessCorporateClients_btn = types.InlineKeyboardButton('Корпоративным клиентам', callback_data='businessCorporateClients')
        back_btn = types.InlineKeyboardButton('В меню', callback_data='back')
        markup.add(businessTrucking_btn, businessPass_btn, businessCorporateClients_btn, back_btn)
        bot.send_message(message.chat.id, 'Бизнес:', reply_markup=markup)
    if message.text == '📌 Информация':
        markup = types.InlineKeyboardMarkup(row_width=1)
        informationInAirport_btn = types.InlineKeyboardButton('В аэропорту', callback_data='informationInAirport')
        informationOnBoard_btn = types.InlineKeyboardButton('На борту', callback_data='informationOnBoard')
        informationForPassengers_btn = types.InlineKeyboardButton('Для пассажиров', callback_data='informationForPassengers')
        informationLegalInfo_btn = types.InlineKeyboardButton('Правовая информация', callback_data='informationLegalInfo')
        back_btn = types.InlineKeyboardButton('В меню', callback_data='back')
        markup.add(informationInAirport_btn, informationOnBoard_btn, informationForPassengers_btn, informationLegalInfo_btn, back_btn)
        bot.send_message(message.chat.id, 'Информация:', reply_markup=markup)
    if message.text == '🦠 Информация о Covid19':
        markup = types.InlineKeyboardMarkup(row_width=1)
        informationCovidSiteInfo_btn = types.InlineKeyboardButton('Сайт Aeroflot', url='https://www.aeroflot.ru/ru-ru/covid-19')
        back_btn = types.InlineKeyboardButton('В меню', callback_data='back')
        markup.add(informationCovidSiteInfo_btn, back_btn)
        bot.send_message(message.chat.id, 'Ознакомтесь с ифнормацией о Covid19 на <b>сайте</b>:', parse_mode='html', reply_markup=markup)


#Сценарий по нажатию inline кнопок
@bot.callback_query_handler(func=lambda call:True)
def inlineButtonsReaction(call):
    if call.data == 'buyTickets_useBot':
        outCity_msg = bot.send_message(call.message.chat.id, 'Введите <b>город вылета</b>.', parse_mode='html')
        bot.register_next_step_handler(outCity_msg, outCity_get)
    if call.data == 'bookingStatus_useBot':
        booking_example = open('img/booking_code.jpg', 'rb')
        bot.send_message(call.message.chat.id, 'Введите <u>код бронирования</u>.', parse_mode='html')
        bookingCodeExample = bot.send_photo(call.message.chat.id, booking_example)
        bot.register_next_step_handler(bookingCodeExample, bookingCode_get)
    if call.data == 'onlineTimetable_useBot':
        flightNum_msg = bot.send_message(call.message.chat.id, 'Введите <b>номер рейса</b> и <b>дату вылета</b> в формате ГГГГ-ММ-ДД через пробел.\nНапример: SU1711 2022-09-15', parse_mode='html')
        bot.register_next_step_handler(flightNum_msg, raiseNum)
    if call.data == 'backTicketYes':
        inDate_msg = bot.send_message(call.message.chat.id, 'Введите <b>дату вылета</b> в формате ГГГГ-ММ-ДД.\nНапример: 2022-09-16', parse_mode='html')
        bot.register_next_step_handler(inDate_msg, passCount_get)
    if call.data == 'backTicketNo':
        markup = types.InlineKeyboardMarkup()
        back_btn = types.InlineKeyboardButton('В меню', callback_data='back')
        markup.add(back_btn)
        bot.send_message(call.message.chat.id, 'ДЕМОВЕРСИЯ', reply_markup=markup)
    if call.data == 'callCenter':
        bot.send_message(call.message.chat.id, '<b>Контакты</b>:\n+7 (800) 444-55-55 — бесплатно по России\n+7 (495) 223-55-55 — бесплатно для Москвы', parse_mode='html')
    if call.data == 'businessTrucking':
        markup = types.InlineKeyboardMarkup(row_width=1)
        businessTruckingHowSend_btn = types.InlineKeyboardButton('Как отправить груз', url='https://www.aeroflot.ru/ru-ru/business/cargo_transport/howto')
        businessTruckingCallCenter_btn = types.InlineKeyboardButton('Соединение с контакт центром', callback_data='callCenter')
        back_btn = types.InlineKeyboardButton('В меню', callback_data='back')
        markup.add(businessTruckingHowSend_btn, businessTruckingCallCenter_btn, back_btn)
        bot.send_message(call.message.chat.id, 'Грузовые перевозки:', reply_markup=markup)
    if call.data == 'businessCorporateClients':
        markup = types.InlineKeyboardMarkup(row_width=1)
        businessCorporateClientsLoyaltyProg_btn = types.InlineKeyboardButton('Программа корпоративной лояльности', url='https://www.aeroflot.ru/ru-ru/business/corporate/loyalty_programme')
        businessCoprorateClientsDirectContract_btn = types.InlineKeyboardButton('Прямой договор (обслуживание в офисе)', url='https://www.aeroflot.ru/ru-ru/business/corporate/direct_cooperation')
        businessCorporateClientsCallCenter_btn = types.InlineKeyboardButton('Соединение с контакт центром', callback_data='callCenter')
        back_btn = types.InlineKeyboardButton('В меню', callback_data='back')
        markup.add(businessCorporateClientsLoyaltyProg_btn, businessCoprorateClientsDirectContract_btn, businessCorporateClientsCallCenter_btn, back_btn)
        bot.send_message(call.message.chat.id, 'Корпоративным клиентам', reply_markup=markup)
    if call.data == 'informationInAirport':
        markup = types.InlineKeyboardMarkup(row_width=1)
        informationInAirportDocuments_btn = types.InlineKeyboardButton('Дорожные документы', callback_data='informationInAirportDocuments')
        informationInAirportControl_btn = types.InlineKeyboardButton('Паспортно-визовый контроль', url='https://www.aeroflot.ru/ru-ru/information/airport/passport')
        informationInAirportPreFlight_btn = types.InlineKeyboardButton('Предполётный досмотр', url='https://www.aeroflot.ru/ru-ru/information/airport/security')
        informationAirportCallCenter_btn = types.InlineKeyboardButton('Соединение с контакт центром', callback_data='callCenter')
        back_btn = types.InlineKeyboardButton('В меню', callback_data='back')
        markup.add(informationInAirportDocuments_btn, informationInAirportControl_btn, informationInAirportPreFlight_btn, informationAirportCallCenter_btn, back_btn)
        bot.send_message(call.message.chat.id, 'В аэропорту:', reply_markup=markup)
    if call.data == 'informationOnBoard':
        markup = types.InlineKeyboardMarkup(row_width=1)
        informationOnBoardSeats_btn = types.InlineKeyboardButton('Схема посадочных мест', url='https://www.aeroflot.ru/ru-ru/information/onboard/seating')
        informationOnBoardDining_btn = types.InlineKeyboardButton('Питание на борту', url='https://www.aeroflot.ru/ru-ru/information/onboard/dining')
        informationOnBoardDevices_btn = types.InlineKeyboardButton('Электронные устройства', url='https://www.aeroflot.ru/ru-ru/information/onboard/entertainment')
        informationOnBoardCallCenter_btn = types.InlineKeyboardButton('Соединение с контакт центром', callback_data='callCenter')
        back_btn = types.InlineKeyboardButton('В меню', callback_data='back')
        markup.add(informationOnBoardSeats_btn, informationOnBoardDining_btn, informationOnBoardDevices_btn, informationOnBoardCallCenter_btn, back_btn)
        bot.send_message(call.message.chat.id, 'На борту:', reply_markup=markup)
    if call.data == 'informationForPassengers':
        markup = types.InlineKeyboardMarkup(row_width=1)
        informationForPassengersKids_btn = types.InlineKeyboardButton('С детьми', url='https://www.aeroflot.ru/ru-ru/information/special/kids')
        informationForPassengersAnimals_btn = types.InlineKeyboardButton('С животными', url='https://www.aeroflot.ru/ru-ru/information/special/animals')
        informationForPassengersDifSit_btn = types.InlineKeyboardButton('В сложных жизненных ситуациях', url='https://www.aeroflot.ru/ru-ru/information/special/difficult_situations')
        informationForPassengersDisabled_btn = types.InlineKeyboardButton('Пассажирам с ограничениями жизнедеятельности', url='https://www.aeroflot.ru/ru-ru/information/special/disabled')
        informationForPassengersBanned_btn = types.InlineKeyboardButton('Запрещенные к перевозке предметы', url='https://www.aeroflot.ru/ru-ru/information/airport/security')
        informationForPassengersCallCenter_btn = types.InlineKeyboardButton('Соединение с контакт центром', callback_data='callCenter')
        back_btn = types.InlineKeyboardButton('В меню', callback_data='back')
        markup.add(informationForPassengersKids_btn, informationForPassengersAnimals_btn, informationForPassengersDifSit_btn, informationForPassengersDisabled_btn, informationForPassengersBanned_btn, informationForPassengersCallCenter_btn, back_btn)
        bot.send_message(call.message.chat.id, 'Для пассажиров:', reply_markup=markup)
    if call.data == 'informationLegalInfo':
        markup = types.InlineKeyboardMarkup(row_width=1)
        informationLegalInfoTruckAgrmnt_btn = types.InlineKeyboardButton('Договор перевозки', url='https://www.aeroflot.ru/ru-ru/information/legal/contract')
        informationLegalInfoInsurance_btn = types.InlineKeyboardButton('Информация о страховщике', url='https://www.aeroflot.ru/ru-ru/information/legal/insurance')
        informationLegalInfoForeign_btn = types.InlineKeyboardButton('Оформление электронной визы для иностранцев', url='https://evisa.kdmid.ru/ru-RU/Home/Index')
        informationLegalInfoCancel_btn = types.InlineKeyboardButton('При задержке/отмене рейсов', url='https://www.aeroflot.ru/ru-ru/information/legal/liability')
        informationLegalInfoCallCenter_btn = types.InlineKeyboardButton('Соединение с контакт центром', callback_data='callCenter')
        back_btn = types.InlineKeyboardButton('В меню', callback_data='back')
        markup.add(informationLegalInfoTruckAgrmnt_btn, informationLegalInfoInsurance_btn, informationLegalInfoForeign_btn, informationLegalInfoCancel_btn, informationLegalInfoCallCenter_btn, back_btn)
        bot.send_message(call.message.chat.id, 'Правовая информация:', reply_markup=markup)
    if call.data == 'back':
        markupKeys = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buyTickets_btn = types.KeyboardButton('✈️ Купить билет')
        onlineRegister_btn = types.KeyboardButton('🎫 Онлайн-регистрация')
        bookingStatus_btn = types.KeyboardButton('📔 Статус бронирования')
        onlineTimetable_btn = types.KeyboardButton('🗓 Информация о рейсе')
        tecSupport_btn = types.KeyboardButton('❓ Тех. поддержка')
        specialOffers_btn = types.KeyboardButton('🎁 Спецпредложения')
        business_btn = types.KeyboardButton('💼 Бизнес')
        information_btn = types.KeyboardButton('📌 Информация')
        covidInfo_btn = types.KeyboardButton('🦠 Информация о Covid19')
        markupInline = types.InlineKeyboardMarkup(row_width=1)
        ratingFirst_btn = types.InlineKeyboardButton('Пассажирам с животными (ДЕМО)', url='https://www.aeroflot.ru/ru-ru/information/special/animals',callback_data='ratingFirst')
        ratingSecond_btn = types.InlineKeyboardButton('При задержке/отмене рейсов (ДЕМО)', url='https://www.aeroflot.ru/ru-ru/information/legal/liability',callback_data='ratingSecond')
        ratingThird_btn = types.InlineKeyboardButton('Предполётный досмотр (ДЕМО)', url='https://www.aeroflot.ru/ru-ru/information/airport/security',callback_data='ratingThird')
        markupKeys.add(buyTickets_btn, onlineRegister_btn, bookingStatus_btn, onlineTimetable_btn, tecSupport_btn, specialOffers_btn, business_btn, information_btn, covidInfo_btn)
        markupInline.add(ratingFirst_btn, ratingSecond_btn, ratingThird_btn)
        bot.send_message(call.message.chat.id, 'Вы в главном меню', reply_markup=markupKeys)
        bot.send_message(call.message.chat.id, 'Популярные запросы:', reply_markup=markupInline)
    if call.data == 'informationInAirportDocuments':
        markup = types.InlineKeyboardMarkup(row_width=1)
        roadDocsInfo_msg = roadDocsParse()
        moreInfo_btn = types.InlineKeyboardButton('Подробнее на сайте.', url='https://www.aeroflot.ru/ru-ru/information/preparation/regulations_papers')
        back_btn = types.InlineKeyboardButton('В меню', callback_data='back')
        markup.add(moreInfo_btn, back_btn)
        bot.send_message(call.message.chat.id, roadDocsInfo_msg, reply_markup=markup)
#Взятие города вылета
def outCity_get(message):
    outCity = message.text   
    inCity_msg = bot.send_message(message.chat.id, 'Введите <b>город прибытия</b>.', parse_mode='html')
    bot.register_next_step_handler(inCity_msg, inCity_get)

#Взятие города прибытия
def inCity_get(message):
    inCity = message.text
    outDate_msg = bot.send_message(message.chat.id, 'Введите <b>дату вылета</b> в формате ГГГГ-ММ-ДД.\nНапример: 2022-09-15', parse_mode='html')
    bot.register_next_step_handler(outDate_msg, outDate_get)
    
#Взятие даты вылета
def outDate_get(message):
    outDate = message.text
    markup = types.InlineKeyboardMarkup()
    backTicketYes_btn = types.InlineKeyboardButton('Да', callback_data='backTicketYes')
    backTicketNo_btn = types.InlineKeyboardButton('Нет', callback_data='backTicketNo')
    markup.add(backTicketYes_btn, backTicketNo_btn)
    bot.send_message(message.chat.id, 'Нужен обратный билет?', reply_markup=markup)
    
#Взятие даты прибытия
def passCount_get(message):
    inDate = message.text
    markup = types.InlineKeyboardMarkup()
    back_btn = types.InlineKeyboardButton('В меню', callback_data='back')
    markup.add(back_btn)
    passCount_msg = bot.send_message(message.chat.id, 'ДЕМОВЕРСИЯ', reply_markup=markup)
    
#Взятие кода бронирования
def bookingCode_get(message):
    bookingCode = message.text
    bookingSurname_msg = bot.send_message(message.chat.id, 'Введите фамилию <u>латиницей</u>.\nПример: IVANOV', parse_mode='html')
    bot.register_next_step_handler(bookingSurname_msg, bookingSurname_get)
    
#Взятие фамилии
def bookingSurname_get(message):
    bookingSurname = message.text
    markup = types.InlineKeyboardMarkup()
    back_btn = types.InlineKeyboardButton('В меню', callback_data='back')
    markup.add(back_btn)
    bot.send_message(message.chat.id, '<b>Статус оплаты</b>: Не оплачен\n<b>Информация по оплате</b>: 4898₽\n<b>Статус документов</b>: Не выпущены\n<b>Время на оплату</b>: 6ч 16мин\n(ДЕМОВЕРСИЯ)', parse_mode='html', reply_markup=markup)

#Взятие номера рейса
def flightNum_get(message):
    log_mes = message.text
    outDate_msg = bot.send_message(message.chat.id, 'Введите <b>дату вылета</b> в формате ГГГГ-ММ-ДД.\nНапример: 2022-09-15', parse_mode='html')
    bot.register_next_step_handler(outDate_msg, )
    
#Запрос в онлайн табло
def raiseNum(message):
    flightInfo = message.text
    if flightInfo.count(' ') == 1:
        flightInfoSplit = flightInfo.split()
        flightNumber = flightInfoSplit[0]
        date = flightInfoSplit[1]
        bot.send_message(message.chat.id, 'Идет поиск...')
        url = "https://flights.aeroflot.ru/api/flights/v1.1/ru/board?type=onlineboard&flightNumber="+flightNumber+"&dateFrom="+date+"+T00:00:00&dateTo="+date+"T00:00:00&timeFrom=00:00:00&timeTo=23:59:59&returnTo=23:59:59"
        payload={}
        headers = {'Cookie': 'sb_pnr_session_id=sb-m9-2-pnr-712ddce03f3ad16810108b9ce723c6b86e7c3690; session-cookie=1714a2768b2780dd8b33d0c318991a242115e6d86ee3196e4b9d0468ea070a06735615f64f0842b2eddabd0b2c492a4f', 'User-Agent':'PostmanRuntime/7.29.2'}
        response = requests.request("GET", url, headers=headers, data=payload)
        data = json.loads(response.text)
        if response.status_code==200 and len(date)==10 and len(flightNumber)==6 and len(data['data']['routes'])>0: 
            if date[4]=="-" and date[7]=='-':
                flightInfo_msg = '<u>Вылет</u>:\n<b>Город вылета</b>: '+data['data']['routes'][0]['leg']['departure']['scheduled']['city']+"\n<b>Аэропорт отправления</b>: "+data['data']['routes'][0]['leg']['departure']['scheduled']['airport']+"\n<b>Время отправления</b>: "+data['data']['routes'][0]['leg']['departure']['times']['scheduledDeparture']['localTime']+'\n<u>Прибытие</u>:'+"\n<b>Город прибытия</b>: "+data['data']['routes'][0]['leg']['arrival']['scheduled']['city']+"\n<b>Аэропорт прибытия</b>: "+data['data']['routes'][0]['leg']['arrival']['scheduled']['airport']+"\n<b>Время прибытия</b>: "+data['data']['routes'][0]['leg']['arrival']['times']['scheduledArrival']['localTime']
                markup = types.InlineKeyboardMarkup()
                back_btn = types.InlineKeyboardButton('В меню', callback_data='back')
                markup.add(back_btn)
                bot.send_message(message.chat.id, flightInfo_msg, parse_mode='html', reply_markup=markup)
    else:
        markup = types.InlineKeyboardMarkup()
        back_btn = types.InlineKeyboardButton('В меню', callback_data='back')
        markup.add(back_btn)
        bot.send_message(message.chat.id, "Рейс не найден. Проверьте правильность введённых данных.", reply_markup=markup)

bot.polling(none_stop=True)