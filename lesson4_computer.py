import time


class Computer:
    def __init__(self):
        self.__power_up()
        self.__start_power_on_set_test()
        self.__run_downloader()
        self.__launch_the_core_of_operating_system()
        self.__ready_to_use()

    def __power_up(self):
        print('Подача тока на материнскую плату и остальные компоненты компьютера')
        time.sleep(2)
        print('Все компоненты компьютера снабжены питанием и готовы к работе')
        time.sleep(2)

    def __start_power_on_set_test(self):
        print('BIOS начинает проверку всех компонентов компьютера на работоспособность')
        time.sleep(2)
        print('Все компоненты работают корректно!')
        time.sleep(2)

    def __run_downloader(self):
        print('Начинается скачивание всех необходимых программ и драйверов для запуска ОС')
        time.sleep(2)
        print('Установка завершена!')
        time.sleep(2)

    def __launch_the_core_of_operating_system(self):
        print('Запуск операционной системы')
        time.sleep(3)

    def __ready_to_use(self):
        print('Компьютер готов к работе!')
        time.sleep(2)


computer = Computer()
