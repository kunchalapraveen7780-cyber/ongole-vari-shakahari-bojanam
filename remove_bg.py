from PIL import Image

def remove_bg(input_path, output_path):
    try:
        img = Image.open(input_path).convert("RGBA")
        data = img.getdata()
        new_data = []
        
        # We assume background is the color of the top-left pixel
        bg_color = data[0]
        
        for item in data:
            # Calculate distance to background color
            dist = sum(abs(item[i] - bg_color[i]) for i in range(3))
            
            # If it's close to the background color (or very bright white/beige), make it transparent
            if dist < 60 or (item[0] > 230 and item[1] > 230 and item[2] > 220):
                new_data.append((255, 255, 255, 0))
            else:
                new_data.append(item)
                
        img.putdata(new_data)
        img.save(output_path, "PNG")
        print("Success")
    except Exception as e:
        print(f"Error: {e}")

remove_bg("logo.png", "logo-transparent.png")
