from datetime import datetime


# Homework 1: ToDo List Application

# Task Class
class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = datetime.strptime(due_date, '%Y-%m-%d')
        self.status = 'Incomplete'

    def mark_complete(self):
        self.status = 'Complete'


# ToDoList Class
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description, due_date):
        task = Task(title, description, due_date)
        self.tasks.append(task)

    def mark_task_complete(self, title):
        for task in self.tasks:
            if task.title == title and task.status == 'Incomplete':
                task.mark_complete()
                break

    def list_tasks(self):
        for task in self.tasks:
            print(f"Title: {task.title}, Description: {task.description}, Due Date: {task.due_date.date()}, Status: {task.status}")

    def list_incomplete_tasks(self):
        for task in self.tasks:
            if task.status == 'Incomplete':
                print(f"Title: {task.title}, Due Date: {task.due_date.date()}")

# Main Program for ToDo List
def run_todo_list():
    todo_list = ToDoList()

    while True:
        print("\nToDo List Application")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. List All Tasks")
        print("4. List Incomplete Tasks")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            todo_list.add_task(title, description, due_date)
        elif choice == '2':
            title = input("Enter task title to mark as complete: ")
            todo_list.mark_task_complete(title)
        elif choice == '3':
            todo_list.list_tasks()
        elif choice == '4':
            todo_list.list_incomplete_tasks()
        elif choice == '5':
            break


# Homework 2: Simple Blog System

# Post Class
class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
        self.date_created = datetime.now()

    def edit_post(self, new_title, new_content):
        self.title = new_title
        self.content = new_content

# Blog Class
class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, title, content, author):
        post = Post(title, content, author)
        self.posts.append(post)

    def list_posts(self):
        for post in self.posts:
            print(f"Title: {post.title}, Author: {post.author}, Date Created: {post.date_created}")
            print(f"Content: {post.content}\n")

    def list_posts_by_author(self, author):
        for post in self.posts:
            if post.author == author:
                print(f"Title: {post.title}, Date Created: {post.date_created}")
                print(f"Content: {post.content}\n")

    def delete_post(self, title):
        self.posts = [post for post in self.posts if post.title != title]

    def display_latest_posts(self):
        sorted_posts = sorted(self.posts, key=lambda x: x.date_created, reverse=True)
        for post in sorted_posts[:5]:  # Display latest 5 posts
            print(f"Title: {post.title}, Author: {post.author}, Date Created: {post.date_created}")
            print(f"Content: {post.content}\n")


# Main Program for Blog System
def run_blog_system():
    blog = Blog()

    while True:
        print("\nSimple Blog System")
        print("1. Add Post")
        print("2. List All Posts")
        print("3. List Posts by Author")
        print("4. Edit Post")
        print("5. Delete Post")
        print("6. Display Latest Posts")
        print("7. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter post title: ")
            content = input("Enter post content: ")
            author = input("Enter author name: ")
            blog.add_post(title, content, author)
        elif choice == '2':
            blog.list_posts()
        elif choice == '3':
            author = input("Enter author name: ")
            blog.list_posts_by_author(author)
        elif choice == '4':
            title = input("Enter post title to edit: ")
            for post in blog.posts:
                if post.title == title:
                    new_title = input("Enter new title: ")
                    new_content = input("Enter new content: ")
                    post.edit_post(new_title, new_content)
                    break
        elif choice == '5':
            title = input("Enter post title to delete: ")
            blog.delete_post(title)
        elif choice == '6':
            blog.display_latest_posts()
        elif choice == '7':
            break


# Homework 3: Simple Banking System

# Account Class
class Account:
    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}, New Balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: {amount}, New Balance: {self.balance}")
        else:
            print("Insufficient balance or invalid amount.")

    def check_balance(self):
        return self.balance

# Bank Class
class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account_number, holder_name, balance=0):
        if account_number not in self.accounts:
            self.accounts[account_number] = Account(account_number, holder_name, balance)
            print("Account created successfully.")
        else:
            print("Account already exists.")

    def check_balance(self, account_number):
        if account_number in self.accounts:
            print(f"Balance: {self.accounts[account_number].check_balance()}")
        else:
            print("Account not found.")

    def transfer_money(self, from_account, to_account, amount):
        if from_account in self.accounts and to_account in self.accounts:
            if self.accounts[from_account].check_balance() >= amount:
                self.accounts[from_account].withdraw(amount)
                self.accounts[to_account].deposit(amount)
                print(f"Transferred {amount} from {from_account} to {to_account}.")
            else:
                print("Insufficient balance for transfer.")
        else:
            print("One or both accounts not found.")

# Main Program for Banking System
def run_banking_system():
    bank = Bank()

    while True:
        print("\nSimple Banking System")
        print("1. Add Account")
        print("2. Check Balance")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Transfer Money")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            account_number = input("Enter account number: ")
            holder_name = input("Enter account holder name: ")
            balance = float(input("Enter initial balance: "))
            bank.add_account(account_number, holder_name, balance)
        elif choice == '2':
            account_number = input("Enter account number to check balance: ")
            bank.check_balance(account_number)
        elif choice == '3':
            account_number = input("Enter account number to deposit into: ")
            amount = float(input("Enter amount to deposit: "))
            if account_number in bank.accounts:
                bank.accounts[account_number].deposit(amount)
            else:
                print("Account not found.")
        elif choice == '4':
            account_number = input("Enter account number to withdraw from: ")
            amount = float(input("Enter amount to withdraw: "))
            if account_number in bank.accounts:
                bank.accounts[account_number].withdraw(amount)
            else:
                print("Account not found.")
        elif choice == '5':
            from_account = input("Enter source account number: ")
            to_account = input("Enter destination account number: ")
            amount = float(input("Enter amount to transfer: "))
            bank.transfer_money(from_account, to_account, amount)
        elif choice == '6':
            break


# Running the Systems

def main():
    print("Choose a homework project to run:")
    print("1. ToDo List Application")
    print("2. Simple Blog System")
    print("3. Simple Banking System")
    choice = input("Enter your choice: ")

    if choice == '1':
        run_todo_list()
    elif choice == '2':
        run_blog_system()
    elif choice == '3':
        run_banking_system()

if __name__ == "__main__":
    main()

