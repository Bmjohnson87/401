# bard
# Set the desired screen lock timeout in seconds (adjust as needed)
$timeoutInSeconds = 600  # 10 minutes

# Function to check idle time and lock screen if necessary
function Check-IdleTime {
    $idleTime = (Get-CimInstance -ClassName Win32_Process -Filter "name = 'explorer.exe'").LastInputTime
    $idleTimeSpan = New-TimeSpan -Start $idleTime -End (Get-Date)

    if ($idleTimeSpan.TotalSeconds -ge $timeoutInSeconds) {
        rundll32.exe user32.dll,LockWorkStation
    }
}

# Start the idle time check loop
while ($true) {
    Check-IdleTime
    Start-Sleep -Seconds 10  # Check every 10 seconds
}
