FROM sonarqube:latest
WORKDIR /opt
RUN wget https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-4.0.0.1744.zip
RUN unzip sonar-scanner-cli-4.0.0.1744.zip
RUN ls
RUN export PATH="/opt/sonar-scanner-4.0.0.1744/bin:$PATH"
CMD ["/opt/sonar-scanner-4.0.0.1744/bin/sonar-scanner"]