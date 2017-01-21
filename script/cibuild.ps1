function Run-Command([scriptblock]$Command, [switch]$Fatal, [switch]$Quiet) {
  $output = ""
  try {
    if ($Quiet) {
      $output = & $Command 2>&1
    } else {
      & $Command
    }
  } catch {
    throw
  }

  if (!$Fatal) {
    return
  }

  $exitCode = 0
  if ($LastExitCode -ne 0) {
    $exitCode = $LastExitCode
  } elseif (!$?) {
    $exitCode = 1
  } else {
    return
  }

  $error = "Error executing command ``$Command``."
  if ($output) {
    $error += " Output:" + [System.Environment]::NewLine + $output
  }
  Write-Output $error
  exit $exitCode
}

# Make the output width reeeeeaaaaaly wide so our output doesn't get hard-wrapped.
# <http://stackoverflow.com/questions/978777/powershell-output-column-width>
$Host.UI.RawUI.BufferSize = New-Object Management.Automation.Host.Size -ArgumentList 5000, 25

Write-Output ""
Run-Command -Fatal { python .\script\cibuild }
