# import the alternat library
# from alternat.collection import Collector
from alternat.generation import Generator
from bs4 import *
import requests
import os

def img_list(img_folder):

    img_list = []

    # list files in img directory
    img_folder = img_folder.replace('/','-_-')
    path = f"static/images/{img_folder}"
    files = os.listdir(path)

    for file in files:
        # make sure file is an image
        if file.endswith(('.jpg', '.png', 'jpeg')):
            img_path = path + file
            img_list.append(img_path)
            
    return img_list


# CREATE FOLDER
def folder_create(url , images):
    try:
        url = url.replace('/','-_-')
        folder_name = f"static/images/{url}"
		# folder creation
        os.mkdir(folder_name)

	# if folder exists with that name, ask another name
    except:
        print("Folder Exist with that name!")

	# image downloading start
    download_images(images, folder_name)


# DOWNLOAD ALL IMAGES FROM THAT URL
def download_images(images, folder_name):

	# initial count is zero
	count = 0

	# print total images found in URL
	print(f"Total {len(images)} Image Found!")

	# checking if images is not zero
	if len(images) != 0:
		for i, image in enumerate(images):
			# From image tag ,Fetch image Source URL

						# 1.data-srcset
						# 2.data-src
						# 3.data-fallback-src
						# 4.src

			# Here we will use exception handling

			# first we will search for "data-srcset" in img tag
			try:
				# In image tag ,searching for "data-srcset"
				image_link = image["data-srcset"]
				
			# then we will search for "data-src" in img
			# tag and so on..
			except:
				try:
					# In image tag ,searching for "data-src"
					image_link = image["data-src"]
				except:
					try:
						# In image tag ,searching for "data-fallback-src"
						image_link = image["data-fallback-src"]
					except:
						try:
							# In image tag ,searching for "src"
							image_link = image["src"]

						# if no Source URL found
						except:
							pass

			# After getting Image Source URL
			# We will try to get the content of image
			try:
				r = requests.get(image_link).content
				try:

					# possibility of decode
					r = str(r, 'utf-8')

				except UnicodeDecodeError:

					# After checking above condition, Image Download start
					with open(f"{folder_name}/images{i+1}.jpg", "wb+") as f:
						f.write(r)

					# counting number of image downloaded
					count += 1
			except:
				pass

		# There might be possible, that all
		# images not download
		# if all images download
		if count == len(images):
			print("All Images Downloaded!")
			
		# if all images not download
		else:
			print(f"Total {count} Images Downloaded Out of {len(images)}")

# MAIN FUNCTION START
def img_scraper(url):

	# content of URL
	r = requests.get(url)

	# Parse HTML Code
	soup = BeautifulSoup(r.text, 'html.parser')

	# find all images in URL
	images = soup.findAll('img')

	# Call folder create function
	folder_create(url, images)

# def img_collector(
#     url,
#      download_recursive = False,
#      collect_using_apify = True
# ):

#     output_dir_path = f"static/output/{url}"

#     # instantiate the collector
#     collector = Collector()

#     # Download images from url and saves image files in  output_dir_path
#     # Optional parameters, download_recursive if True crawls whole site mentioned in
#     # url by visiting each link recursively and downloads images
#     # collect_using_apify in future more crawlers will be supported this parameter
#     # ensures that apify crawler is used.
#     collector.process(url, output_dir_path, download_recursive, collect_using_apify)

def alt_text_generator(img_path):

    result_dir_path = "static/result/"

    # instantiate the generator for Opensource OCR
    generator = Generator()

    #To configure the generator
    generator_config = {
        "DEBUG": True, 
        "ENABLE_OCR_CLUSTERING": False
        }
    generator.set_config(generator_config)

    # generate alt text from file (file at location sample/images_with_text/sample1.png
    # and results saved at location folder results)
    generator.generate_alt_text_from_file(img_path , result_dir_path)

if __name__ == '__main__':
    url = "https://css-tricks.com/using-artificial-intelligence-to-generate-alt-text-on-images/"
    img_scraper(url)
    img_list = img_list(url)
    for img in img_list:
        alt_text_generator(img)