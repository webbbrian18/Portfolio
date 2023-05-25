$KB = "WHICHEVER KB YOU CHOOSE"
try {
    $HotFixes = Get-HotFix -Id $KB -ErrorAction Stop

    Write-Output "Update $KB is already installed on this computer."
} catch {
    Write-Output "Update $KB is not installed on this computer. Downloading and installing..."

    $url = "MICROSOFT LINK FOR KB DOWNLOAD"
    $path = "$env:USERPROFILE\Downloads\$KB.msu"

    try {
        Invoke-WebRequest -Uri $url -OutFile $path -ErrorAction Stop
        Start-Process -FilePath wusa.exe -ArgumentList $path,"/quiet","/norestart" -Wait -ErrorAction Stop
        Write-Output "Update $KB has been installed on this computer."
    } catch {
        Write-Output "Error: $_"
    }
}