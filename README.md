This is a simple project for automation to Release Elastic public ip in AWS that are unused.
If EIP are not deleted after instances are deleted, they remain unused and can increase unnecessary cost if they are not released.

In this simple python script i used boto3 module and tried to release ips that are not allocated to any instance.

To tun this script:

1. If you are running the script in AWS instance, add permission to the role and then execute it.

2. If you are using local machine to run,
   1. create a IAM user,
   2. go to its dashboard,
   3. create an access key,
   4. then install aws cli,
   5. use command `aws configure`,
   6. and pass iin the keys and defaullt region

3. Make sure python3 is installed by running command `python3` in terminal.
4. Run 'pip install boto3' for boto3 module
5. siimply run the script using `python3 <script-name>`

You can also use Aws Lambda to run this script, 
  1. simply create a lambda function,
  2. paste the code in the function,
  3. give the roles the 'ec2fullaccess' permission and
  4. run it,
note: you can aslo make the script run automatically after certain period of time.

The goal of the automation is to reduce the cost that can be added if proper usage and deletion after usecase is over is not done..
The costs for unnecessary resources and services usage can pile up quickl and using this script as cron job or lambda, we can reduce those costs.

Thanks for checking out the project, comment if you have any suggestions for me :)

