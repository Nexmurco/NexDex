import curses
from PIL import Image

class ImageHandler:
    def prep_palettes(menu, image_data):
            
        palette = image_data["palette"]
        png_term_color_dict = {}
        color_pair_dict = {}

        #add all colors from png and track them in palette_dict
        for key in palette.keys():
            r = palette[key][0]
            g = palette[key][1]
            b = palette[key][2]

            new_color = ImageHandler.convert_color_and_init(menu, r, g, b)
            png_term_color_dict[key] = new_color

        
        image = image_data["image"]
        for col in range(len(image)):
            for row in range(len(image[col])):
                color_pair = image[col][row]
                #if dict does not contain the color, add it to the list
                if not color_pair_dict.get(color_pair):
                    #make a new color pair

                    #assign it a number based on the dict size + 2
                    
                    color_pair_number = menu.initialized_color_pairs
                    menu.initialized_color_pairs += 1
                    curses.init_pair(color_pair_number, png_term_color_dict[color_pair[0]], png_term_color_dict[color_pair[1]])
                    color_pair_dict[color_pair] = color_pair_number
                #palette_dict contains the color, then skip

        return color_pair_dict

    @staticmethod
    def print_image(menu, color_pair_dict, image_data, x_offset = 0, y_offset = 0):
        image = image_data["image"]
        for col in range(len(image)):
            for row in range(len(image[col])):
                pixel_pair = image[col][row]
                color_code = color_pair_dict[pixel_pair]
                menu.print_string(y_offset + row,x_offset + col, "▀", color_code)

    @staticmethod
    def print_file(menu, file_name):
        image_data = ImageHandler.prep_image_data(file_name)
        ImageHandler.output_image(image_data)
        ImageHandler.output_palette(image_data)

        color_pair_dict = ImageHandler.prep_palettes(menu, image_data)
        ImageHandler.print_image(menu, color_pair_dict, image_data)


        #take palette and initialize or overwrite color pairs using ex. curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
        #go through line by line and print the pokemon!

    @staticmethod
    def prep_image_data(file_name):
        image_data = {}
        image = Image.open("Images\\" + file_name)
        pixels = image.load()
        image_palette = image.getpalette()
        palette = {}

        for i in range(0,round(len(image_palette)/3)):
            palette[i] = image_palette[i*3:i*3+3]

        image_data["palette"] = palette

        paired_rows = []
        for row in range(0, image.height, 2):
            new_row = []
            if(row+1 < image.height):
                for col in range(0, image.width):
                    new_row.append((pixels[col, row], pixels[col, row+1]))
            else:
                for col in range(0,image.width):
                    row.append((pixels[col, row], 0))
            paired_rows.append(new_row)

        image_data["image"] = paired_rows

        return image_data
    
    @staticmethod
    def output_palette(image_data):
        palette = image_data["palette"]
        with open("Output\\output_palette.txt", "w") as f:
            for key in palette.keys():
                f.write(f"{key}: {palette[key]}")
                f.write("\n")

    @staticmethod
    def output_image(image_data):
        image = image_data["image"]
        with open("Output\\output_image.txt", "w") as f:
            for col in range(len(image)):
                for row in range(len(image[col])):
                    f.write(f"{image[col][row]} ")
                f.write("\n")

    @staticmethod
    def convert_color_and_init(menu, r, g, b):
        # convert 0-255 range to 0-1000 range
        r_1000 = round(r * 1000 / 255)
        g_1000 = round(g * 1000 / 255)
        b_1000 = round(b * 1000 / 255)

        # need to deal with 255 color limit, overwrite instead of append in future
        
        curses.init_color(menu.initialized_colors, r_1000, g_1000, b_1000)
        new_color_id = menu.initialized_colors
        menu.initialized_colors += 1

        return new_color_id