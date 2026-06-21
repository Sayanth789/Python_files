import json
import logging

# Logging setup
logging.basicConfig(
    filename="bank.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

# Load users
with open("users.json", "r") as file:
    users = json.load(file)


def save_users():
    with open("users.json", "w") as file:
        json.dump(users, file, indent=4)


def deposit(user_id, amount):
    user_id = str(user_id)

    if user_id not in users:
        logging.error(f"Deposit failed - User {user_id} not found")
        return

    users[user_id]["balance"] += amount
    logging.info(f"{users[user_id]['name']} deposited {amount}")
    save_users()


def withdraw(user_id, amount):
    user_id = str(user_id)

    if user_id not in users:
        logging.error(f"Withdraw failed - User {user_id} not found")
        return

    if users[user_id]["balance"] < amount:
        logging.warning(f"{users[user_id]['name']} attempted overdraft: {amount}")
        return

    users[user_id]["balance"] -= amount
    logging.info(f"{users[user_id]['name']} withdrew {amount}")
    save_users()


def transfer(from_id, to_id, amount):
    from_id = str(from_id)
    to_id = str(to_id)

    if from_id not in users or to_id not in users:
        logging.error("Transfer failed - invalid user")
        return

    if users[from_id]["balance"] < amount:
        logging.warning(f"Transfer failed - insufficient funds from {from_id}")
        return

    users[from_id]["balance"] -= amount
    users[to_id]["balance"] += amount

    logging.info(
        f"{users[from_id]['name']} transferred {amount} to {users[to_id]['name']}"
    )

    save_users()


# ---------------- DEMO OPERATIONS ----------------

deposit(101, 1000)
withdraw(102, 500)
withdraw(102, 5000)      # overdraft case
transfer(101, 103, 1500)
transfer(999, 103, 1000) # invalid user
