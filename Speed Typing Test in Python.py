import time

def typing_speed_test():
    print("Welcome to the Typing Speed Test!")
    input("Press Enter when you are ready to start...")

    start_time = time.time()

    text = "The quick brown fox jumps over the lazy dog."
    print("Type the following text:")
    print(text)

    user_input = input()

    end_time = time.time()
    elapsed_time = end_time - start_time

    correct_chars = sum(1 for i, j in zip(text, user_input) if i == j)
    accuracy = (correct_chars / len(text)) * 100
    words_per_minute = (len(user_input.split()) / elapsed_time) * 60

    print("\nTyping speed test result:")
    print("Time elapsed:", round(elapsed_time, 2), "seconds")
    print("Accuracy:", round(accuracy, 2), "%")
    print("Words per minute:", round(words_per_minute))

if __name__ == "__main__":
    typing_speed_test()
