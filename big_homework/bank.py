wimport json
import random


def get_random_digits(count: int) -> str:
    return ''.join(str(random.randint(0, 9)) for i in range(count))


class BankAccount:

    def __init__(self, card_holder: str):
        self.card_holder = card_holder.upper()
        self.money = 0
        self.account_number = get_random_digits(20)
        self.card_number = get_random_digits(16)


class Bank:

    def __init__(self):
        self.bank_accounts = {}

    def open_account(self, card_holder: str):
        person = BankAccount(card_holder)
        #TODO add .__dict__ after person
        self.bank_accounts[person.account_number] = person
        print(self.bank_accounts)
        #json was created for debugging
        # self.writer(self.bank_accounts)
        return person

    def add_money(self, account_number: str, money: int):
        self.bank_accounts[account_number].money += money

    def transfer_money(self, account_number_from: str, account_number_to: str, money: int):
        self.bank_accounts[account_number_from].money -= money
        self.bank_accounts[account_number_to].money += money

    def external_transfer(self, account_number, to_external_account, money):
        self.bank_accounts[account_number].money -= money
        print(f'Банк перевёл {money}$ с вашего счёта {account_number} на внешний счёт {to_external_account}')

    def show_accounts(self):
        print('Ваши открытые счета:')
        for account_number, account in self.bank_accounts.items():
            print(f'Cчёт: {account_number}')
            print(f'   Остаток на счету: {account.money}$')
            print(f'   Номер карты: {account.card_number}')
            print(f'   Держатель карты: {account.card_holder}')

    def writer(self,data):
        with open('test.json','w') as f:
            json.dump(data, f, indent=4)
class Controller:

    def __init__(self):
        self.bank = Bank()

    def run(self):
        print("Здравствуйте, наш банк открылся!")
        while True:
            user_input = int(input("""
            Выберите действие:
            0. Завершить программу
            1. Открыть новый счёт
            2. Просмотреть открытые счета
            3. Положить деньги на счёт
            4. Перевести деньги между счетами
            5. Совершить платёж
            """))
            if user_input == 0:
                print("До свидания!")
                break
            elif user_input == 1:
                user_name = input('Введите имя и фамилию держателя карты (на английском): ')
                account = self.bank.open_account(user_name)
                print(f'Счёт {account.account_number} создан.')
            elif user_input == 2:
                self.bank.show_accounts()
            elif user_input == 3:
                account_number = (input('Введите номер cчёта: '))
                money = int(input('Количество денег: '))
                self.bank.add_money(account_number, money)
            elif user_input == 4:
                pass
            # TODO send money from one account ot another
            elif user_input == 5:
                pass
            # TODO do a payment from an account
            else:
                pass
            # TODO add descripiption that the user entered wrong number

    # logger for logging


if __name__ == '__main__':
    controller = Controller()
    controller.run()
