pipeline {
    agent any
    environment {
        VENV_DIR = 'venv'
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/RVICTOIRE/test_devops.git'
            }
        }
        stage('Validate Environment') {
            steps {
                script {
                    try {
                        sh 'git --version'
                        sh 'python3 --version'
                        sh 'pip3 --version'
                    } catch (err) {
                        echo "Erreur lors de la validation de l'environnement : ${err}"
                        currentBuild.result = 'FAILURE'
                        error("Échec de la validation de l'environnement")
                    }
                }
            }
        }
        stage('Debug Git') {
            steps {
                sh 'git config --list'
                sh 'git remote -v'
            }
        }
        stage('Setup') {
            steps {
                script {
                    try {
                        sh '''
                            python3 -m venv venv
                            . venv/bin/activate
                            pip install --upgrade pip
                            pip install -r requirements.txt
                        '''
                    } catch (err) {
                        echo "Erreur lors de la configuration de l'environnement : ${err}"
                        currentBuild.result = 'FAILURE'
                        error("Échec de la configuration de l'environnement")
                    }
                }
            }
        }
        stage('Run Script') {
            steps {
                script {
                    try {
                        sh '''
                            . venv/bin/activate
                            python app.py
                        '''
                    } catch (err) {
                        echo "Erreur lors de l'exécution du script : ${err}"
                        currentBuild.result = 'FAILURE'
                        error("Échec de l'exécution du script")
                    }
                }
            }
        }
    }
    post {
        always {
            script {
                def result = currentBuild.result ?: 'SUCCESS'
                emailext subject: "Jenkins Build: ${result}",
                    body: "Build Status: ${result}\nVoir Jenkins: ${env.BUILD_URL}",
                    to: 'Rabysene17@gmail.com',
                    attachLog: true
            }
        
            sh 'rm -rf venv'
        }
    }
}