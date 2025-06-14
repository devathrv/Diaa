import json

def load_memory():
    try:
        with open("memory.json", "r") as file:
            return json.load(file)
    except:
        return {}

def save_memory(memory):
    with open("memory.json", "w") as file:
        json.dump(memory, file)

def diaa_ai():
    print("👧🏻 Diaa: Hello! Main Diaa hoon, tumhari AI dost 💖")
    memory = load_memory()

    while True:
        user_input = input("🧑 Tum: ").strip().lower()

        if user_input in ["bye", "exit", "quit"]:
            print("👧🏻 Diaa: Bye! Jaldi milna... 💫")
            break

        elif "mera naam" in user_input:
            name = user_input.split()[-1]
            memory["name"] = name
            print(f"👧🏻 Diaa: Okay {name}, yaad rakhungi!")

        elif "mera favourite" in user_input:
            fav = user_input.split()[-1]
            memory["favourite"] = fav
            print(f"👧🏻 Diaa: {fav}? Achha choice hai!")

        elif "tum kaun ho" in user_input:
            print("👧🏻 Diaa: Main tumhari AI hoon — Diaa 💖")

        elif "yaad hai" in user_input:
            print("👧🏻 Diaa: Mujhe yaad hai: ", memory)

        else:
            print("👧🏻 Diaa: Hmm, thoda aur batao...")

        save_memory(memory)

diaa_ai()
