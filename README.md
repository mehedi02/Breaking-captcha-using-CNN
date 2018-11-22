# Breaking-captcha-using-CNN
---
# Dependency
1. keras
2. scikit-learn
3. imutils
4. matplotlib
5. numpy
6. cv2
7. requests

---

## To break the captchas with CNN, following steps are taken
1. Downloading a set of images.
2. Labeling and annotating your images for training.
3. Training a CNN on your custom dataset.
4. Evaluating and testing the trained CNN.
---

1. To automatically fetch new captcha images and save them to disk we use `download_images.py` , 
requests python package is needed, to install it ,insert following command:

$`pip install requests`

to run `download_images.py`  insert following command


$`python download_images.py --output downloads`



2. we can efficiently create out own dataset using openCV image processing techniques, to do it run `annotate.py` 

$`python annotate.py --input downloads --annot dataset`

when digits are shown corresponding key should be pressed

3. Training the captcha Breaker, by running

$ ` python train_model.py --dataset dataset --model output/lenet.hdf5`

4. to test the captcha Breaker

$`python test_model.py --input downloads --model output/lenet.hdf5`
