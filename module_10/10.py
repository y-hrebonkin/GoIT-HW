from collections import UserList


class AmountPaymentList(UserList):
    def amount_payment(self):
        total = 0
        for value in self.data:
            if value > 0:
                total += value
        return total


payment = AmountPaymentList([1, -3, 4])
print(payment.amount_payment())  # 5

#  У цьому прикладі ми створили клас AmountPaymentList, 
# який успадковує клас UserList. В класі AmountPaymentList
# ми додали метод amount_payment(), який обчислює суму платежів
# зі списку self.data, ігноруючи від'ємні значення.
# При створенні екземпляру payment ми передали список 
# платежів як аргумент. Потім ми можемо викликати метод 
# amount_payment() на цьому екземплярі, щоб отримати суму позитивних платежів.