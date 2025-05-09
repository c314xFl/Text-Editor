class Text_Editor:
    def __init__(self):
        global time, os, sys, textwrap, json, Path, Counter, string
        import time, os, sys, textwrap, json, string
        from pathlib import Path
        from collections import Counter

        # Customizeable Delay
        self.settings_file = "settings.json"
        default_settings = {"delay": 0.000314}

        if os.path.exists(self.settings_file):
            with open(self.settings_file, "r") as f:
                settings = json.load(f)
        else:
            settings = default_settings
            with open(self.settings_file, "w") as f:
                json.dump(default_settings, f, indent=4)

        self.delay = settings.get("delay", default_settings["delay"])

        # Get file name, from local folder
        self.file_name = Path(__file__).name

    # Replace pass with passing_arguements
    def passing_arguements(self):
        (lambda: (self.printing_effect("\nNot yet implemented."), input("\nPress [Enter] to return to the menu"), self.transition_effect()))()

    # Printing animation
    def printing_effect(self, message):
        for char in message:
            print(char, end='', flush=True)
            time.sleep(self.delay)
        print(flush=True)
        time.sleep(self.delay)

    # PowerPoint presentation ah transition effect
    def transition_effect(self):
        (lambda: (time.sleep(self.delay), os.system('cls' if os.name == 'nt' else 'clear'), time.sleep(self.delay)))()

    # Used to replace multiple if yes or if no
    def verification(self, question, isTrue_message, isFalse_message):
        while True:
            user_input = input(f"{self.file_name} > {question}").strip().lower()
            if user_input in ['y', 'yes']:
                self.printing_effect(isTrue_message)
                time.sleep(self.delay)
                return True
            elif user_input in ['n', 'no']:
                (lambda: (self.printing_effect(isFalse_message), self.transition_effect()))()
                return False
            else:
                self.invalid_input("missing" if user_input == "" else "invalid")

    # For invalid or missing inputs
    def invalid_input(self, default_error="invalid"):
        erro_type = {
            "invalid": f"{self.file_name} > Invalid input. Please try again.",
            "missing": f"{self.file_name} > Missing input. Please try again."
        }
        (lambda: (self.printing_effect(erro_type[default_error]), input("\nPress [Enter] to return to the menu"), self.transition_effect()))()

    def logo(self):
        logo = textwrap.dedent("""
            88888888888                888         8888888888     888 d8b 888                                       
                888                    888         888            888 Y8P 888                                       
                888                    888         888            888     888                                       
                888   .d88b.  888  888 888888      8888888    .d88888 888 888888 .d88b.  888d888  88888b.  888  888 
                888  d8P  Y8b `Y8bd8P' 888         888       d88" 888 888 888   d88""88b 888P"    888 "88b 888  888 
                888  88888888   X88K   888         888       888  888 888 888   888  888 888      888  888 888  888 
                888  Y8b.     .d8""8b. Y88b.       888       Y88b 888 888 Y88b. Y88..88P 888  d8b 888 d88P Y88b 888 
                888   "Y8888  888  888  "Y888      8888888888 "Y88888 888  "Y888 "Y88P"  888  Y8P 88888P"   "Y88888 
                                                                                                  888           888 
                                                                                                  888      Y8b d88P 
                                                                                                  888       "Y88P"  

                                                                                                   version 1.23.456
            """)
        (lambda: (self.printing_effect(logo), time.sleep(2.718) ,self.transition_effect()))()

    def main_program(self):
        logofx = 84
        sinofpi = "=" * logofx
        menu = textwrap.dedent(f"""
            88888888888                888         8888888888     888 d8b 888                    
                888                    888         888            888 Y8P 888                    
                888                    888         888            888     888                    
                888   .d88b.  888  888 888888      8888888    .d88888 888 888888 .d88b.  888d888 
                888  d8P  Y8b `Y8bd8P' 888         888       d88" 888 888 888   d88""88b 888P"   
                888  88888888   X88K   888         888       888  888 888 888   888  888 888     
                888  Y8b.     .d8""8b. Y88b.       888       Y88b 888 888 Y88b. Y88..88P 888     
                888   "Y8888  888  888  "Y888      8888888888 "Y88888 888  "Y888 "Y88P"  888     
            
            {sinofpi.rjust(logofx)}

            {"[ 1 ] Text Analyser   ".center(logofx)}
            {"[ 2 ] Text Modifier   ".center(logofx)}
            {"[ 3 ] Settings        ".center(logofx)}
            {"[ 4 ] Exit            ".center(logofx)}

            {sinofpi.rjust(logofx)}
            """)
        return menu

    def user_input(self):
        while True:
            menus = self.main_program()
            self.printing_effect(menus)
            cmds = {
                '1': self.text_analyser,
                '2': self.text_modifier,
                '3': self.settings,
                '4': self.exit
            }
            self.printing_effect(f"{self.file_name} > Choose an option between [ 1 ] and [ 5 ]")
            user_request = input(f"{self.file_name} > ").strip().lower()
            if user_request in cmds:
                self.transition_effect()
                cmds[user_request]()
            elif not user_request:
                self.invalid_input("missing")
            else:
                self.invalid_input("invalid")

    def text_analyser(self):
        while True:
            logarithm = 112
            exponents = "=" * logarithm
            analyser = textwrap.dedent(f"""
                    88888888888                888                d8888                   888                                    
                        888                    888               d88888                   888                                    
                        888                    888              d88P888                   888                                    
                        888   .d88b.  888  888 888888          d88P 888 88888b.   8888b.  888 888  888 .d8888b   .d88b.  888d888 
                        888  d8P  Y8b `Y8bd8P' 888            d88P  888 888 "88b     "88b 888 888  888 88K      d8P  Y8b 888P"   
                        888  88888888   X88K   888           d88P   888 888  888 .d888888 888 888  888 "Y8888b. 88888888 888     
                        888  Y8b.     .d8""8b. Y88b.        d8888888888 888  888 888  888 888 Y88b 888      X88 Y8b.     888     
                        888   "Y8888  888  888  "Y888      d88P     888 888  888 "Y888888 888  "Y88888  88888P'  "Y8888  888     
                                                                                                   888                           
                                                                                              Y8b d88P                           
                                                                                              "Y88P"     

                {exponents.rjust(logarithm)}

                {"[ 1 ] Alphabet Counter   ".center(logarithm)}
                {"[ 2 ] Word Counter       ".center(logarithm)}
                {"[ 3 ] Return to main menu".center(logarithm)}

                {exponents.rjust(logarithm)}
                """)
            display = [
                f"{analyser}",
                f"{self.file_name} > Choose an option between [ 1 ] and [ 3 ]"
            ]
            self.printing_effect("\n".join(display))
            user_input = input(f"{self.file_name} > ").strip().lower()
            if user_input == '1':
                alphabet_counter = input(f"{self.file_name} > Enter text: ")
                alphabets = [char for char in alphabet_counter if char.isalpha()]
                alphabet_count = Counter(alphabets)
                self.printing_effect("\nAlphabet Frequencies:\n")
                for letter, count in sorted(alphabet_count.items(), key=lambda x: (x[0].lower(), not x[0].isupper())):
                    self.printing_effect(f"'{letter}': {count}")
                (lambda: (input("\nPress [Enter] to return to the menu"), self.transition_effect()))()
            elif user_input == '2':
                word_counter = input(f"{self.file_name} > Enter text: ").strip()
                words = word_counter.split()
                counter = {}
                for word in words:
                    if word in counter:
                        counter[word] += 1
                    else:
                        counter[word] = 1
                self.printing_effect("\nWord Frequencies:\n")
                for word, count in counter.items():
                    self.printing_effect(f"'{word}': {count}")
                (lambda: (input("\nPress [Enter] to return to the menu"), self.transition_effect()))()
            elif user_input == '3':
                self.transition_effect()
                question = "Are you sure you want to return to the main menu? (Y/N): "
                isTrue_message = "Returning to main menu..."
                isFalse_message = "Returning to text analyser..."
                if self.verification(question, isTrue_message, isFalse_message):
                    self.transition_effect()
                    break

            elif not user_input:
                self.invalid_input("missing")
            else:
                self.invalid_input("invalid")

    def text_modifier(self):
        while True:
            length = 102
            wall = "=" * length
            modifier = textwrap.dedent(f"""
                88888888888                888         888b     d888               888 d8b  .d888 d8b                  
                    888                    888         8888b   d8888               888 Y8P d88P"  Y8P                  
                    888                    888         88888b.d88888               888     888                         
                    888   .d88b.  888  888 888888      888Y88888P888  .d88b.   .d88888 888 888888 888  .d88b.  888d888 
                    888  d8P  Y8b `Y8bd8P' 888         888 Y888P 888 d88""88b d88" 888 888 888    888 d8P  Y8b 888P"   
                    888  88888888   X88K   888         888  Y8P  888 888  888 888  888 888 888    888 88888888 888     
                    888  Y8b.     .d8""8b. Y88b.       888   "   888 Y88..88P Y88b 888 888 888    888 Y8b.     888     
                    888   "Y8888  888  888  "Y888      888       888  "Y88P"   "Y88888 888 888    888  "Y8888  888    

                {wall.rjust(length)}

                {"[ 1 ] Uppercase all words                 ".center(length)}
                {"[ 2 ] Lowercase all words                 ".center(length)}
                {"[ 3 ] Capitalise first letter of each word".center(length)}
                {"[ 4 ] Convert letters to numebrs          ".center(length)}
                {"[ 5 ] Return to main menu                 ".center(length)}

                {wall.rjust(length)}
                """)
            display = [
                f"{modifier}",
                f"{self.file_name} > Choose an option between [ 1 ] and [ 5 ]"
            ]
            self.printing_effect("\n".join(display))
            user_input = input(f"{self.file_name} > ").strip().lower()
            if user_input == '1':
                text = input(f"{self.file_name} > Enter text: ")
                self.printing_effect("\nUppercased text:\n")
                self.printing_effect(text.upper())
                (lambda: (input("\nPress [Enter] to return to the menu"), self.transition_effect()))()
            elif user_input == '2':
                text = input(f"{self.file_name} > Enter text: ")
                self.printing_effect("\nLowercased text:\n")
                self.printing_effect(text.lower())
                (lambda: (input("\nPress [Enter] to return to the menu"), self.transition_effect()))()
            elif user_input == '3':
                text = input(f"{self.file_name} > Enter text: ")
                self.printing_effect("\nCapitalised text:\n")
                self.printing_effect(text.title())
                (lambda: (input("\nPress [Enter] to return to the menu"), self.transition_effect()))()
            elif user_input == '4':
                text = input(f"{self.file_name} > Enter text: ")
                self.printing_effect("\n\nI. Original input:\n")
                self.printing_effect(text)

                word_number_groups = [
                    [ord(char.lower()) - ord('a') + 1 for char in word if char.isalpha()]
                    for word in text.split()
                ]
                self.printing_effect("\n\nII. Final input (as numbers grouped by word):\n")
                self.printing_effect(str(word_number_groups)[1:-1])

                clarified = []
                for word in text.split():
                    clarified_word = " ".join(
                        f"{char.upper()}({ord(char.lower()) - ord('a') + 1})"
                        for char in word if char.isalpha()
                    )
                    clarified.append(f"[{clarified_word}]")
                self.printing_effect("\n\nIII. Final input with clarity:\n")
                self.printing_effect(", ".join(clarified))

                (lambda: (input("\n\nPress [Enter] to return to the menu"), self.transition_effect()))()
            elif user_input == '5':
                self.transition_effect()
                question = "Are you sure you want to return to the main menu? (Y/N): "
                isTrue_message = "Returning to main menu..."
                isFalse_message = "Returning to text modifier..."
                if self.verification(question, isTrue_message, isFalse_message):
                    self.transition_effect()
                    break

            elif not user_input:
                self.invalid_input("missing")
            else:
                self.invalid_input("invalid")

    def settings(self):
        while True:
            length = 64
            barrier = "=" * length
            settings = textwrap.dedent(f"""
                 .d8888b.           888    888    d8b                            
                d88P  Y88b          888    888    Y8P                            
                Y88b.               888    888                                   
                 "Y888b.    .d88b.  888888 888888 888 88888b.   .d88b.  .d8888b  
                    "Y88b. d8P  Y8b 888    888    888 888 "88b d88P"88b 88K      
                      "888 88888888 888    888    888 888  888 888  888 "Y8888b. 
                Y88b  d88P Y8b.     Y88b.  Y88b.  888 888  888 Y88b 888      X88 
                 "Y8888P"   "Y8888   "Y888  "Y888 888 888  888  "Y88888  88888P' 
                                                                    888          
                                                               Y8b d88P          
                                                                "Y88P"    

                {barrier.rjust(length)}

                {f"Current delay duration: {self.delay}".center(length)}

                {barrier.rjust(length)}

                {"[ 1 ] Change delay duration".center(length)}
                {"[ 2 ] Return to main menu  ".center(length)}

                {barrier.rjust(length)}
                """)
            display = [
                f"{settings}",
                f"{self.file_name} > Choose an option between [ 1 ] and [ 2 ]"
            ]
            self.printing_effect("\n".join(display))
            user_input = input(f"{self.file_name} > ").strip().lower()
            if user_input == '1':
                try:
                    new_delay = float(input(f"{self.file_name} > Enter a new delay duration: "))
                    if new_delay < 0:
                        raise ValueError
                    question = f"Are you sure you want to change the delay duration to {new_delay}? (Y/N): "
                    isTrue_message = f"Changing delay duration to {new_delay}..."
                    isFalse_message = "Returning to settings..."
                    if self.verification(question, isTrue_message, isFalse_message):
                        self.delay = new_delay
                        with open(self.settings_file, "w") as f:
                            json.dump({"delay": self.delay}, f, indent=4)
                        self.printing_effect(f"New delay saved as {self.delay} seconds.")
                        self.transition_effect()
                except ValueError:
                    self.invalid_input("invalid")

            elif user_input == '2':
                self.transition_effect()
                question = "Are you sure you want to return to the main menu? (Y/N): "
                isTrue_message = "Returning to main menu..."
                isFalse_message = "Returning to settings..."
                if self.verification(question, isTrue_message, isFalse_message):
                    self.transition_effect()
                    break

            elif not user_input:
                self.invalid_input("missing")
            else:
                self.invalid_input("invalid")

    def exit(self):
        question = "Are you sure you want to exit the program? (Y/N): "
        isTrue_message = f"Exiting {self.file_name}..."
        isFalse_message = "Returning to main menu..."
        if self.verification(question, isTrue_message, isFalse_message):
            sys.exit(0)

    def run(self):
        self.logo()
        while True:
            self.user_input()

if __name__ == "__main__":
    game = Text_Editor()
    game.run()