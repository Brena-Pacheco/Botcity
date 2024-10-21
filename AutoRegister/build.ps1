$exclude = @("venv", "AutoRegister.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "AutoRegister.zip" -Force