import random
import string
import time

WORDLIST_FILENAME = "words.txt"

# ---------------------------------------------------------
# Utility Functions

def load_words(filename: str) -> list[str]:
    """Load words from a file and return as a list."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            words = f.read().split()
        print(f"✅ Loaded {len(words)} words.")
        return words
    except FileNotFoundError:
        print(f"❌ {filename} file not found!")
        return []

def get_random_word(wordlist: list[str]) -> str:
    """Return a random word from the wordlist."""
    return random.choice(wordlist)

def fake_clear_screen():
    """Simulate clearing the screen for local multiplayer fairness."""
    print("\n" * 50)

# ---------------------------------------------------------
# Player Class

class Player:
    """Represents a player (Human or AI)."""

    def __init__(self, name: str, is_ai: bool = False):
        self.name = name
        self.score = 0
        self.is_ai = is_ai

    def __str__(self) -> str:
        role = "🤖 AI" if self.is_ai else "👤 Human"
        return f"{self.name} [{role}] - Total Score: {self.score}"

# ---------------------------------------------------------
# Hangman Game Class

class HangmanGame:
    """Main Hangman Game Logic."""

    MAX_GUESSES = 6
    MAX_WARNINGS = 3

    def __init__(self, session_wordlist: list[str], players: list[Player]):
        self.players = players
        self.wordlist = session_wordlist  # Filtered by length in main()

        if not self.wordlist:
            raise ValueError("❌ No words available for the selected length!")

    def display_word(self, word: str, guessed: list[str]) -> str:
        return " ".join([l if l in guessed else "_" for l in word])

    def available_letters(self, guessed: list[str]) -> str:
        return "".join([l for l in string.ascii_lowercase if l not in guessed])

    def ai_guess(self, guessed: list[str]) -> str:
        """Simple AI: picks a random unused letter."""
        available = [l for l in string.ascii_lowercase if l not in guessed]
        return random.choice(available)

    def play_turn(self, player: Player) -> None:
        # Each player gets a unique word of the SAME length chosen for the session
        word = get_random_word(self.wordlist)
        guesses = self.MAX_GUESSES
        warnings = self.MAX_WARNINGS
        guessed_letters: list[str] = []

        print(f"\n🎯 {player.name}'s Turn")
        print(f"Word Length: {len(word)}")
        print("-" * 40)

        while guesses > 0:
            print("\nWord:", self.display_word(word, guessed_letters))
            print(f"Guesses left: {guesses} | Warnings: {warnings}")
            print("Available:", self.available_letters(guessed_letters))

            if player.is_ai:
                guess = self.ai_guess(guessed_letters)
                print(f"🤖 {player.name} guesses: {guess}")
                time.sleep(1.5)
            else:
                guess = input("Enter a letter: ").lower().strip()

            # Validation
            if not (guess.isalpha() and len(guess) == 1):
                if warnings > 0:
                    warnings -= 1
                    print(f"⚠️ Invalid input! Warnings left: {warnings}")
                else:
                    guesses -= 1
                    print("❌ Invalid input! Lost 1 guess.")
                continue

            if guess in guessed_letters:
                if warnings > 0:
                    warnings -= 1
                    print(f"⚠️ Already guessed! Warnings left: {warnings}")
                else:
                    guesses -= 1
                    print("❌ Already guessed! Lost 1 guess.")
                continue

            guessed_letters.append(guess)

            # Scoring Logic
            if guess in word:
                print("✅ Correct guess!")
                player.score += 10
            else:
                print("❌ Wrong guess!")
                guesses -= 2 if guess in "aeiou" else 1

            # Win Check
            if all(l in guessed_letters for l in word):
                print(f"\n🎉 {player.name} guessed the word: {word}")
                player.score += (guesses * 5) # Bonus for remaining guesses
                return

            print("-" * 40)

        print(f"\n💀 {player.name} failed! The word was: {word}")

    def show_results(self) -> None:
        print("\n🏆 MATCH RESULTS")
        print("=" * 40)
        for p in self.players:
            print(p)

        max_score = max(p.score for p in self.players)
        winners = [p for p in self.players if p.score == max_score]

        if len(winners) == 1:
            print(f"\n🥇 Leader: {winners[0].name} ({max_score} points)")
        else:
            print(f"\n🤝 Tie at {max_score} points!")

    def play(self) -> None:
        print("\n🎮 Starting Hangman Match...")
        for i, player in enumerate(self.players):
            self.play_turn(player)

            if i < len(self.players) - 1:
                print("\n⏳ Next player's turn in 3 seconds...")
                time.sleep(3)
                fake_clear_screen()

        self.show_results()

# ---------------------------------------------------------
# MAIN FUNCTION

def main() -> None:
    all_words = load_words(WORDLIST_FILENAME)
    if not all_words:
        return

    # Setup Players (Only done once)
    while True:
        try:
            n = int(input("Enter number of players (1-10): "))
            if 1 <= n <= 10: break
            print("❌ Choose between 1 and 10.")
        except ValueError:
            print("❌ Invalid number.")

    players = []
    if n == 1:
        print("🎮 Single Player Mode: You vs AI")
        name = input("Enter your name: ").strip() or "Player_1"
        players.append(Player(name))
        players.append(Player("AI_Bot", is_ai=True))
    else:
        for i in range(n):
            name = input(f"Enter Player {i+1} name: ").strip() or f"Player_{i+1}"
            players.append(Player(name))

    # Main Game Loop
    while True:
        # Word length selection happens here so it's fresh each round
        while True:
            try:
                target_len = int(input("\n🔤 Enter desired word length for all players: "))
                filtered_words = [w for w in all_words if len(w) == target_len]
                if filtered_words:
                    break
                print(f"❌ No words of length {target_len} in dictionary.")
            except ValueError:
                print("❌ Enter a valid number.")

        try:
            game = HangmanGame(filtered_words, players)
            game.play()
        except Exception as e:
            print(f"An error occurred: {e}")
            break

        if input("\n🔁 Play another match? (y/n): ").lower() != 'y':
            print("👋 Thanks for playing!")
            break

if __name__ == "__main__":
    main()