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
<img width="905" height="341" alt="01_folder_structure" src="https://github.com/user-attachments/assets/77a5d6af-2c00-4ce9-8e5f-a5da34fae585" />


Step 3: Create Google Colab Notebook
stay in the main AI-PhishDetect-2026 folder on Google Drive
Click "+ New" → "More" → "Google Colaboratory"
rename the notebook:
Enable GPU (Important for speed):<img width="904" height="392" alt="02_gpu_enabled" src="https://github.com/user-attachments/assets/20a119f9-d4e5-463c-8167-a55300484114" />
Change runtime type
Under "Hardware accelerator" → Select "T4 GPU" 
Restart runtime to activate


Step 1.3: Mount Google Drive in Colab
In the first code cell of your notebook, paste and run:

python
# Cell 1: Mount Google Drive to access files
from google.colab import drive
drive.mount('/content/drive')
What happens: A link appears. Click it, choose your Google account, copy the authorization code, paste back in Colab, press Enter .

Expected output: Mounted at /content/drive

python
# Cell 2: Navigate to your project folder
import os
os.chdir('/content/drive/My Drive/AI-PhishDetect-2026')
!pwd
Expected output: /content/drive/My Drive/AI-PhishDetect-2026

python
# Cell 3: Verify folder structure
!ls -la
Expected output: Shows your folders: detections, docs, tests, test_samples

📸 SCREENSHOT #3: Drive Mounted
When: After running Cell 3

