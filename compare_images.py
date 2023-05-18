import tensorflow as tf
import matplotlib.pyplot as plt
def compare_images(image_path1, image_path2):
    # Load images
    image1 = tf.io.read_file(image_path1)
    image1 = tf.image.decode_image(image1, channels=3)
    image1 = tf.image.resize(image1, (224, 224))  # Resize if needed

    image2 = tf.io.read_file(image_path2)
    image2 = tf.image.decode_image(image2, channels=3)
    image2 = tf.image.resize(image2, (224, 224))  # Resize if needed

    # Normalize pixel values
    image1 = image1 / 255.0
    image2 = image2 / 255.0

    # Compute similarity
    similarity = tf.image.ssim(image1, image2, max_val=1.0)

    return similarity.numpy()

# Paths to the two images you want to compare
image_path1 = 'D:\WillR\Pictures\Test-Image 1-Desk-Base.jpg'
image_path2 = 'D:\WillR\Pictures\Test-Image 1-Desk-Flipped.jpg'

similarity_percentage = compare_images(image_path1, image_path2) * 100
print(f"Similarity Percentage: {similarity_percentage}%")

fig, (ax1,ax2) = plt.subplots(1,2, figsize=(10,5))

ax1.imshow(plt.imread(image_path1))
ax1.set_title("Image 1")

ax2.imshow(plt.imread(image_path2))
ax2.set_title("Image 2")

plt.text(0.5, 0.05, f"Similarity: {similarity_percentage:.2f}%", 
         fontsize=12, ha='center', transform=fig.transFigure)

# Adjust layout and display the plot
plt.tight_layout()
plt.show()