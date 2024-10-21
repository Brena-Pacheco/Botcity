$exclude = @("venv", "API_Metropolitana_Para_clima.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "API_Metropolitana_Para_clima.zip" -Force