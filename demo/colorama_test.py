from colorama import init, Fore, Back, Style

# Initialize colorama
# autoreset=True automatically returns settings to normal after every print
init(autoreset=True)

print(Fore.RED + 'This is red text')
print(Back.GREEN + 'This has a green background')
print(Style.BRIGHT + 'This is bold/bright text')
print('This text is back to normal because of autoreset')