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
              timeout(300) {
                sh 'script/bootstrap'
                sh 'script/update --clean -t $TARGET_ARCH --ignore_git_cache_locks'
                sh 'script/build -t $TARGET_ARCH -c $COMPONENT'
                sh 'script/build -t $TARGET_ARCH -c ffmpeg'
                sh 'script/create-dist -t $TARGET_ARCH -c $COMPONENT'
                script {
                  GIT_COMMIT = sh(returnStdout: true, script: "git rev-parse HEAD").trim()
                }
                withCredentials([string(credentialsId: 'libccbucket', variable: 'LIBCC_BUCKET')]) {
                  withAWS(credentials:'libccs3',region:'us-east-1') {
                    s3Upload(file:'libchromiumcontent.tar.bz2', bucket:"${LIBCC_BUCKET}", path:"libchromiumcontent/osx/${env.TARGET_ARCH}/${GIT_COMMIT}/libchromiumcontent.tar.bz2", acl:'PublicRead')
                  }
                }
                fileOperations([fileRenameOperation(destination: 'libchromiumcontent-osx.tar.bz2', source: 'libchromiumcontent.tar.bz2')])
              }
            }
            post {
              always {
                archive 'libchromiumcontent-osx.tar.bz2'
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
              timeout(300) {
                sh 'script/bootstrap'
                sh 'script/update --clean -t $TARGET_ARCH --ignore_git_cache_locks'
                sh 'script/build -t $TARGET_ARCH -c $COMPONENT'
                sh 'script/build -t $TARGET_ARCH -c ffmpeg'
                sh 'script/create-dist -t $TARGET_ARCH -c $COMPONENT'
                script {
                  GIT_COMMIT = sh(returnStdout: true, script: "git rev-parse HEAD").trim()
                }
                withCredentials([string(credentialsId: 'libccbucket', variable: 'LIBCC_BUCKET')]) {
                  withAWS(credentials:'libccs3',region:'us-east-1') {
                    s3Upload(file:'libchromiumcontent-static.tar.bz2', bucket:"${LIBCC_BUCKET}", path:"libchromiumcontent/osx/${env.TARGET_ARCH}/${GIT_COMMIT}/libchromiumcontent-static.tar.bz2", acl:'PublicRead')
                  }
                }
                fileOperations([fileRenameOperation(destination: 'libchromiumcontent-static-osx.tar.bz2', source: 'libchromiumcontent-static.tar.bz2')])
              }
            }
            post {
              always {
                archive 'libchromiumcontent-static-osx.tar.bz2'
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
            timeout(300) {
              sh 'script/bootstrap'
              sh 'script/update --clean -t $TARGET_ARCH --ignore_git_cache_locks'
              sh 'script/build -t $TARGET_ARCH -c $COMPONENT'
              sh 'script/build -t $TARGET_ARCH -c ffmpeg'
              sh 'script/create-dist -t $TARGET_ARCH -c $COMPONENT'
              script {
                GIT_COMMIT = sh(returnStdout: true, script: "git rev-parse HEAD").trim()
              }
              withCredentials([string(credentialsId: 'libccbucket', variable: 'LIBCC_BUCKET')]) {
                withAWS(credentials:'libccs3',region:'us-east-1') {
                  s3Upload(file:'libchromiumcontent.tar.bz2', bucket:"${LIBCC_BUCKET}", path:"libchromiumcontent/mas/${env.TARGET_ARCH}/${GIT_COMMIT}/libchromiumcontent.tar.bz2", acl:'PublicRead')
                }
              }
              fileOperations([fileRenameOperation(destination: 'libchromiumcontent-mas.tar.bz2', source: 'libchromiumcontent.tar.bz2')])
            }
          }
          post {
            always {
              archive 'libchromiumcontent-mas.tar.bz2'
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
            timeout(300) {
              sh 'script/bootstrap'
              sh 'script/update --clean -t $TARGET_ARCH --ignore_git_cache_locks'
              sh 'script/build -t $TARGET_ARCH -c $COMPONENT'
              sh 'script/build -t $TARGET_ARCH -c ffmpeg'
              sh 'script/create-dist -t $TARGET_ARCH -c $COMPONENT'
              script {
                GIT_COMMIT = sh(returnStdout: true, script: "git rev-parse HEAD").trim()
              }
              withCredentials([string(credentialsId: 'libccbucket', variable: 'LIBCC_BUCKET')]) {
                withAWS(credentials:'libccs3',region:'us-east-1') {
                  s3Upload(file:'libchromiumcontent-static.tar.bz2', bucket:"${LIBCC_BUCKET}", path:"libchromiumcontent/mas/${env.TARGET_ARCH}/${GIT_COMMIT}/libchromiumcontent-static.tar.bz2", acl:'PublicRead')
                }
              }
              fileOperations([fileRenameOperation(destination: 'libchromiumcontent-mas-static.tar.bz2', source: 'libchromiumcontent-static.tar.bz2')])
            }
          }
          post {
            always {
              archive 'libchromiumcontent-mas-static.tar.bz2'
              cleanWs()
            }
          }
        }
      }
    }
  }
}
