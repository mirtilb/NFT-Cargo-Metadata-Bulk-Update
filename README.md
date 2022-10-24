# NFT-Cargo-Metadata-Bulk-Update</br>

Goal        		A solution to update all collectibles at once with a CSV including URL + metadata</br>
Project			No More TV (NMTV)</br>
Developer		syed_aj</br>
			https://github.com/SyedAzeemJaved</br>
			https://www.fiverr.com/syed_aj</br>
-------------------------------------------------------------------------------------

<strong>HOW IT WORKS</strong>

FIRST
install chromedriver + fill provided .xlsx including</br>
A/ collectibles link in dashboard </br>
B/ metadata </br>
... backup everything first (you should have done that before minting NFTs anyway).</br>
</br>
<strong>STEPS:</strong></br>
01. Command: go to the bot folder 
02. Execute the 'main.py' file in Python (command: python3 main.py)
03. Wait for Chrome Driver to launch.
04. Terminal will be waiting for you to login to the website by prompting "Press 'Y' to continue", so kindly login using your preferred method.
05. The above step has been done to ensure privacy, so that no passwords and credentials are stored on disk.
06. While logging in make sure that cargo.build window (1st tab) is not closed and open.
07. After logging in press 'Y' and enter on the terminal, to let the code know.
08. Once that is done, bot will start reading rows from 'data.xlsx' and edit their metadata(s).

PS: "attribute" format is needed to set variations on OPENSEA.
