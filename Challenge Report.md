# Introduction
In this Segmentation challenge ([CHAOS19](https://chaos.grand-challenge.org/)[^1][^3]) the objective was to create a model capable of segmenting Liver, kidneys and spleen in the given dataset of biomedical images


# Architecture
I decided to use the the [U-net](https://arxiv.org/abs/1505.04597) to solve the task, since it is considered to be one of the best segmentation architecture in biomedicinal domain.
It is composed by:

1. <u>Encoder</u>: a downsampling path that consists of 4 blocks where each block applies two <font color="#0070c0">$3\times 3$ convolution</font> (+batch norm) followed by <font color="#c00000">$2\times 2$ max-pooling</font>. The number of features maps are doubled at each pooling layer (after each block) as 64 -> 128 -> 256 and so on;
2. <u>Bottleneck</u>: consists of two <font color="#0070c0">$3\times 3$ convolutions</font> followed by $2\times 2$ up-convolution;
3. <u>Decoder</u>: an  upsampling path, complimentary to the encoding, that consists of 4 blocks, where each block applies two $3\times 3$ convolution followed by <font color="#00b050">$2\times 2$ upsampling</font> (transposed convolution). The number of features maps are halved after every block

![unet](https://github.com/manuviani/CHAOS19_Biomedical_Segmentation_Challenge/blob/main/Images/unet.png)


# Preprocessing and Dataset [^2] Modification
I adopted a light preprocessing avoiding the voxel rescaling because it would be useless since the model was only fed 2D slices and not the whole 3D volume. 

After resizing every volume with its groundtruth mask to a $(256,256,z)$ shape (where $z$ is the number of slices) I changed the masks' classes to $[0,1,2,3,4]$, where $0$ is the background class and the others are the four organs.

Finally I "unpacked" the 3D volumes and masks and created `train` and `test` folders that contained every slice with its respective label (mask) both saved as `.png`

I used a $80:20$ split of the `T1DUAL`  for training and testing/validation. I didn't use the `T2SPIR` part of the datset since it was more difficult to distinguish organs from background. I decided to not use data augmentation since the dataset was big enough for the scope. 



# Training
I trained the model for 50 epochs optaining the following validation results:
- Epoch 1: ![epoch1](https://github.com/manuviani/CHAOS19_Biomedical_Segmentation_Challenge/blob/main/Images/epoch%201.png)

- Epoch 10: ![epoch10](https://github.com/manuviani/CHAOS19_Biomedical_Segmentation_Challenge/blob/main/Images/epoch%2010.png)
- Epoch 20: ![epoch20](https://github.com/manuviani/CHAOS19_Biomedical_Segmentation_Challenge/blob/main/Images/epoch%2020.png)
- Epoch 30: ![epoch30](https://github.com/manuviani/CHAOS19_Biomedical_Segmentation_Challenge/blob/main/Images/epoch%2030.png)
- Epoch 40: ![epoch40](https://github.com/manuviani/CHAOS19_Biomedical_Segmentation_Challenge/blob/main/Images/epoch%2040.png)
- Epoch 50: ![epoch50](https://github.com/manuviani/CHAOS19_Biomedical_Segmentation_Challenge/blob/main/Images/epoch%2050.png)

The following plot summarises training, validation loss and accuracy values:

![plot](https://github.com/manuviani/CHAOS19_Biomedical_Segmentation_Challenge/blob/main/Images/plot.png)


# Testing

In the testing phase I obtained the followig results:

1. ![test1](https://github.com/manuviani/CHAOS19_Biomedical_Segmentation_Challenge/blob/main/Images/test1.png)

2. ![test2](https://github.com/manuviani/CHAOS19_Biomedical_Segmentation_Challenge/blob/main/Images/test2.png)

3. ![test3](https://github.com/manuviani/CHAOS19_Biomedical_Segmentation_Challenge/blob/main/Images/test3.png)

4. ![test4](https://github.com/manuviani/CHAOS19_Biomedical_Segmentation_Challenge/blob/main/Images/test4.png)


# Conclusion
I'm satisfied with the outcome of the challenge. I think in the future it would be interesting to try implement a version of the Unet that takes the whole 3D volumes without slicing it and creates a 3D segmentation.

# References

[^1]: A.E. Kavur, N.S. Gezer, M. Barış, S. Aslan, P.-H. Conze, et al. "CHAOS Challenge - combined (CT-MR) Healthy Abdominal Organ Segmentation",  Medical Image Analysis, Volume 69, 2021. https://doi.org/10.1016/j.media.2020.101950

[^2]: A.E. Kavur, M. A. Selver, O. Dicle, M. Barış,  N.S. Gezer. CHAOS - Combined (CT-MR) Healthy Abdominal Organ Segmentation Challenge Data (Version v1.03) [Data set]. Apr.  2019. Zenodo. http://doi.org/10.5281/zenodo.3362844


[^3]: A.E. Kavur, N.S. Gezer, M. Barış, Y.Şahin, S. Özkan, B. Baydar, et al.  "Comparison of semi-automatic and deep learning-based automatic methods for liver segmentation in living liver transplant donors", Diagnostic and  Interventional  Radiology,  vol. 26, pp. 11–21, Jan. 2020. https://doi.org/10.5152/dir.2019.19025