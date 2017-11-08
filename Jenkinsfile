pipeline {
  agent none
  stages {
    stage('Build') {
      parallel {
        stage('libchromiumcontent-osx') {
            agent {
              label 'osx-libcc'
            }
            environment {
              LIBCHROMIUMCONTENT_GIT_CACHE='/Volumes/LIBCC_CACHE'
            }
            steps {
              sh 'script/cibuild'
            }
            post {
              always {
                cleanWs()
              }
              success {
                 archive 'libchromiumcontent.zip'
                 archive 'libchromiumcontent-static.zip'
              }
            }
        }
        stage('libchromiumcontent-mas') {
          agent {
            label 'osx-libcc'
          }
          environment {
            MAS_BUILD = '1'
            LIBCHROMIUMCONTENT_GIT_CACHE='/Volumes/LIBCC_CACHE'
          }
          steps {
            sh 'script/cibuild'
          }
          post {
            always {
              cleanWs()
            }
            success {
               archive 'libchromiumcontent.zip'
               archive 'libchromiumcontent-static.zip'
            }
          }
        }
      }
    }
  }
}
