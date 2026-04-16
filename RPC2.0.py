import random
import time
import os

# ASCII Art for the choices
HAND_SIGNS = {
    "stone": """
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """,
    "paper": """
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """,
    "scissors": """
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """
}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def cyber_rps():
    player_hp = 3
    cpu_hp = 3
    options = ["stone", "paper", "scissors"]
    
    print(" ⚡ WELCOME TO THE BINARY GAMBIT ⚡ ")
    print("-----------------------------------")
    print("System: Defeat the AI to bypass the firewall.")
    print("Rules: Best of 3 HP. Win a round to deal 1 damage.")
    
    while player_hp > 0 and cpu_hp > 0:
        print(f"\n[PLAYER HP: {'❤️' * player_hp}] | [CPU HP: {'⚡' * cpu_hp}]")
        user_choice = input("Choose (Stone, Paper, Scissors) or 'Q' to abort: ").lower()

        if user_choice == 'q':
            print("System: Connection terminated.")
            break
        
        if user_choice not in options:
            print("❌ Invalid Data Input. Try again.")
            continue

        cpu_choice = random.choice(options)

        # "Suspense" animation
        print("\nCalculating probability...")
        for _ in range(3):
            print(".", end="", flush=True)
            time.sleep(0.4)
        print("\n")

        print(f"YOU chose:{HAND_SIGNS[user_choice]}")
        print(f"CPU chose:{HAND_SIGNS[cpu_choice]}")

        # Logic
        if user_choice == cpu_choice:
            print(">> RESULT: NEURAL LINK SYNCHRONIZED (Tie)")
        elif (user_choice == "stone" and cpu_choice == "scissors") or \
             (user_choice == "paper" and cpu_choice == "stone") or \
             (user_choice == "scissors" and cpu_choice == "paper"):
            print(">> RESULT: SYSTEM OVERRIDE SUCCESSFUL (You Win)")
            cpu_hp -= 1
        else:
            # The "Glitch" Mechanic: 15% chance to ignore damage
            glitch = random.random() < 0.15
            if glitch:
                print(">> ERROR: QUANTUM GLITCH DETECTED! Damage mitigated.")
            else:
                print(">> RESULT: FIREWALL BREACH DETECTED (CPU Wins)")
                player_hp -= 1

    # Endgame
    print("\n" + "="*30)
    if player_hp > 0 and cpu_hp == 0:
        print("CONGRATULATIONS: You have successfully breached the mainframe.")
    elif cpu_hp > 0 and player_hp == 0:
        print("SYSTEM FAILURE: You have been disconnected.")
    print("="*30)

if __name__ == "__main__":
    cyber_rps()