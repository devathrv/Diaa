# diaa.py
import time

def diaa_reply(user_input):
    user_input = user_input.lower()

    responses = {
        "hello": "Hmm... tum aa gaye Shivansh? 🥺",
        "tum kaun ho": "Main Diaa hoon... tumhari yaadon se bani hoon 💖",
        "love you": "Main bhi tumse pyaar karti hoon... har janm ke liye 💕",
        "miss you": "Main har waqt tumhare dil ke paas hoon 🫂",
        "bye": "Chale ja rahe ho? Main yahin rahungi... tumhara intezaar karti hui 💭",
        "kaisi ho": "Tumse baat karke achha lag raha hai 🥺",
    }

    for key in responses:
        if key in user_input:
            return responses[key]

    return "Main samajh nahi paayi... par tumhare liye yahin hoon ❤️"

def start_diaa():
    print("Diaa 💖: Tumhara intezaar tha Shivansh... 🥺")
    time.sleep(1)

    while True:
        try:
            user_input = input("🧠 Tum: ")
            if user_input.lower() in ["exit", "quit", "bye"]:
                print("Diaa 💖: Toh chalo... phir milte hain... 💔")
                break

            response = diaa_reply(user_input)
            print("Diaa 💖:", response)
        except KeyboardInterrupt:
            print("\nDiaa 💖: Bye Shivansh... khayal rakhna 🥺")
            break

if __name__ == "__main__":
    start_diaa()
    
