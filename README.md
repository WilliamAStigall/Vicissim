# Vicissim
Image Recognition System
A more detailed explanation is in the Base Idea docx

This project contains a scene comparison model, which is designed to compare the degree of similarity between two new images
The purpose of this comparison model is to save memory, when we are sending objects in fro reference, we risk overloading the system if there is
not a way to determine whether the last x amount of frames are similar.

This project contains an object detection model, built or rather stripped from the Yolov7 model, I removed the classification feature
because it does not contain all the necessary classes, and its functionality is slightly different than what I am looking for

This project contains a classification model, built not on ImageNet but a self creating database leveraging Natural Language Processing 
and google images, the NLP is used to translate image descriptions to probable item classifications and building the dataset from there.
This is the most ambitous part of the project, to see if we can remove the need to human labeled images.

One pontential issue would be if there was an object that does not exist and therefore a image search of it would return nothing,
although this would not help in the human interpretation I believe it would be possible to give it an ID that the machine can use to recognize
it if there are more future occurences.
