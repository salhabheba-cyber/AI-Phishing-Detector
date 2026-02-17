



Step 1: Create the Main Project Folder
On your computer, create a folder named:
AI-PhishDetect-2026

Step 2: Create All Subfolders
Inside AI-PhishDetect-2026, create these folders:
Folder Path	How to Create
src/	New folder
app/	New folder
tests/	New folder
samples/	New folder
screenshots/	New folder
Final Folder structure:
<img width="905" height="341" alt="01_folder_structure" src="https://github.com/user-attachments/assets/30904982-013c-455f-a75e-f1a786802a97" />



Step 3: Create Google Colab Notebook
stay in the main AI-PhishDetect-2026 folder on Google Drive
Click "+ New" → "More" → "Google Colaboratory"
rename the notebook:
Enable GPU (Important for speed): 
<img width="904" height="392" alt="02_gpu_enabled" src="https://github.com/user-attachments/assets/20a119f9-d4e5-463c-8167-a55300484114" />
Change runtime type
Under "Hardware accelerator" → Select "T4 GPU" 
Restart runtime to activate


Step 4: Mount Google Drive in Colab
In the first code cell of your notebook run:

python
# Cell 1: Mount Google Drive to access files
from google.colab import drive
drive.mount('/content/drive')


python
# Cell 2: Navigate to your project folder
import os
os.chdir('/content/drive/My Drive/AI-PhishDetect-2026')
!pwd


python
# Cell 3: Verify folder structure
!ls -la
Expected output: Shows your folders: detections, docs, tests, test_samples
<img width="589" height="331" alt="03_drive_mounted" src="https://github.com/user-attachments/assets/bdd84015-8de6-40f0-8758-779cc50f7b26" />


Step 5: Install Required Libraries
Create a new cell and run:

python
# Cell 4: Install all required packages
!pip install torch transformers gradio pandas numpy scikit-learn matplotlib seaborn
!pip install email-validator python-whois
Wait: This takes 2-3 minutes. You'll see many installation messages.

python
# Cell 5: Verify installations
import torch
import transformers
import gradio as gr

print(f"✅ PyTorch version: {torch.__version__}")
print(f"✅ Transformers version: {transformers.__version__}")
print(f"✅ Gradio version: {gr.__version__}")
print(f"✅ CUDA Available: {torch.cuda.is_available()}")
if torch.cuda.is_available():
    print(f"✅ GPU: {torch.cuda.get_device_name(0)}")
<img width="742" height="378" alt="04_dependencies_installed" src="https://github.com/user-attachments/assets/97a0a072-b3a2-46f8-b15d-de9c92125f4a" />


Step 6: Create classifier.py
<img width="570" height="370" alt="06_classifier_result" src="https://github.com/user-attachments/assets/18a70b5d-5988-41a3-b358-05e8e809b0a2" />


Step 7: Create app.py
<img width="766" height="383" alt="07_app_created" src="https://github.com/user-attachments/assets/b0e65f4f-c347-4311-9df8-f270ab271437" />

Step 8: Run the Gradio App
Run this cell:

python
# Cell 6: Launch Gradio web app
!python detections/phishing_detector/app.py
<img width="716" height="388" alt="07_app_ready_to_use" src="https://github.com/user-attachments/assets/5fab7bea-04e7-44da-abc0-29e7cef70a5f" />

Step 8: Go to Hugging Face
Open: huggingface.co
Login to your account (or create one for free)
create new space
Fill in Space Details
Upload these 3 files:
File 1: app.py
File 2: requirements.txt
File 3: README.md
Wait for Build

step 9 :Your App is Live!
Once built, your app will be at:....

check mine
https://huggingface.co/spaces/HEBA-cyber/Ai-phishing-detecting
<img width="788" height="410" alt="09_app_done" src="https://github.com/user-attachments/assets/f6bbedd9-bc01-4a67-8d30-c442d1b35f94" />

