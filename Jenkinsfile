pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/Msdev224/devops.git', branch: 'main'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t my-django-app:latest .'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'docker run my-django-app:latest python manage.py test'
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker-compose down'
                sh 'docker-compose up -d --build'
            }
        }
        stage('Expose with Ngrok') {
            steps {
                sh 'curl -sL https://ngrok.com/install | bash -s -- ngrok'  
                sh './ngrok http 8000 & sleep 5' 
                sh 'curl -s http://localhost:4040/api/tunnels | jq -r .tunnels[0].public_url > ngrok_url.txt'  
                sh 'cat ngrok_url.txt'  
            }
        }
    }
    post {
        always {
            sh 'docker-compose down || true'
        }
    }
}