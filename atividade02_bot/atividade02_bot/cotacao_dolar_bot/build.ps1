$exclude = @("venv", "cotacao_dolar_bot.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "cotacao_dolar_bot.zip" -Force