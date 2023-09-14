#!/usr/bin/env python
# coding: utf-8

# # Combine Images

# In[2]:


import cv2

def combine_and_resize_images(image1, image2, size):
    # Read the images
    image11 = cv2.imread(image1)
    image22 = cv2.imread(image2)

    # Resize both images to the target size
    image1_resized = cv2.resize(image11, size)
    image2_resized = cv2.resize(image22, size)

    # Combine the images horizontally (side by side)
    combined_image = cv2.hconcat([image1_resized, image2_resized])
    
    return combined_image

# Example usage
image1_path = "angel.jpg"
image2_path = "devil.jpg"

target_size = (200, 200)

combined_image = combine_and_resize_images(image1_path, image2_path, target_size)

# Display the combined and resized image
cv2.imshow("Combined and Resized Image", combined_image)

cv2.waitKey(0)
cv2.destroyAllWindows()


# # Swap Images

# In[3]:


import cv2

# Load the images
image1 = cv2.imread("angel.jpg")
image2 = cv2.imread("devil.jpg")

# Define the regions to be cropped and swapped
# Format: (startY:endY, startX:endX)
target_size = (500, 500)

# Resize image2 for consistency
image1 = cv2.resize(image1, (500, 500))
image2 = cv2.resize(image2, (500, 500))

# Swap the cropped regions
image2[250:, :500] = image1[250:, :500]
image1[200:250, :] = image2[200:250, :]

# Display the modified images
image1 = cv2.resize(image1, target_size)
image2 = cv2.resize(image2, target_size)

cv2.imshow('Image 1 with swapped region', image1)
cv2.imshow('Image 2 with swapped region', image2)

cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:




