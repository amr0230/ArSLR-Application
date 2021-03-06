# ArSLR-Application
> ArSLR Application  ==>  Arabic Alphabet Sign Language Recognition Based on Machine Learning Methods

# Abstract

> There are several groups in society that have different disabilities, such as deaf and dumb groups, that cannot communicate freely with others. The world of deaf and dumb, a world not far away from us but a mysterious world not known to many, and although they are among us, the misperception of society about their world, their movements and body language among them, signs and symbolic expressions that few people understand and are unknown by many people, have led them to isolate themselves from people. So, the main objective of the associations and institutions that sponsor these groups is how to integrate them into society. Therefore, the development of a computerized system that analyzes deaf and dumb signals will help this group and ordinary people to communicate.

> My project aims to recognize the gestures of the 28 characters of the Arabic alphabet. The development and implementation of the proposed system are generally based on two main phases that includes: preprocessing and extracting the necessary features using a machine learning algorithm, which will be used to perform the classification process. In this project, I proposed to use the Support Vector Machine (SVM) and the K-Nearest Neighbors (KNN) classifiers to classify and recognize the gestures of the 28 Arabic letters.
In total, around 14,000 samples of the 28 Arabic alphabetic signs have been used after resizing for the learning and testing phases. The classification process was conducted using a SVM and KNN and achieved an overall accuracy of 89.29% and 83.57% respectively, showing that the results of SVM outperformed those results obtained by KNN. This model also achieved a sensitivity of 89% and 84% for the SVM and KNN respectively.

# Project Objectives:
> - To develop an intelligent computerized system that addresses the problem of ArSLR and based on machine learning algorithms, such as SVM and KNN algorithms.
> - To help people with disabilities such as deaf and dumb to communicate with ordinary people easily and freely, and vice versa.

# Dataset
> The first step is to collect dataset for the 28 Arabic alphabet signs. We need a lot images for each alphabet, this dataset is somewhat hard to collect but thank for University Malaysia Sarawak, Prince Mohammad Bin Fahd University for their dataset. They made a fully labeled dataset consists of 54,049 images of ArSLR alphabets performed by more than 40 volunteers for 32 standard Arabic signs and alphabets (as shown in the picture below).

![image](https://user-images.githubusercontent.com/65462055/169630880-592dc17a-84fb-4d86-8f01-7449dbe24908.png)

# Coding Programming Languages

> To develop this system, I have used the Python programming language. In particular, the system uses Python to read and prepare the image, and I used Python to design system tasks such as logging into the system.

> Important Python libraries needed to operate this system:
> - NumPy
> - Scikit-Learn
> - Matplotlib
> - OpenCV
> - Joblib
> - Random
> - Tkinter
> - PIL
> - Time
> - Pymysql

> I used XAMPP that is one of the widely used cross-platform web servers, to help a local host or server to test its website and clients via computers and laptops before releasing it to the main server. It is a platform that furnishes a suitable environment to test and verify the working of projects based on Apache, Perl, MySQL database, and PHP through the system of the host itself.

# System Interfaces

> ## Login Interface:

![Login](https://user-images.githubusercontent.com/65462055/169636082-267f3e6f-92cd-4117-bd26-0291dcdaa20a.png)

> ## Registration Interface:

![Registration](https://user-images.githubusercontent.com/65462055/169636111-7744c23d-327d-4efd-a2ed-6139edc92a7e.png)

> ## Hand Sign Recognition Interface:

![Applicaiton_Interface](https://user-images.githubusercontent.com/65462055/169636173-155ac464-3ae4-4560-8b70-4142382837eb.png)

![Predict](https://user-images.githubusercontent.com/65462055/169636175-78b18bc6-3fad-4696-8fba-cb0772f5d802.png)

> ## User Management System Interface:

![UMS](https://user-images.githubusercontent.com/65462055/169636218-8d7e5ff4-91a8-46ba-9b3d-6ac1de95dc9e.png)

> ## Forget Passwrod Interface:

![ForgetPW](https://user-images.githubusercontent.com/65462055/169636260-e9fae786-6fd6-4776-ba5c-425f4291ca59.png)

# Conclusion:

> This proposed system has been presented, described and evaluated successfully. After developing its functions, we conclude that it satisfies the requirements and the objectives correctly as intended. And accordingly we have some observations concerning algorithms that we have used, we have used Support Vector Machine (SVM) and K-Nearest Neighbors (KNN) algorithms. In this case we have found that the overall classification results using SVM is 89%, while the overall classification results using KNN is 84% (as shown in the picture below).

![image](https://user-images.githubusercontent.com/65462055/169636394-c07a4965-0954-4731-9b90-3387ebf95ff0.png)

> It underlines that the SVM classifier obtains more accurate results than KNN. It demonstrates that the non-linear classifier (SVM) has significantly played an important role in computing and improving the linear separation between the gestures of the Arabic language characters. 



