pipeline {

  agent any
  
  
  stages {
      
       stage('Clone Git') {
            steps {
                git url:'https://github.com/RashedKewan/Docker-Final-Task.git' , branch:'master'
            }
        }
        
        stage('Build Image') {
            steps {
                sh 'docker build -t bitcoin_price .'
            }
        }
        
        stage('Tag Image') {
            steps {
                sh 'docker tag bitcoin_price kewanrashed/bitcoin_price'
            }
        }

        stage('Push Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub', passwordVariable: 'pass', usernameVariable: 'username')]) {
                    sh 'docker login -u ${username} -p ${pass}'
                    sh 'docker push kewanrashed/bitcoin_price'
                }
            }
        }
    }

  
}
