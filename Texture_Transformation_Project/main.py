import tkinter as tk
from PIL import Image, ImageTk
import numpy as np
import math

# Create window
root = tk.Tk()
root.title("Texture Transformation & Distortion Analyzer")
root.geometry("900x700")

# Load image
original_image = Image.open("texture.jpg")
original_image = original_image.resize((300, 300))
photo = ImageTk.PhotoImage(original_image)

image_label = tk.Label(root, image=photo)
image_label.pack(pady=20)

# --- Sliders ---

scale_slider = tk.Scale(root, from_=0.5, to=2.0, resolution=0.1,
                        orient=tk.HORIZONTAL, label="Scale")
scale_slider.set(1)
scale_slider.pack()

rotation_slider = tk.Scale(root, from_=0, to=360,
                           orient=tk.HORIZONTAL, label="Rotation (degrees)")
rotation_slider.set(0)
rotation_slider.pack()

# --- Matrix & Determinant Display ---

matrix_label = tk.Label(root, text="", font=("Arial", 12))
matrix_label.pack(pady=10)

det_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
det_label.pack()

# --- Function to Apply Transformation ---

def apply_transformation():
    scale = scale_slider.get()
    angle = math.radians(rotation_slider.get())

    # Transformation Matrix
    M = np.array([
        [scale * math.cos(angle), -scale * math.sin(angle), 0],
        [scale * math.sin(angle),  scale * math.cos(angle), 0],
        [0, 0, 1]
    ])

    # Calculate determinant
    determinant = np.linalg.det(M)

    # Update matrix display
    matrix_text = f"Transformation Matrix:\n{M}"
    matrix_label.config(text=matrix_text)

    det_label.config(text=f"Determinant: {round(determinant, 3)}")

    # Apply transformation visually (simplified)
    transformed = original_image.resize(
        (int(300 * scale), int(300 * scale))
    )

    transformed = transformed.rotate(rotation_slider.get())

    transformed_photo = ImageTk.PhotoImage(transformed)
    image_label.config(image=transformed_photo)
    image_label.image = transformed_photo


# Button
apply_button = tk.Button(root, text="Apply Transformation",
                         command=apply_transformation)
apply_button.pack(pady=20)

root.mainloop()