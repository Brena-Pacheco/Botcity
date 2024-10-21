$exclude = @("venv", "auto_register.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "auto_register.zip" -Force