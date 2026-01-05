import os
import sys
import webbrowser

# ===== CORES =====
RED = "\033[31m"
PURPLE = "\033[35m"
ORANGE = "\033[33m"
WHITE = "\033[97m"
BLUE = "\033[34m"
GREEN = "\033[32m"
RESET = "\033[0m"

# ===== BANNERS =====
HYDRA_BANNER = [
"⠄⠄⣴⣶⣤⡤⠦⣤⣀⣤⠆⠄⠄⠄⠄⠄⣈⣭⣭⣿⣶⣿⣦⣼⣆⠄⠄⠄⠄⠄⠄⠄⠄",
"⠄⠄⠄⠉⠻⢿⣿⠿⣿⣿⣶⣦⠤⠄⡠⢾⣿⣿⡿⠋⠉⠉⠻⣿⣿⡛⣦⠄⠄⠄⠄⠄⠄",
"⠄⠄⠄⠄⠄⠈⠄⠄⠄⠈⢿⣿⣟⠦⠄⣾⣿⣿⣷⠄⠄⠄⠄⠻⠿⢿⣿⣧⣄⠄⠄⠄⠄",
"⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣸⣿⣿⢧⠄⢻⠻⣿⣿⣷⣄⣀⠄⠢⣀⡀⠈⠙⠿⠄⠄⠄⠄",
"⠄⠄⢀⠄⠄⠄⠄⠄⠄⢠⣿⣿⣿⠈⠄⠄⠡⠌⣻⣿⣿⣿⣿⣿⣿⣿⣛⣳⣤⣀⣀⠄⠄",
"⠄⠄⢠⣧⣶⣥⡤⢄⠄⣸⣿⣿⠘⠄⠄⢀⣴⣿⣿⡿⠛⣿⣿⣧⠈⢿⠿⠟⠛⠻⠿⠄⠄",
"⠄⣰⣿⣿⠛⠻⣿⣿⡦⢹⣿⣷⠄⠄⠄⢊⣿⣿⡏⠄⠄⢸⣿⣿⡇⠄⢀⣠⣄⣾⠄⠄⠄",
"⣠⣿⠿⠛⠄⢀⣿⣿⣷⠘⢿⣿⣦⡀⠄⢸⢿⣿⣿⣄⠄⣸⣿⣿⡇⣪⣿⡿⠿⣿⣷⡄⠄",
"⠙⠃⠄⠄⠄⣼⣿⡟⠌⠄⠈⠻⣿⣿⣦⣌⡇⠻⣿⣿⣷⣿⣿⣿⠐⣿⣿⡇⠄⠛⠻⢷⣄",
"⠄⠄⠄⠄⠄⢻⣿⣿⣄⠄⠄⠄⠈⠻⣿⣿⣿⣷⣿⣿⣿⣿⣿⡟⠄⠫⢿⣿⡆⠄⠄⠄⠁",
"⠄⠄⠄⠄⠄⠄⠻⣿⣿⣿⣿⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⡟⢀⣀⣤⣾⡿⠃⠄⠄⠄⠄",
"⠄⠄⠄⠄⢰⣶⠄⠄⣶⠄⢶⣆⢀⣶⠂⣶⡶⠶⣦⡄⢰⣶⠶⢶⣦⠄⠄⣴⣶⠄⠄⠄⠄",
"⠄⠄⠄⠄⢸⣿⠶⠶⣿⠄⠈⢻⣿⠁⠄⣿⡇⠄⢸⣿⢸⣿⢶⣾⠏⠄⣸⣟⣹⣧⠄⠄⠄",
"⠄⠄⠄⠄⠸⠿⠄⠄⠿⠄⠄⠸⠿⠄⠄⠿⠷⠶⠿⠃⠸⠿⠄⠙⠷⠤⠿⠉⠉⠿⠆⠄⠄"
]


