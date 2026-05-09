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
                    docker run --rm \
                      -v ${WORKSPACE}/reports:/app/reports \
                      sdet-tests:latest
                '''
            }
        }

        stage('Publish Report') {
            steps {
                publishHTML(target: [
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: 'reports',
                    reportFiles: 'report.html',
                    reportName: 'Test Report'
                ])
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
            mail(
                to: 'rohitkd430@gmail.com',
                subject: "✅ PASSED: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: """
                    Build passed successfully.
                    Job: ${env.JOB_NAME}
                    Build: #${env.BUILD_NUMBER}
                    URL: ${env.BUILD_URL}
                """
            )
        }
        failure {
            echo '❌ Tests failed!'
            mail(
                to: 'rohitkd430@gmail.com',
                subject: "❌ FAILED: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: """
                    Build failed! Check the test report.
                    Job: ${env.JOB_NAME}
                    Build: #${env.BUILD_NUMBER}
                    URL: ${env.BUILD_URL}
                    Report: ${env.BUILD_URL}Test_Report/
                """
            )
        }
    }
}