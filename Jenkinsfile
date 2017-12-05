pipeline {
  agent none
  stages {
    stage('Build') {
      parallel {
        stage('libchromiumcontent-osx-shared') {
            agent {
              label 'osx-libcc'
            }
            environment {
              LIBCHROMIUMCONTENT_GIT_CACHE = '/Volumes/LIBCC_CACHE'
              COMPONENT = 'shared_library'
              TARGET_ARCH = 'x64'
            }
            steps {
              echo "Branch name is:${BRANCH_NAME}"
              if ($BRANCH_NAME =~ ^master|electron-\n-\n-x) {
                echo "BRANCH IS SPECIAL"
              } else {
                echo "BRANCH IS NOT SPECIAL"
              }
              currentBuild.result = 'ABORTED'
              error('Stopping early because this is a test')


              sh 'script/bootstrap'
              sh 'script/update --clean -t $TARGET_ARCH'
              sh 'script/build -t $TARGET_ARCH -c $COMPONENT'
              sh 'script/build -t $TARGET_ARCH -c ffmpeg'
              sh 'script/create-dist -t $TARGET_ARCH -c $COMPONENT'
              script {
                GIT_COMMIT = sh(returnStdout: true, script: "git rev-parse HEAD").trim()
              }
              withCredentials([string(credentialsId: 'libccbucket', variable: 'LIBCC_BUCKET')]) {
                withAWS(credentials:'libccs3',region:'us-east-1') {
                  s3Upload(file:'libchromiumcontent.zip', bucket:"${LIBCC_BUCKET}", path:"libchromiumcontent/osx/${env.TARGET_ARCH}/${GIT_COMMIT}/libchromiumcontent.zip", acl:'PublicRead')
                }
              }
            }
            post {
              always {
                archive 'libchromiumcontent.zip'
                cleanWs()
              }
            }
        }
        stage('libchromiumcontent-osx-static') {
            agent {
              label 'osx-libcc'
            }
            environment {
              LIBCHROMIUMCONTENT_GIT_CACHE = '/Volumes/LIBCC_CACHE'
              COMPONENT = 'static_library'
              TARGET_ARCH = 'x64'
            }
            steps {
              sh 'script/bootstrap'
              sh 'script/update --clean -t $TARGET_ARCH'
              sh 'script/build -t $TARGET_ARCH -c $COMPONENT'
              sh 'script/build -t $TARGET_ARCH -c ffmpeg'
              sh 'script/create-dist -t $TARGET_ARCH -c $COMPONENT'
              script {
                GIT_COMMIT = sh(returnStdout: true, script: "git rev-parse HEAD").trim()
              }
              withCredentials([string(credentialsId: 'libccbucket', variable: 'LIBCC_BUCKET')]) {
                withAWS(credentials:'libccs3',region:'us-east-1') {
                  s3Upload(file:'libchromiumcontent-static.zip', bucket:"${LIBCC_BUCKET}", path:"libchromiumcontent/osx/${env.TARGET_ARCH}/${GIT_COMMIT}/libchromiumcontent-static.zip", acl:'PublicRead')
                }
              }
            }
            post {
              always {
                archive 'libchromiumcontent-static.zip'
                cleanWs()
              }
            }
        }
        stage('libchromiumcontent-mas-shared') {
          agent {
            label 'osx-libcc'
          }
          environment {
            MAS_BUILD = '1'
            LIBCHROMIUMCONTENT_GIT_CACHE = '/Volumes/LIBCC_CACHE'
            COMPONENT = 'shared_library'
            TARGET_ARCH = 'x64'
          }
          steps {
            sh 'script/bootstrap'
            sh 'script/update --clean -t $TARGET_ARCH'
            sh 'script/build -t $TARGET_ARCH -c $COMPONENT'
            sh 'script/build -t $TARGET_ARCH -c ffmpeg'
            sh 'script/create-dist -t $TARGET_ARCH -c $COMPONENT'
            script {
              GIT_COMMIT = sh(returnStdout: true, script: "git rev-parse HEAD").trim()
            }
            withCredentials([string(credentialsId: 'libccbucket', variable: 'LIBCC_BUCKET')]) {
              withAWS(credentials:'libccs3',region:'us-east-1') {
                s3Upload(file:'libchromiumcontent.zip', bucket:"${LIBCC_BUCKET}", path:"libchromiumcontent/mas/${env.TARGET_ARCH}/${GIT_COMMIT}/libchromiumcontent.zip", acl:'PublicRead')
              }
            }
          }
          post {
            always {
              archive 'libchromiumcontent.zip'
              cleanWs()
            }
          }
        }
        stage('libchromiumcontent-mas-static') {
          agent {
            label 'osx-libcc'
          }
          environment {
            MAS_BUILD = '1'
            LIBCHROMIUMCONTENT_GIT_CACHE = '/Volumes/LIBCC_CACHE'
            COMPONENT = 'static_library'
            TARGET_ARCH = 'x64'
          }
          steps {
            sh 'script/bootstrap'
            sh 'script/update --clean -t $TARGET_ARCH'
            sh 'script/build -t $TARGET_ARCH -c $COMPONENT'
            sh 'script/build -t $TARGET_ARCH -c ffmpeg'
            sh 'script/create-dist -t $TARGET_ARCH -c $COMPONENT'
            script {
              GIT_COMMIT = sh(returnStdout: true, script: "git rev-parse HEAD").trim()
            }
            withCredentials([string(credentialsId: 'libccbucket', variable: 'LIBCC_BUCKET')]) {
              withAWS(credentials:'libccs3',region:'us-east-1') {
                s3Upload(file:'libchromiumcontent-static.zip', bucket:"${LIBCC_BUCKET}", path:"libchromiumcontent/mas/${env.TARGET_ARCH}/${GIT_COMMIT}/libchromiumcontent-static.zip", acl:'PublicRead')
              }
            }
          }
          post {
            always {
              archive 'libchromiumcontent-static.zip'
              cleanWs()
            }
          }
        }
      }
    }
  }
}
