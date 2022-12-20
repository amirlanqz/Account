
class Account:

	def __init__(self, name, balance):
		self.name = name
		self.balance = balance
		self.history = []

	def deposit(self, amount):
		self.balance += amount
		self.show_balance()
		self.history.append(amount)

	def withdraw(self, amount):
		if self.balance > amount:
			self.balance -= amount
			print(f'You spend {amount} units')
			self.show_balance()
			self.history.append(-amount)
		else:
			print('Not enough money')
			self.show_balance()

	def show_balance(self):
		print(f'Your balance:{self.balance}')

	def show_history(self):
		for amount in self.history:
			if amount > 0:
				transaction = 'deposited'
			else:
				transaction = 'withdraw'
			print(f'{transaction}\n{amount}')


a = Account('Amirlan', 100)
a.deposit(150)
a.withdraw(50)
a.show_history()

