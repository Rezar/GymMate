import bpy
import math

object = bpy.data.objects['Man Body.0']

# Calculate the center of the object
center = object.location

# Define camera positions (in this case, a circle around the object's center)
camera_positions = [(math.sin(math.radians(angle)) * 10, math.cos(math.radians(angle)) * 10, center.z) for angle in range(0, 360, 45)]

# Get the camera
camera = bpy.data.objects['Camera']

for i, position in camera_positions:
    # Move the camera to the position
    camera.location.x = position[0]
    camera.location.y = position[1]
    camera.location.z = position[2]

    # Point the camera towards the center of the character
    look_at = center - camera.location
    rot_quat = look_at.to_track_quat('-Z', 'Y')
    camera.rotation_euler = rot_quat.to_euler()

    # Set the render output path for each camera position
    bpy.context.scene.render.filepath = f'C:/Users/123/Downloads/output/render_{i}.mp4'
    
    # Render settings for video
    bpy.context.scene.render.image_settings.file_format = 'FFMPEG'
    bpy.context.scene.render.ffmpeg.format = 'MPEG4'
    bpy.context.scene.render.ffmpeg.codec = 'H264'

    # Render the animation from the current camera position
    bpy.ops.render.render(animation=True)