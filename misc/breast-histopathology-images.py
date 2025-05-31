import os
import glob
import sys

def _count_dataset_images(root_path):
    total_count = 0
    counts_per_dataset = {}

    # 1. breast-histopathology-images
    # Path: <root_path>/breast-histopathology-images/**/*.png
    dataset1_name = 'breast-histopathology-images'
    path1 = os.path.join(root_path, dataset1_name)
    current_dataset_count = 0
    if os.path.exists(path1):
        pattern1 = os.path.join(path1, '**', '*.png')
        files1 = glob.glob(pattern1, recursive=True)
        current_dataset_count = len(files1)
        print(f"Found {current_dataset_count} images in {path1}")
    else:
        print(f"Directory not found: {path1}")
    total_count += current_dataset_count
    counts_per_dataset[dataset1_name] = current_dataset_count

    # 2. MINI-DDSM-Complete-PNG-16
    # Path: <root_path>/MINI-DDSM-Complete-PNG-16/[Benign|Cancer]/<4 digits number>/<image name.png>
    dataset2_name = 'MINI-DDSM-Complete-PNG-16'
    path2_base = os.path.join(root_path, dataset2_name)
    current_dataset_count = 0
    if os.path.exists(path2_base):
        # Count Benign
        pattern2a = os.path.join(path2_base, 'Benign', '????', '*.png') # Assuming .png extension
        files2a = glob.glob(pattern2a)
        current_dataset_count += len(files2a)
        print(f"Found {len(files2a)} images in {os.path.join(path2_base, 'Benign', '????')}")
        
        # Count Cancer
        pattern2b = os.path.join(path2_base, 'Cancer', '????', '*.png') # Assuming .png extension
        files2b = glob.glob(pattern2b)
        current_dataset_count += len(files2b)
        print(f"Found {len(files2b)} images in {os.path.join(path2_base, 'Cancer', '????')}")
    else:
        print(f"Directory not found: {path2_base}")
    total_count += current_dataset_count
    counts_per_dataset[dataset2_name] = current_dataset_count
    
    # 3. cbis-ddsm-breast-cancer-image-dataset
    # Path: <root_path>/cbis-ddsm-breast-cancer-image-dataset/jpeg/<name like ...>/<imagename.jpg>
    dataset3_name = 'cbis-ddsm-breast-cancer-image-dataset'
    path3_base = os.path.join(root_path, dataset3_name, 'jpeg')
    current_dataset_count = 0
    if os.path.exists(path3_base):
        pattern3 = os.path.join(path3_base, '*', '*.jpg') # Assuming .jpg extension
        files3 = glob.glob(pattern3)
        current_dataset_count = len(files3)
        print(f"Found {current_dataset_count} images in {path3_base}")
    else:
        print(f"Directory not found: {os.path.join(root_path, dataset3_name, 'jpeg')} (or {os.path.join(root_path, dataset3_name)} is missing)")
    total_count += current_dataset_count
    counts_per_dataset[dataset3_name] = current_dataset_count

    print("\nSummary of counts per dataset:")
    for name, count in counts_per_dataset.items():
        print(f"- {name}: {count}")
    print("---")
    return total_count

def count_images_local(root_dir):
    print(f"Counting local images from root directory: {root_dir}")
    return _count_dataset_images(root_dir)

def count_images_gdrive(root_dir):
    print(f"Counting Google Drive images from root directory: {root_dir}")
    return _count_dataset_images(root_dir)

def is_on_gdrive():
    # Check if running in Google Colab or if /drive exists
    return os.path.exists('/content/drive') or os.path.exists('/drive')

def main():
    # Define root paths for datasets. 
    # These paths should be the PARENT directory of 
    # 'breast-histopathology-images', 'MINI-DDSM-Complete-PNG-16', etc.
    local_datasets_root = os.getcwd() 
    # Example: If script is in /Projects/cnn-pytorch-breastcancer, and datasets are in 
    # /Projects/cnn-pytorch-breastcancer/breast-histopathology-images, etc.
    
    gdrive_datasets_root = '/content/drive/My Drive/dl-udemy' 
    # Example: Parent folder on GDrive containing the dataset folders.

    if is_on_gdrive():
        print(f"Detected Google Drive environment. Using root for datasets: {gdrive_datasets_root}")
        if not os.path.exists(gdrive_datasets_root):
            print(f"Google Drive datasets root path not found: {gdrive_datasets_root}")
            print("Please ensure Google Drive is mounted and the path is correct.")
            count = 0
        else:
            count = count_images_gdrive(gdrive_datasets_root)
        print(f"\nTotal images found across all datasets in Google Drive: {count}")
    else:
        print(f"Google Drive not detected. Using local root for datasets: {local_datasets_root}")
        if not os.path.exists(local_datasets_root):
            print(f"Local datasets root path not found: {local_datasets_root}")
            print("Ensure the script is run from the correct directory or adjust 'local_datasets_root'.")
            count = 0
        else:
            count = count_images_local(local_datasets_root)
        print(f"\nTotal images found across all local datasets: {count}")

if __name__ == '__main__':
    main()

# Total images locally: 555048 (This comment might need updating after running the new script)