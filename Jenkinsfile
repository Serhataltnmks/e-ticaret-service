pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/serhataltnmks/e-ticaret-service.git'
            }
        }
        stage('Build and Push Docker Images') {
            steps {
                script {
                    def services = ["product_service", "order_service", "user_service"]
                    services.each { service ->
                        dockerImage = docker.build("${service}:${env.BUILD_ID}", "${service}")
                        dockerImage.push()
                    }
                }
            }
        }
        stage('Deploy Services') {
            steps {
                script {
                    def services = ["product_service", "order_service", "user_service"]
                    services.each { service ->
                        sh "docker run -d --name ${service} -p 5000${services.indexOf(service)+1}:5000${services.indexOf(service)+1} ${service}:${env.BUILD_ID}"
                    }
                }
            }
        }
    }
}
