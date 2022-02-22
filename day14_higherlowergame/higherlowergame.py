import art
import random
import game_data
import os


def clear():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def get_random_data():
    return random.choice(game_data.data)


def compare_followers(user_choice, account_a, account_b):
    account_a_followers = account_a['follower_count']
    account_b_followers = account_b['follower_count']

    if account_a_followers > account_b_followers:
        return user_choice == 'a'
    else:
        return user_choice == 'b'


def game():
    print(art.logo)
    score = 0
    game_still_on = True
    account_a = get_random_data()
    account_b = get_random_data()

    while game_still_on:
        account_a = account_b
        account_b = get_random_data()

        print(f"compare A: {account_a['name']}, a {account_a['description']}, from {account_a['country']}")
        print(art.vs)
        print(f"compare B: {account_b['name']}, a {account_b['description']}, from {account_b['country']}")
        user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
        is_correct = compare_followers(user_choice, account_a, account_b)

        clear()
        print(art.logo)

        if is_correct:
            score += 1
            print(f"You are right! Current score: {score}")
        else:
            game_still_on = False
            print(f"Sorry, that's wrong. Final score: {score}")


game()