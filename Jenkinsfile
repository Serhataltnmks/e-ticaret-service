pipline {
        agent any

        stages {
                stage('Clone Repository'){
                steps {
                        git 'https://github.com/Serhataltnmks/e-ticaret-service.git'
                        }
                }
                stage('Build and Push Docker Images') {
                steps {
                        script {
                                def services=["product-service", "order-service", "user-service"]
                                services.each { service ->
                                        dockerImage = docker.build("${service}:${env.BUILD_ID}", "${service}")
                                        dockerImage.push()
                                        }
                                }
                        }
                }
                stage('Deploy Service') {
                steps {
                        script {
                                def services=["product-service", "order-service", "user-service"]
                                services.each { service ->
                                        sh "docker run -d --name ${service} -p 5000${services.indexOf(service)+1}:5000${services.indexOf(service)+1} ${service}:${env.BUILD_ID}"
                                        }
                                }
                        }
                }
        }
}