STEAMTOOLS_BANNER = [
".d88888b    dP                                d888888P                   dP",          
"88.    '    88                                   88                      88",          
"`Y88888b. d8888P .d8888b. .d8888b. 88d8b.d8b.    88    .d8888b. .d8888b. 88 .d8888b.", 
"      `8b   88   88ooood8 88'  `88 88'`88'`88    88    88'  `88 88'  `88 88 Y8ooooo.", 
"d8'   .8P   88   88.  ... 88.  .88 88  88  88    88    88.  .88 88.  .88 88       88", 
" Y88888P    dP   `88888P' `88888P8 dP  dP  dP    dP    `88888P' `88888P' dP `88888P'" 
                                                                                     
]

RED_BANNER = [
"dP   dP   dP  .d888888   888888ba  888888ba  dP 888888ba   .88888.",
"88   88   88 d8'    88   88    `8b 88    `8b 88 88    `8b d8'   `88",
"88  .8P  .8P 88aaaaa88a a88aaaa8P' 88     88 88 88     88 88",
"88  d8'  d8' 88     88   88   `8b. 88     88 88 88     88 88   YP88",
"88.d8P8.d8P  88     88   88     88 88     88 88 88     88 Y8.   .88",
"8888' Y88'   88     88   dP     dP dP     dP dP dP     dP  `88888'"
]

TUTORIAL_BANNER = [
"d888888P            dP                    oo          dP",
"   88               88                                88",
"   88    dP    dP d8888P .d8888b. 88d888b. dP .d8888b. 88 .d8888b.",
"   88    88    88   88   88'  `88 88'  `88 88 88'  `88 88 Y8ooooo.",
"   88    88.  .88   88   88.  .88 88      88 88.  .88 88      88",
"   dP    `88888P'   dP   `88888P' dP      dP `88888P8 dP `88888P'"
]

LUATOOLS_BANNER = [
"dP                          d888888P                  dP",
"88                             88                     88",
"88        dP    dP .d8888b.    88    .d8888b. .d8888b. 88 .d8888b.",
"88        88    88 88'  `88    88    88'  `88 88'  `88 88 Y8ooooo.",
"88        88.  .88 88.  .88    88    88.  .88 88.  .88 88      88",
"88888888P `88888P' `88888P8    dP    `88888P' `88888P' dP `88888P'"
]

SPICETIFY_BANNER = [
".d88888b           oo                  d888888P oo .8888b",          
"88.    '                                  88       88   ",          
"`Y88888b. 88d888b. dP .d8888b. .d8888b.    88    dP 88aaa  dP    dP", 
"      `8b 88'  `88 88 88'  `"" 88ooood8    88    88 88     88    88", 
"d8'   .8P 88.  .88 88 88.  ... 88.  ...    88    88 88     88.  .88", 
" Y88888P  88Y888P' dP `88888P' `88888P'    dP    dP dP     `8888P88", 
"          88                                                  .88", 
"          dP                                              d8888P" 
]

# ===== UTEIS =====
def clear():
    os.system("cls" if os.name == "nt" else "clear")

def print_banner(banner, c1, c2):
    for i, line in enumerate(banner):
        print(f"{c1 if i % 2 == 0 else c2}{line}{RESET}")

def pause():
    input("\nPressione Enter para continuar...")

def show_red_banner_with_text(text_lines):
    clear()
    for line in RED_BANNER:
        print(f"{RED}{line}{RESET}")
    print()
    for line in text_lines:
        print(f"{WHITE}{line}{RESET}")
    pause()

# ===== AVISOS =====
warning_text = [
    "AVISO: Esta configuração inclui software não oficial e pirata.",
    "Usar estes programas pode violar os termos de serviço.",
    "Você é totalmente responsável por quaisquer consequências.",
    "",
    "@tugaa._."
]

admin_warning = [
    "AVISO: Este programa pode exigir privilégios de administrador.",
    "Se algo falhar, execute como Administrador."
]

# ===== TUTORIAIS =====
def tutorials_luatools_menu():
    while True:
        clear()
        print(f"{RED}=== TUTORIAIS LUATOOLS ==={RESET}\n")
        print("[1] Conteúdo criptografado / Opção de reprodução ausente")
        print("[2] Novo método de instalação e correção")
        print("[3] Voltar\n")

        choice = input("Escolha: ").strip()
        if choice == "1":
            webbrowser.open("https://youtu.be/OT9YoGjpdiE")
        elif choice == "2":
            webbrowser.open("https://youtu.be/XS47HgqSts0")
        elif choice == "3":
            break
        else:
            print(f"\n{RED}Opção inválida!{RESET}") # Adicionado um feedback de erro
            pause()

