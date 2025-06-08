import numpy as np
import matplotlib.pyplot as plt

def image_to_world(x_img, y_img):
    # Center the coordinates
    x_centered = (x_img - 128)
    y_centered = (128 - y_img)  # Invert y-axis
    
    # Calculate distance from center (for perspective correction)
    r = np.sqrt(x_centered**2 + y_centered**2)
    
    # Scale factor based on camera height and FOV
    base_scale = 0.619 / 256  # visible_width / image_width
    
    # Apply perspective correction
    perspective_factor = 1.0 + (r / 256) * 0.2
    
    # Transform to world coordinates
    x_world = x_centered * base_scale * perspective_factor
    y_world = y_centered * base_scale * perspective_factor
    
    return x_world, y_world

# Test data
image_coords = [
    (12, 75),    # Second largest disc
    (167, 65),   # Largest disc
    (169, 6),    # Smallest disc
]

world_coords = [
    (-0.100, 0.300),  # Second largest disc
    (-0.095, 0.149),  # Largest disc
    (0.275, 0.125),   # Smallest disc
]

# Test the transformation
transformed_coords = [image_to_world(x, y) for x, y in image_coords]

# Plot the results
plt.figure(figsize=(12, 6))

# Plot 1: Image coordinates
plt.subplot(121)
plt.scatter([x for x, _ in image_coords], [y for _, y in image_coords], c='blue', label='Image Points')
plt.axhline(y=128, color='r', linestyle='--', alpha=0.3)
plt.axvline(x=128, color='r', linestyle='--', alpha=0.3)
plt.grid(True)
plt.title('Image Coordinates')
plt.xlim(0, 256)
plt.ylim(256, 0)  # Invert y-axis to match image coordinates

# Plot 2: World coordinates
plt.subplot(122)
plt.scatter([x for x, _ in world_coords], [y for _, y in world_coords], c='blue', label='Actual World')
plt.scatter([x for x, _ in transformed_coords], [y for _, y in transformed_coords], c='red', label='Transformed')
plt.grid(True)
plt.title('World Coordinates')
plt.legend()

# Print numerical results
print("\nResults comparison:")
print("Point | Image Coords | Transformed World | Actual World | Error (m)")
print("-" * 70)
for i, ((img_x, img_y), (trans_x, trans_y), (world_x, world_y)) in enumerate(zip(image_coords, transformed_coords, world_coords)):
    error = np.sqrt((trans_x - world_x)**2 + (trans_y - world_y)**2)
    print(f"{i+1} | ({img_x:3d}, {img_y:3d}) | ({trans_x:6.3f}, {trans_y:6.3f}) | ({world_x:6.3f}, {world_y:6.3f}) | {error:.3f}")

plt.tight_layout()
plt.show() 