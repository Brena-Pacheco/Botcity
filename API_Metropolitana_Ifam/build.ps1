$exclude = @("venv", "API_Metropolitana_Ifam.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "API_Metropolitana_Ifam.zip" -Force