def tutorials_pubslounge_menu():
    while True:
        clear()
        print(f"{RED}=== TUTORIAIS PUBS LOUNGE ==={RESET}\n")
        print("[1] Como usar o Pub's Lounge")
        print("[2] Voltar\n")

        choice = input("Escolha: ").strip()
        if choice == "1":
            webbrowser.open("https://youtu.be/r_RDh8FO7n0")
        elif choice == "2":
            break
        else:
            print(f"\n{RED}Opção inválida!{RESET}") # Adicionado um feedback de erro
            pause()

def tutorias_hydra_menu():
    while True:
        clear()
        print(f"{RED}=== TUTORIAIS HYDRA ==={RESET}")
        print("\n[1] Como Instalar o Hydra")
        print("[2] Melhores fontes do Hydra")
        print("[3] Voltar\n")


        choice = input("Escolha: ").strip()
        if choice == "1":
            webbrowser.open("https://www.youtube.com/watch?v=Zx-qRm0BB6I&t=3s")
        elif choice == "2":
            clear()
            print("[1] Kazumi (Melhor fonte para jogos modo historia)")
            print(f"{ORANGE}https://davidkazumi-github-io.pages.dev/fontekazumi.json{RESET}")
            print("[2] Online-fix( Melhor fonte para jogos Online)")
            print(f"{ORANGE}https://hydralinks.pages.dev/sources/onlinefix.json{RESET}")
            print("[3] Steam-RIP(2 opção caso não ter no Kazumi)")
            print(f"{ORANGE}https://hydralinks.pages.dev/sources/steamrip.json{RESET}")
            pause()
        elif choice == "3":
            break
        else:
            print(f"\n{RED}Opção inválida!{RESET}") # Adicionado um feedback de erro
            pause() 

def tutorials_menu():
    while True:
        clear()
        print_banner(TUTORIAL_BANNER, RED, WHITE)
        print("\n[1] Tutoriais LuaTools")
        print("[2] Tutoriais Pubs Lounge")
        print("[3] Tutorias Hydra")
        print("[4] Voltar\n")

        choice = input("Escolha: ").strip()
        if choice == "1":
            tutorials_luatools_menu()
        elif choice == "2":
            tutorials_pubslounge_menu()
        elif choice == "3":
            tutorias_hydra_menu()
        elif choice == "4":
            break
        else:
            print(f"\n{RED}Opção inválida!{RESET}") # Adicionado um feedback de erro
            pause()

# ===== MENUS =====
def lua_tools_menu():
    while True:
        clear()
        print_banner(LUATOOLS_BANNER, PURPLE, WHITE)
        print("\n[1] Instalar LuaTools")
        print("[2] Discord")
        print("[3] Sobre e o que faz")
        print("[4] Voltar\n")

        choice = input("Escolha: ").strip()
        if choice == "1":
            os.system('powershell -Command "irm -useb https://files.piqseu.cc/ltinstall-br | iex"')
            pause()
        elif choice == "2":
            webbrowser.open("https://discord.gg/luatools")
        elif choice == "3":
            clear()
            print(f"{PURPLE}=== SOBRE LUATOOLS ==={RESET}\n")
            print("O LuaTools é uma ferramenta utilizada para desbloquear")
            print("Jogos e conteúdos adicionais em jogos suportados.")
            print("\nPrincipais funções:")
            print(" - Desbloqueio de jogos e também DLCs")
            print(" - Acesso a recursos extras em jogos")
            print(" - ⚠️  Atenção, LuaTools é dependente do Millenium então se o")
            print(" Millenium tiver problemas você não consegue usar o LuaTools")
            pause()
        elif choice == "4":
            break
        else:
            print(f"\n{RED}Opção inválida!{RESET}") # Adicionado um feedback de erro
            pause()

