import emoji

print("Emojis disponíveis:")
print("❤️ - :red_heart:")
print("💙 - :blue_heart:")
print("🦊 - :fox:")
print("🏆 - :trophy:")
print("👍 - :thumbs_up:")
print("🤔 - :thinking_face:")
print("🥳 - :partying_face:")

frase = input("Digite uma frase e ela será emojizada:")

frase_emojizada = emoji.emojize(frase, language='alias')

print("Frase emojizada:")
print(frase_emojizada)