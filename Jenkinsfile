pipeline {
    agent any
  
  
    stages {
        stage('Build Docker') {
            steps {
                sh 'docker build -t bitcoin_price .'
            }
        }
        
        stage('Tag Docker') {
            steps {
                sh 'docker tag bitcoin-price kewanrashed/bitcoin_price'
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

    post {
        failure {
            script {
                slackSend(
                color: "#FF0000",
                channel: "automation",
                message: "Bitcoin_Price Status: FAILED"
                )
            }
        }

        success {
            script {
                slackSend(
                    color: "#00FF00",
                    channel: "automation",
                    message: "Bitcoin_Price Status: SUCCESS"
                ) 
            }
        }
    }
}