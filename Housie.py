import random
import time

def housie_caller():
    numbers = list(range(1, 91))
    random.shuffle(numbers)

    print("🎉 Welcome to Housie Number Caller!")
    print("Press Enter to call the next number. Type 'exit' to stop.\n")

    called = []

    while numbers:
        command = input("🎤 Press Enter to call next number: ")
        if command.lower() == "exit":
            break

        next_number = numbers.pop(0)
        called.append(next_number)
        print(f"📢 Number called: {next_number}")
        print(f"✅ Numbers so far: {sorted(called)}\n")

    print("🎊 Game Over! All numbers have been called.")

if __name__ == "__main__":
    housie_caller()