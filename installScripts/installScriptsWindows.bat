@setlocal enableextensions
@cd /d "%~dp0"
echo Make sure you have installed Anaconda, git, Node.js and npm.
pause
cd ..
echo Installing jupyterlab ...
conda install -c conda-forge jupyterlab
echo Installing ipywidgets. Enter 'y' when prompted to install ...
conda install -c conda-forge ipywidgets
echo Installing labextension ...
jupyter labextension install @jupyter-widgets/jupyterlab-manager@0.38
echo Installing AISpace2 library ...
pip install -e .
pip install -r requirements-dev.txt
cd js
npm install
npm run update-lab-extension
jupyter labextension install
cd ..
jupyter lab