pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Pulling code from GitHub...'
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                sh 'docker build -t sdet-tests:latest .'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running tests inside container...'
                sh '''
                    mkdir -p reports
                    chmod 777 reports
                    docker run --rm \
                      -v ${WORKSPACE}/reports:/app/reports \
                      sdet-tests:latest
                '''
            }
        }

        stage('Archive Report') {
            steps {
                archiveArtifacts artifacts: 'reports/report.html',
                                 fingerprint: true,
                                 allowEmptyArchive: false
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished. Cleaning up...'
            sh 'docker rmi sdet-tests:latest || true'
        }
        success {
            echo '✅ All tests passed!'
        }
        failure {
            echo '❌ Tests failed!'
        }
    }
}