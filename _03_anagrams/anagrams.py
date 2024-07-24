"""
Create an anagram game!
"""
import random
import tkinter as tk

# TODO Use this dictionary of anagrams to create an anagrams GUI word game.
#  Look at 'anagrams_game_example.png' in this folder for an example.

word_anagrams = {
    "action": ["cation"],
    "agree": ["eager"],
    "calm": ["clam"],
    "charming": ["marching"],
    "clean": ["lance"],
    "cool": ["loco"],
    "creative": ["reactive"],
    "delight": ["lighted"],
    "earnest": ["eastern", "nearest"],
    "easy": ["ayes", "yeas"],
    "free": ["reef"],
    "great": ["grate"],
    "green": ["genre"],
    "grin": ["ring"],
    "hearty": ["earthy"],
    "idea": ["aide"],
    "ideal": ["ailed"],
    "keen": ["knee"],
    "lively": ["evilly", "vilely"],
    "lovely": ["volley"],
    "merit": ["miter", "remit", "timer"],
    "open": ["nope", "peon", "pone"],
    "prepared": ["dapperer"],
    "quiet": ["quite"],
    "refined": ["definer"],
    "restored": ["resorted", "rostered"],
    "reward": ["drawer", "redraw", "warder", "warred"],
    "rewarding": ["redrawing", "wardering"],
    "right": ["girth"],
    "secure": ["rescue"],
    "simple": ["impels"],
    "smile": ["limes", "miles", "slime"],
    "super": ["puers", "purse"],
    "tops": ["opts", "post", "pots", "spot", "stop"],
    "unreal": ["neural"],
    "wonderful": ["underflow"],
    "zeal": ["laze"]}


class Anagrams(tk.Tk):

    def __init__(self):

        super().__init__()

        self.guesses = 5

        self.label3 = tk.Label(self, text="", fg='black', font=('courier new', 16, 'bold'))

        self.label3.place(relx=.3, rely=.8, relwidth=.5, relheight=.1)

        self.input_entry = tk.Entry(self, fg='black', font=('courier new', 16, 'bold'), relief='solid')

        self.input_entry.place(relx=0.4, rely=0.35, relwidth=0.47, relheight=0.2)

        self.input_entry.bind('<KeyRelease>', self.on_key_release)

        self.button = tk.Button(self, text='Get New Word!', fg='black', font=('courier new', 16, 'bold'))

        self.button.place(relx=0.73, rely=0.1, relwidth=0.25, relheight=0.1)

        self.button.bind('<ButtonPress>', self.on_button_press)

        self.button2 = tk.Button(self, text='Submit', fg='black', font=('courier new', 16, 'bold'))

        self.button2.place(relx=0.88, rely=0.4, relwidth=0.08, relheight=0.1)

        self.button2.bind('<ButtonPress>', self.on_button2_press)

        self.label = tk.Label(self, text="Guess the anagram for the word:", fg='black', font=('courier new', 16, 'bold'))

        self.label.place(relx=.001, rely=.1, relwidth=.5, relheight=.1)

        self.label4 = tk.Label(self, text='test', fg='black', font=('courier new', 16, 'bold'))

        self.label4.place(relx=.51, rely=.1, relwidth=.13, relheight=.1)

        self.label4.bind('<ButtonPress>', self.on_button_press)

        self.label2 = tk.Label(self, text="Guesses remaining: " + str(self.guesses), fg='black', font=('courier new', 16, 'bold'))

        self.label2.place(relx=.001, rely=.4, relwidth=.38, relheight=.1)

    def on_button_press(self, event):
        self.label4.configure(text=str(word_anagrams.keys()))

    def on_button2_press(self, event):
        for key, value in word_anagrams.items():
            val = word_anagrams[key]
            if self.label3 == val:
                print("correct")
            else:
                self.guesses -= 1
                self.label2.configure(text="Guesses remaining: " + str(self.guesses))
                if self.guesses == 0:
                    exit()

    def on_key_release(self, event):
        label_text = self.input_entry.get()
        self.label3.config(text=label_text)


if __name__ == '__main__':

    anagram = Anagrams()

    anagram.geometry('750x150')

    anagram.mainloop()
