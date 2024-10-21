$exclude = @("venv", "climamanausbot.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "climamanausbot.zip" -Force