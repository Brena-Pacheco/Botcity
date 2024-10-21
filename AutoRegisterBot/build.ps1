$exclude = @("venv", "AutoRegisterBot.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "AutoRegisterBot.zip" -Force