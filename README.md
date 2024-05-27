# SkinDB
A template to store your minecraft skins in a web provider

## How to use
1. Generate a repository from this template
2. Upload your skins in the skins folder
3. In your hosting provider panel, set the generation commands to `python3 -m pip install -r requirements.txt` and `python3 generate.py`
4. In your hosting provider panel, set the output directory to the root directory

## Vercel deployment guide
1. Create a new project from your generated repository
2. Set the install command to `python3 -m pip install -r requirements.txt`
3. Set the build command to `python3 generate.py`
4. Set the output directory to `.`
5. Deploy