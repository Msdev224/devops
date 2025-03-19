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
    }
    post {
        always {
            sh 'docker-compose down || true'
        }
    }
}