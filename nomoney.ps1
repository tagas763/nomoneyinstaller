# ===== COLORS =====
$RED = "Red"
$PURPLE = "Magenta"
$ORANGE = "Yellow"
$WHITE = "White"

# ===== BANNERS =====
$RED_BANNER = @(
"dP   dP   dP  .d888888   888888ba  888888ba  dP 888888ba   .88888.  ",
"88   88   88 d8'    88   88    `8b 88    `8b 88 88    `8b d8'   `88 ",
"88  .8P  .8P 88aaaaa88a a88aaaa8P' 88     88 88 88     88 88        ",
"88  d8'  d8' 88     88   88   `8b. 88     88 88 88     88 88   YP88 ",
"88.d8P8.d8P  88     88   88     88 88     88 88 88     88 Y8.   .88 ",
"8888' Y88'   88     88   dP     dP dP     dP dP dP     dP  `88888'  "
)

$LUATOOLS_BANNER = @(
"dP                          d888888P                   dP          ",
"88                             88                      88          ",
"88        dP    dP .d8888b.    88    .d8888b. .d8888b. 88 .d8888b. ",
"88        88    88 88'  `88    88    88'  `88 88'  `88 88 Y8ooooo. ",
"88        88.  .88 88.  .88    88    88.  .88 88.  .88 88       88 ",
"88888888P `88888P' `88888P8    dP    `88888P' `88888P' dP `88888P' "
)

$SPICETIFY_BANNER = @(
".d88888b           oo                   d888888P oo .8888b          ",
"88.    \"'                                  88       88   \"          ",
"`Y88888b. 88d888b. dP .d8888b. .d8888b.    88    dP 88aaa  dP    dP ",
"      `8b 88'  `88 88 88'  `\"\" 88ooood8    88    88 88     88    88 ",
"d8'   .8P 88.  .88 88 88.  ... 88.  ...    88    88 88     88.  .88 ",
" Y88888P  88Y888P' dP `88888P' `88888P'    dP    dP dP     `8888P88 ",
"          88                                                    .88 ",
"          dP                                                d8888P  "
)

# ===== FUNCTIONS =====
function Print-Banner ($banner, $color1, $color2) {
    for ($i=0; $i -lt $banner.Count; $i++) {
        if ($i % 2 -eq 0) { Write-Host $banner[$i] -ForegroundColor $color1 }
        else { Write-Host $banner[$i] -ForegroundColor $color2 }
    }
    Write-Host ""
}

function Pause() {
    Write-Host "`nPress Enter to continue..." -ForegroundColor $WHITE
    [void][System.Console]::ReadLine()
}

# ===== WARNING =====
$warning_text = @(
"This setup includes software that is considered pirated or unofficial.",
"Using these programs may violate the terms of service of the original applications.",
"You are solely responsible for any consequences resulting from their use,",
"including account bans, legal issues, or other risks.",
"By continuing, you acknowledge and accept all risks associated with using this setup."
)

Clear-Host
Print-Banner $RED_BANNER $RED $WHITE
foreach ($line in $warning_text) { Write-Host $line -ForegroundColor $WHITE }
Pause

# ===== MENUS =====
function LuaTools-Menu {
    while ($true) {
        Clear-Host
        Print-Banner $LUATOOLS_BANNER $PURPLE $WHITE
        Write-Host "[1] Install LuaTools"
        Write-Host "[2] What is LuaTools"
        Write-Host "[3] Discord"
        Write-Host "[4] Back"
        $choice = Read-Host "Choose an option"
        switch ($choice) {
            "1" {
                iwr -useb "https://luatools.vercel.app/install-plugin.ps1" | iex
                Pause
            }
            "2" {
                Clear-Host
                Print-Banner $LUATOOLS_BANNER $PURPLE $WHITE
                Write-Host "LuaTools is a software used with SteamTools to add unofficial games to the Steam library." -ForegroundColor $PURPLE
                Write-Host "It does not provide games, it only helps integrate and organize them within Steam." -ForegroundColor $WHITE
                Write-Host "Usage may violate Steam's terms and is the user's responsibility." -ForegroundColor $PURPLE
                Pause
            }
            "3" {
                Start-Process "https://discord.gg/luatools"
                Pause
            }
            "4" { break }
            default { Write-Host "Invalid option." -ForegroundColor Red; Pause }
        }
    }
}

function SpiceTify-Menu {
    while ($true) {
        Clear-Host
        Print-Banner $SPICETIFY_BANNER $ORANGE $WHITE
        Write-Host "[1] Install SpiceTify"
        Write-Host "[2] What is SpiceTify"
        Write-Host "[3] Discord"
        Write-Host "[4] Back"
        $choice = Read-Host "Choose an option"
        switch ($choice) {
            "1" {
                $answer = Read-Host "Do you have Spotify installed? (Y/N)"
                if ($answer.ToUpper() -eq "Y") {
                    iwr -useb "https://raw.githubusercontent.com/spicetify/cli/main/install.ps1" | iex
                } elseif ($answer.ToUpper() -eq "N") {
                    Start-Process "https://download.scdn.co/SpotifySetup.exe"
                } else {
                    Write-Host "Invalid input." -ForegroundColor Red
                }
                Pause
            }
            "2" {
                Clear-Host
                Print-Banner $SPICETIFY_BANNER $ORANGE $WHITE
                Write-Host "SpiceTify is a software designed to enhance the Spotify experience by unlocking deeper customization and a cleaner interface." -ForegroundColor $ORANGE
                Write-Host "It allows users to enjoy music without ads and personalize the app’s visual theme, transforming Spotify into something that feels truly their own." -ForegroundColor $WHITE
                Write-Host "Built for users who want more control and personality, SpiceTify focuses on freedom, customization, and immersion, delivering a smoother and more visually engaging listening experience beyond the standard limitations." -ForegroundColor $ORANGE
                Write-Host "SpiceTify isn’t about following the default — it’s about upgrading how music feels." -ForegroundColor $WHITE
                Pause
            }
            "3" {
                Start-Process "https://discord.gg/spicetify"
                Pause
            }
            "4" { break }
            default { Write-Host "Invalid option." -ForegroundColor Red; Pause }
        }
    }
}

# ===== MAIN MENU =====
while ($true) {
    Clear-Host
    Write-Host "=== SELECT A CATEGORY ===" -ForegroundColor $PURPLE
    Write-Host "[1] LuaTools"
    Write-Host "[2] SpiceTify"
    Write-Host "[3] Exit"
    $opt = Read-Host "Choose an option"
    switch ($opt) {
        "1" { LuaTools-Menu }
        "2" { SpiceTify-Menu }
        "3" { break }
        default { Write-Host "Invalid option." -ForegroundColor Red; Pause }
    }
}
