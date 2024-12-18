<h1 align="center"> 🔑 Password Manager - Tkinter GUI </h1>

In this project, we create a password manager via **Tkinter**. The program expects three entries from the user, those are 
respectively:

* Website name
* Email or username
* Password (optional)

Password is an optional entry that can be generated by the program(By clicking on the `Generate Password` button). 
After filling entries, the user can click the `Save & Encrypt` button to save it in a txt file called **data.txt**.

To reach out the encrypted data, the user can copy and paste the info on the referring entry and click on the 
`Load & Decrypt` button.

Required modules for this project are:

* **tkinter**
* **random**

<hr>

<h2> How does it work?</h2>

This is how our program looks like:

The app expects the user to fill in the `Website`, `Email/Username`, and the `Password` respectively.

![Screenshot_password_manager](https://github.com/Trigenaris/password-manager-GUI/assets/122381599/3f068c62-8254-4d0d-af50-ac7037d1e1f4)

Firstly the user fills in the `Website` and the `Email/Username` entries as shown:

![Screenshot_password_manager1](https://github.com/Trigenaris/password-manager-GUI/assets/122381599/404f0720-d06e-414c-88fa-fc147f87d022)

Secondly, the user can either fill in the `Password` or click on the `Generate Password` button and then, click the `Save & Encrypt` button:

![Screenshot_password_manager2](https://github.com/Trigenaris/password-manager-GUI/assets/122381599/18aa3374-bc4a-4cc8-9c66-315d72fa51bc)

As the user clicks the button, they get a 'askyesno' message box:

![Screenshot_password_manager3](https://github.com/Trigenaris/password-manager-GUI/assets/122381599/61fb4680-3244-42f9-a067-25e09ccb5c86)

After the saving process, the user gets feedback and their email remains in the entry box:

![Screenshot_password_manager4](https://github.com/Trigenaris/password-manager-GUI/assets/122381599/4b221ede-52d0-4ff1-afc0-58ff5642fa91)

The saved information is stored in `data.txt` file:

![Screenshot_password_manager5](https://github.com/Trigenaris/password-manager-GUI/assets/122381599/bfa79731-3487-4645-93b1-048fd4b53283)

The user can enter the **encrypted data** in the related entry boxes and click the `Load & Decrypt` button to **decrypt** the data:

![Screenshot_password_manager6](https://github.com/Trigenaris/password-manager-GUI/assets/122381599/ef4dccca-7f05-4e1b-893c-d31576041b86)

As the user attempts to decryption, another message box is shown:

![Screenshot_password_manager7](https://github.com/Trigenaris/password-manager-GUI/assets/122381599/2a2393fc-fa32-4705-8d39-67f655d7887e)

Finally, the user reaches their email and password:

![Screenshot_password_manager8](https://github.com/Trigenaris/password-manager-GUI/assets/122381599/12ce7ac7-e680-4232-9316-f5d30049cc73)





