param([switch]$skipUpload, [switch]$useSccache, [switch]$buildTests)
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
$CommandLine = "python .\script\cibuild"
if ($skipUpload) {
  $CommandLine += " --skip_upload"
}

if ($useSccache) {
  $CommandLine += " --use_sccache"
}

if ($buildTests) {
  $CommandLine += " --build_tests"
}
$CICommand = [ScriptBlock]::Create($CommandLine)
Run-Command -Fatal $CICommand
