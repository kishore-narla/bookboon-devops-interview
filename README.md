# Task 1 (nginx-deploy.yaml) Solution
Added volumesMounts and volumes from container directory to hostpath dir


# Task 2 (cerebro-test.yaml) Solution

In Deployment resources the limit has to be maximum and request has to be minimum. 
Created new namspace and configmaps according to your requirements.
Image tag which you provided has , where in image tags contains '.'  lmenezes/cerebro:0.9.4
Replicaset has to be min of 1 so that it can create pod.
Image pull policy set to always.



# Task 3 (cerebro-test.yaml) Solution
created Nodeport service for the deployment and service manage the deployment by checking at matchlabels in deployment.
Nodeport service exposed to port and we can access the pod using any NODE public ip of cluster with port of svc.


# Task 4 Solution
written a basic docker image that prompts Bookboon test in logs.

# Task 5  Solution
We will first check if the number is divided by 10 if it perfectly divides then we will display the text or else display the number


