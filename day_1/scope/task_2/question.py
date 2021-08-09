"""
Что будет выведено после выполнения кода? Почему?
"""


def transmit_to_space(message):
   
    def data_transmitter():        
        print(message)

    data_transmitter()


print(transmit_to_space("Test message"))

"""
Test message и None. Сначала мы вызываем функцию transmit_to_space, 
в которой инициализируется внутренняя функция и выдает Test message. После чего, принт, который вызывал transmit_to_space
выдает null, потому что transmit_to_space ри выполнении ничего не возвращает
"""