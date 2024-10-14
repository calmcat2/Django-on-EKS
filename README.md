# Django-on-EKS
This is the Kubernetes version of the Django restaurant system developed in the repository [here](https://github.com/calmcat2/littlelemon/tree/v1).

## Repository Structure
`/app`: Contains files necessary for creating a Docker image of the application.

`/IAM`: Includes IAM policy files required for the EKS cluster.

`/yml-files`: Contains YAML files for deploying the application on Amazon EKS.

`/DB-dumps`: Stores MySQL database dumps.

## Deployment
For detailed instructions on deploying the EKS environment, refer to this [blog](https://www.maxinehe.top/2024/10/05/Django-eks/) post.

### Deployment Order
The recommended order for deploying YAML files is:
1. DB
2. EFS
3. Django-app
4. Nginx
5. Ingress

### Pre-deployment Configuration
Before applying the YAML files, ensure the following configurations are set:
#### **1. Django Configuration**
- Modify `yml-files/Django-app/django-config.yml` for Django server customization. Adjust ALLOWED_HOSTS and CSRF_TRUSTED_ORIGINS as needed.
#### **2. Persistent Volume Configuration**
- Update `VolumeHandle` with your EFS ID in `yml-files/Django-app/staticfiles-pv.yml`.
- Modify `yml-files/Django-app/staticfiles-pv.yml` and `yml-files/DB/mysql-pv.yml` to match your storage requirements.
#### **3. MySQL Configuration**
- Update the database ARN in `rds.yml`.
- Change `objectName` in `secretprovider.yml` to match your database secret name.
#### **4. Ingress Configuration**
- Modify `Ingress.yml` rules and tls.hosts as necessary.
### **Additional Notes**
- Ensure all necessary dependencies are installed before deployment.
- Review and test configurations in a staging environment before deploying to production.
- Regularly update and maintain your EKS cluster and application for security and performance.
