
count_end = 2021
# count_cnd = 2021
# кто ходит = 1
# Цикл пока у нас есть конфеты:
#     предлагать игрокам по очереди брать конфеты от 1 до 28, проверяя, кто сейчас ходит
#     сколько конфет осталось
#     если конфет нет, то выйти из цикла и сказать кто победил
#     иначе передаь ход другому

def game_players(num_of_players:int,candy_ammount:int,aloud_ammount_on_turn:int):
    list_of_players = [i for i in range(1,num_of_players+1)]
    i = 0
    while candy_ammount > 0 :
        if aloud_ammount_on_turn > candy_ammount:
            aloud_ammount_on_turn = candy_ammount
        candy_take = PF.input_number_examination(text_in_input=f"Candy left : {candy_ammount} \tPlayer {list_of_players[i]} :",case_def=3,min_num=1,max_num=aloud_ammount_on_turn)
        candy_ammount -= candy_take
        if candy_ammount == 0:
            break
        else :
            if i == num_of_players-1:
                i = 0
            else :
                i += 1

    print(f"Player {list_of_players[i]} took last candy ! he WON! ")

    def start_handler(message):
        if not task.isRunning:
            chat_id = message.chat.id
            bot.send_message(chat_id, 'Привет')
            msg = bot.send_message(chat_id, 'Выбери команду', reply_markup=m.source_markup)
            bot.register_next_step_handler(msg, askAction)
            task.isRunning = True
