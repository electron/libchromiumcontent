const args = require('minimist')(process.argv.slice(2))
const assert = require('assert')
const octokit = require('@octokit/rest')()
const s3Url = 'https://s3.amazonaws.com/github-janky-artifacts/libchromiumcontent'

assert(process.env.LIBCHROMIUMCONTENT_GITHUB_TOKEN, 'LIBCHROMIUMCONTENT_GITHUB_TOKEN not found in environment')

async function postBuildResults () {
  octokit.authenticate({
    type: 'oauth',
    token: process.env.LIBCHROMIUMCONTENT_GITHUB_TOKEN
  })

  try {
    let buildSummary
    if (args.failed) {
      buildSummary = `:x: ${args.buildName} failed for ${args.commitId}.`
    } else {
      buildSummary = `:white_check_mark: ${args.buildName} succeeded for ${args.commitId}.`
    }
    let body = `${buildSummary}  [Details](${s3Url}/${args.logFile})`
    const githubOpts = {
      owner: 'electron',
      repo: 'libchromiumcontent',
      number: args.prNumber,
      body
    }
    await octokit.issues.createComment(githubOpts)
  } catch (ex) {
    console.log(`Error uploading build results`, ex)
  }
}

if (!args.buildName || !args.logFile || !args.prNumber || !args.commitId) {
  console.log(`Usage: upload-build-results --buildname=BUILD_NAME ` +
    `--logFile=LOG_FILE --prNumber=PR_NUMBER, --commitId=COMMIT_ID`)
  process.exit(1)
}
postBuildResults()
