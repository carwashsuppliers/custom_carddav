# Custom CardDAV Module for Odoo

## Overview
This repository contains a custom CardDAV module for Odoo, designed to integrate CardDAV functionality into your Odoo instance.

## Deployment Instructions
### Using Odoo.sh Submodule WebUI
To deploy this module using Odoo.sh, follow these steps:

1. **Create a Development Branch**
   - Navigate to your Odoo.sh project.
   - Create a new branch from `production/main` named `dev`.

2. **Add the Submodule**
   - In the Odoo.sh WebUI, click on the **Submodule** button.
   - Paste the SSH clone URL from this repository (`git@github.com:carwashsuppliers/custom_carddav.git`).
   - Click **Install**.

3. **Test in Development**
   - Wait for the deployment to complete.
   - Log into your Odoo instance in **Development Mode** and verify the module is installed correctly.

4. **Move to Staging**
   - If testing is successful, merge the `dev` branch into `staging`.
   - Perform additional testing if required.

5. **Merge with Main (Production)**
   - If everything works correctly in staging, merge `staging` into `main` to deploy to production.

## Installation Instructions
1. **Enable Developer Tools** (Admin User Required)
   - Log in to your Odoo instance (`www.carwashsuppliers.com`).
   - Navigate to **Settings**.
   - Enable **Developer Tools**.

2. **Update App List and Install the Module**
   - Go to **Apps**.
   - Click **Update Apps List**.
   - Search for `custom_carddav`.
   - Click **Install**.

## iOS Configuration for CardDAV
Once the module is installed and configured, users can set up their CardDAV accounts on iOS devices:

1. **Open Settings on iOS Device**
   - Navigate to **Passwords & Accounts**.
   - Select **Add Account**.
   - Choose **Other**.
   - Select **Add CardDAV Account**.

2. **Enter Server Information**
   - **Server**: `www.carwashsuppliers.com`
   - **Username**: Your Odoo login email
   - **Password**: Your Odoo password
   - **Description**: `Odoo Contacts`

3. **Save and Sync**
   - Click **Next**.
   - Ensure synchronization is enabled.
   - Contacts from Odoo should now appear in the iOS Contacts app.

## Troubleshooting
- If contacts do not sync, verify:
  - The CardDAV module is installed and enabled in Odoo.
  - The correct server URL and login credentials are used.
  - Developer mode is enabled, and the app list has been updated.
- Check Odoo logs for errors related to CardDAV synchronization.

## License
No license. This was made with ChatGPT.

## Support
No support. Install and use at your own risk.
