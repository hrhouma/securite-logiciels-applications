
# 1 - JENKINS

## Jenkins sur VM
- Java base application build with Maven on Jenkins | by Areful Islam | DevOps.dev 
- JAVA:  https://blog.devops.dev/java-base-application-build-with-maven-on-jenkins-540cad37370f
- MAVEN : https://phoenixnap.com/kb/install-maven-on-ubuntu
## Jenkins CI/CD Pipeline (JENKINS DOCKER)
- https://aws.plainenglish.io/jenkins-ci-cd-pipeline-explained-by-a-junior-devops-engineer-1d67ecc08a7e 

# 2 - SONAR
Integrating SonarQube with Jenkins Pipeline | by Abubakr Sadiq | May, 2024 | Medium 
https://medium.com/@abubakr.sadiq/integrating-sonarqube-with-jenkins-pipeline-5bbfe3b46655 


# 3 - Les 3 ensembles
- CI/CD Pipeline with Jenkins + SonarQube + Docker Registry -1- | by Ozan Bozkurt | Medium 

https://medium.com/@ozanbozkurtt96/ci-cd-ipeline-with-jenkins-sonarqube-docker-registry-1-7fa07f172560 

# 4 - BEST
- https://faun.pub/setting-up-dockerized-jenkins-and-sonarqube-in-linux-environment-155ce52b884a
- https://levelup.gitconnected.com/complete-maven-jenkins-sonarqube-jfrog-tomcat-set-up-4c32f6bab04f

# 5 - Les WEBHOOKS

- https://docs.github.com/en/webhooks/using-webhooks/creating-webhooks
- https://suryansh-mathema.medium.com/ci-cd-with-jenkins-git-webhook-automation-946eeaba8b5f
- https://medium.com/@sangeetv09/how-to-configure-webhook-in-github-and-jenkins-for-automatic-trigger-with-cicd-pipeline-34133e9de0ea
- https://betterprogramming.pub/how-too-add-github-webhook-to-a-jenkins-pipeline-62b0be84e006
- https://www.linkedin.com/feed/?trk=public_post_google-one-tap-submit
- https://www.geeksforgeeks.org/how-to-setup-up-jenkins-webhooks-for-automated-builds/
- https://faun.pub/triggering-jenkins-build-on-push-using-github-webhooks-52d4361542d4
- https://medium.com/@samarthgvasist/setting-up-a-github-webhook-ccd895e7b85c
- https://medium.com/@madhavarajas1997/a-comprehensive-guide-to-jenkins-webhooks-06497ace0824
- https://dev.to/robbiecahill/how-to-add-a-github-webhook-to-jenkins-5f34

# 6 - BEST PROJET COMPLET + SONAR 
- https://chirag0002.hashnode.dev/build-a-cicd-pipeline-using-jenkins-sonarqube-docker-and-aws

# 7 - JENKINS BASICS + autorisations (HAM dossier utile)

# 8- 

## ********************************************************************************************************
## 1 - Créer et démarrer une machine virtuelle ubuntu 22.04
## ********************************************************************************************************
Créer et démarrer une machine virtuelle ubuntu 22.04

apt update
apt install openssh-server -y
mettre la machine en bridge
ip a
ssh eleve@IP

## ********************************************************************************************************
## 2 - Installer maven en local sur une vm ubuntu22.04: 
## ********************************************************************************************************

- https://phoenixnap.com/kb/install-maven-on-ubuntu



## ********************************************************************************************************
## 3 - Installer JAVA 17
## ********************************************************************************************************

  $ apt install fontconfig openjdk-17-jre -y
  $ java -version


## ********************************************************************************************************
## 4 - Installer JENKINS
## ********************************************************************************************************

  $ sudo wget -O /usr/share/keyrings/jenkins-keyring.asc \
    https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key
  $ echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] \
    https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
    /etc/apt/sources.list.d/jenkins.list > /dev/null 
  $ sudo apt update
  $ sudo apt install Jenkins -y
  $ systemctl status jenkins
  $ sudo systemctl enable jenkins
  $ sudo ufw allow 8080/tcp
  $ sudo ufw reload 
 ==> http://<public-ip-of-ubuntu-instance>:8080  
  $ sudo cat /var/lib/jenkins/secrets/initialAdminPassword 

Références : 
- https://medium.com/@ranjith_99360/how-to-install-jenkins-on-ubuntu-22-04-17b99fd41678
- https://medium.com/@cloudtechnet/how-to-install-jenkins-on-ubuntu-22-04-aws-ec2-instance-8234a096ffdb
- https://reintech.io/blog/installing-configuring-jenkins-ubuntu-22



## ********************************************************************************************************
## 5 -Pipeline complète avec MAVEN et JAVA installé en local 
## ********************************************************************************************************
- Jenkins Pipeline with Maven, SonarQube and Talisman | by Nandita Sahu | Medium 
⇒ 
- https://medium.com/@nanditasahu031/jenkins-pipeline-with-maven-sonarqube-and-talisman-fa9118910b98
 ou
- https://faun.pub/jenkins-pipeline-script-to-build-deploy-application-on-web-server-af55daf70c5a 


## ********************************************************************************************************
## 6 -ALLER PLUS LOIN
## ********************************************************************************************************

## —------------------------—-----------------------------------------------------------------------------------------
## 20 - Niveau 20 - ws-ec2-docker-and-aws-s3
## —------------------------—-----------------------------------------------------------------------------------------
- https://abhirajdevops.hashnode.dev/project-setting-up-a-cicd-pipeline-using-java-maven-junit-jenkins-github-aws-ec2-docker-and-aws-s3



## —------------------------—-----------------------------------------------------------------------------------------
## 30 - Niveau 30 - Simple CI/CD pipeline Integrating Jenkins with Maven and GitHub to Build a job on a Tomcat server.
## —------------------------—-----------------------------------------------------------------------------------------
- https://blog.devops.dev/simple-ci-cd-pipeline-integrating-jenkins-with-maven-and-github-to-build-a-job-on-a-tomcat-server-275e66a2e640



## —------------------------—-----------------------------------------------------------------------------------------
## 40 - Niveau 40 (BEST) - DevOps (Lab-3)-Building Jenkins pipelines with Maven & Tomcat
## —------------------------—-----------------------------------------------------------------------------------------
- https://aws.plainenglish.io/devops-lab-3-building-jenkins-pipelines-with-maven-tomcat-21494c413202




## —------------------------—-----------------------------------------------------------------------------------------
## 50 - Niveau 5 (NON) - VAGRANT
## —------------------------—-----------------------------------------------------------------------------------------

- https://faun.pub/jenkins-vagrant-automation-pt-1-adae0bdb69d6

 
# Projet complet
## Build a CI/CD Pipeline using Jenkins, SonarQube, Docker and AWS (hashnode.dev) 

- https://chirag0002.hashnode.dev/build-a-cicd-pipeline-using-jenkins-sonarqube-docker-and-aws
## Troubleshooting: 
- sudo adduser sonar
- sudo usermod -aG sudo sonar
- sudo chown -R sonar:sonar /home/ubuntu/sonarqube-10.0.0.68432
- sudo chown -R sonar:sonar /home/ubuntu
- sudo usermod -aG ubuntu sonar 
- (optionnel) sudo chmod 755 /home/ubuntu
- sudo su - sonar
- cd /home/ubuntu/sonarqube-10.0.0.68432/bin/linux-x86-64
- ./sonar.sh start