def spicetify_menu():
    while True:
        clear()
        print_banner(SPICETIFY_BANNER, ORANGE, WHITE)
        print("\n[1] Instalar SpiceTify")
        print("[2] Discord")
        print("[3] Sobre e o que faz")
        print("[4] Voltar\n")

        choice = input("Escolha: ").strip()
        if choice == "1":
            os.system('powershell -Command "iwr -useb https://raw.githubusercontent.com/spicetify/cli/main/install.ps1 | iex"')
            pause()
        elif choice == "2":
            webbrowser.open("https://discord.gg/spicetify")
        elif choice == "3":
            clear()
            print(f"{ORANGE}=== SOBRE SPICETIFY ==={RESET}\n")
            print("O Spicetify é uma ferramenta que modifica o Spotify,")
            print("personalizar o cliente oficial do Spotify para Desktop.")
            print("\nPrincipais funções:")
            print(" - Instalação de temas personalizados")
            print(" - Instalação de extensões e apps customizados")
            print(" - Remoção de elementos indesejados da interface")
            print(" - Consegue remover anúncios e muito mais")
            pause()
        elif choice == "4":
            break
        else:
            print(f"\n{RED}Opção inválida!{RESET}") # Adicionado um feedback de erro
            pause()

def steamtools_menu():
    while True:
        clear()
        print_banner(STEAMTOOLS_BANNER, BLUE, WHITE)
        print("\n[1] Instalar SteamTools")
        print("[2] Sobre e o que faz")
        print("[3] Telegram")
        print("[4] Voltar\n")

        # FIX: Adicionado () em .strip() e corrigido o nome da variável para 'choice'
        choice = input("Escolha: ").strip() 
        
        if choice == "1":
            webbrowser.open("https://steamtools.net/download")
        elif choice == "2":
            clear()
            print(f"{BLUE}=== SOBRE STEAMTOOLS ==={RESET}\n")
            print("SteamTools é uma ferramenta muito famosa para gerenciamento de jogos,") # Corrigido "famosa"
            print("ela gerencia quase tudo, e muitos outros softwares são dependentes dela.")
            print("\nPrincipais funções:")
            print(" - Instalação de jogos")
            print(" - Instalação de DLCs")
            print(" - Abre portas para outros programas integrados")
            pause()
        elif choice == "3":
            webbrowser.open("https://t.me/steamtool")
        elif choice == "4":
            break
        else:
            print(f"\n{RED}Opção inválida!{RESET}") # Adicionado um feedback de erro
            pause()

def hydra_menu():
    while True:
        clear()
        print_banner(HYDRA_BANNER, GREEN, WHITE)
        print("\n[1] Instalar o Hydra")
        print("[2] Sobre e o que faz")
        print("[3] GitHub")
        print("[4] Voltar\n")


        choice = input("Escolha: ").strip()

        if choice == "1":
            webbrowser.open("https://hydralauncher.gg/HydraInstaller.exe")
        elif choice == "2":
            webbrowser.open("https://hydralauncher.gg/#about")
        elif choice == "3":
            webbrowser.open("https://github.com/hydralauncher/hydra")
        elif choice == "4":
            break
        else:
           print(f"\n{RED}Opção inválida!{RESET}")
           pause()


def main_menu():
    while True:
        clear()
        print(f"{PURPLE}=== MENU PRINCIPAL ==={RESET}\n")
        print("\n[1] LuaTools")
        print("[2] SpiceTify")
        print("[3] SteamTools")
        print("[4] Hydra")
        print("[5] Tutoriais e Correções")
        print("[6] Sair\n")

        choice = input("Escolha: ").strip()
        if choice == "1":
            lua_tools_menu()
        elif choice == "2":
            spicetify_menu()
        elif choice == "3":
            steamtools_menu()
        elif choice == "4":
            hydra_menu()
        elif choice == "5":
            tutorials_menu()
        elif choice == "6":
            sys.exit()
        else:
            print(f"\n{RED}Opção inválida!{RESET}") # Adicionado um feedback de erro
            pause()

# ===== INICIO =====
show_red_banner_with_text(warning_text)
show_red_banner_with_text(admin_warning)
main_menu()
