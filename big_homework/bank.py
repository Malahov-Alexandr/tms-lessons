import json
import random
import os


def get_random_digits(count: int) -> str:
    return ''.join(str(random.randint(0, 9)) for i in range(count))


class BankAccount:

    def __init__(self, card_holder, money=0.0, card_number=None, account_number=None):
        self.card_holder = card_holder.upper()
        self.money = money
        self.account_number = get_random_digits(20) if account_number is None else account_number
        self.card_number = get_random_digits(16) if card_number is None else card_number


def convert_bank_account_to_dict(bank_account: BankAccount):
    return {'card_holder': bank_account.card_holder,
            'money': bank_account.money,
            'account_number': bank_account.account_number,
            'card_number': bank_account.card_number}


def load_accounts(file_name) -> dict[str, BankAccount]:
    if not os.path.exists(file_name):
        return {}
    with open(file_name, 'r') as file:
        data = json.load(file)
        return {account_number: BankAccount(**data) for account_number, data in data.items()}


def save_accounts(file_name, bank_accounts):
    with open(file_name, 'w') as file:
        json.dump({account_number: convert_bank_account_to_dict(account) for account_number, account in bank_accounts.items()}, file, indent=4)


class Bank:

    def __init__(self, bank_accounts=None):
        self.bank_accounts = {} if bank_accounts is None else bank_accounts

    def open_account(self, card_holder):
        account = BankAccount(card_holder)
        self.bank_accounts[account.account_number] = account
        return account

    def add_money(self, account_number, money):
        self.bank_accounts[account_number].money += money

    def transfer_money(self, from_account_number, to_account_number, money):
        self.bank_accounts[from_account_number].money -= money
        self.bank_accounts[to_account_number].money += money

    def external_transfer(self, from_account_number, to_external_number, money):
        self.bank_accounts[from_account_number].money -= money
        print(f'Банк перевёл {money} $ с вашего счёта {from_account_number} на внешний счёт {to_external_number}')

    def all_accounts(self):
        print('Ваши открытые счета:')
        for account_number, account in self.bank_accounts.items():
            print(f'Cчёт: {account_number}')
            print(f' Остаток на счету: {account.money} $')
            print(f' Номер карты: {account.card_number}')
            print(f' Держатель карты: {account.card_holder}')


class Controller:

    def __init__(self, data_file_name=None):
        self.bank = Bank()
        self.data_file_name = 'data.json' if data_file_name is None else data_file_name
        self.bank.bank_accounts = load_accounts(self.data_file_name)

    def run(self):
        print('Здравствуйте, наш банк открылся!')
        while True:
            print("""Выберите действие:
           0. Завершить программу
           1. Открыть новый счёт
           2. Просмотреть открытые счета
           3. Положить деньги на счёт
           4. Перевести деньги между счетами
           5. Совершить платёж""")
            user_input = input()

            if not user_input.isdigit():
                print('Неправильный ввод')
                continue
            else:
                user_input = int(user_input)
                match user_input:
                    case 0:
                        print('До свидания!')
                        save_accounts(self.data_file_name, self.bank.bank_accounts)
                        break
                    case 1:
                        user_name = input('ведите имя и фамилию держателя карты (на английском): ')
                        new_account = self.bank.open_account(user_name)
                        print(f'"Счёт {new_account.account_number} создан"')
                    case 2:
                        self.bank.all_accounts()
                    case 3:
                        account_number = input('Введите номер cчёта:  ')
                        money = int(input('Количество денег: '))
                        self.bank.add_money(account_number, money)
                    case 4:
                        from_account = input('Введите номер cчёта-отправителя: ')
                        recipient_account = input('Введите номер cчёта-получателя: ')
                        money = int(input('Количество денег: '))
                        self.bank.transfer_money(from_account, recipient_account, money)
                    case 5:
                        from_account = input('Введите номер cчёта-отправителя: ')
                        external_user = input('Введите номер счёта внешнего получателя: ')
                        money = int(input('Количество денег: '))
                        self.bank.external_transfer(from_account, external_user, money)



if __name__ == '__main__':
    controller = Controller(data_file_name='data.json')
    controller.run()
