import requests
from tqdm import tqdm

def download_file_with_progress(url, destination):
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))

    with open(destination, 'wb') as file, tqdm(
            desc=destination,
            total=total_size,
            unit='B',
            unit_scale=True,
            unit_divisor=1024,
    ) as bar:
        for data in response.iter_content(chunk_size=1024):
            size = file.write(data)
            bar.update(size)

    print(f"Download successful. File saved to {destination}")

def show_menu(model_links, model_names):
    print("Choose models to download (enter model numbers separated by commas):")
    for i, link in enumerate(model_names, 1):
        print(f"{i}. Model " + model_names[i - 1])

    choices = input("Enter model numbers (e.g., 1, 3, 5): ")
    try:
        choices = [int(choice) for choice in choices.split(',')]
    except ValueError:
        print("Invalid input. Please enter numbers separated by commas.")
        return

    for choice in choices:
        if 1 <= choice <= len(model_names):
            url = model_links[choice - 1]
            destination = f"models/" + model_names[choice - 1]

            download_file_with_progress(url, destination)
        else:
            print(f"Invalid choice: {choice}. Skipping.")

if __name__ == "__main__":
    model_links = [
        "https://huggingface.co/TheBloke/LLaMA-13b-GGUF/blob/main/llama-13b.Q4_K_M.gguf",
        "https://huggingface.co/TheBloke/LLaMA-7b-GGUF/blob/main/llama-7b.Q5_K_M.gguf",
    ]

    model_names = [
        "llama-13b.Q4_K_M.gguf",
        "llama-7b.Q5_K_M.gguf"
    ]

    show_menu(model_links, model_names)