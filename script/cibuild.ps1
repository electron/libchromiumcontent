param([switch]$skipUpload)
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

Write-Output ""
if ($skipUpload) {
  Run-Command -Fatal { python .\script\cibuild --skip_upload }
} else {
  Run-Command -Fatal { python .\script\cibuild }
}
