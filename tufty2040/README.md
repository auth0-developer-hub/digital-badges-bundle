# Tufty 2040 from Devday@Oktane

## Start here

### Set up

1. **Thonny:** The IDE we are going to use to communicate with the Tufty2040
1. **Tufty 2040:** Your board for all things fun.
1. **This folder**.

### Uploading assets to the Tufty2040

1. Follow the instructions on [getting started with Tufty 2040](https://learn.pimoroni.com/article/getting-started-with-tufty-2040#introduction);
1. Open Thonny;
1. Choose your preferred character in the _badges/_ and update the seventh line `upload_these/badges/badge.txt` to correspond to the character image
1. Update the contents of `upload_these/badges/badge.txt` to match your details;
1. Upload all the files in the _upload\_these_ folder into your badge, [detailed instructions here](https://www.thoughtasylum.com/2022/04/29/the-badger-2040-set-up/);
1. After everything is uploaded into your device, reset the Tufty2040 and navigate to _badge_ to see your badge.

### Need help?

For further assistance either find any Auth0 by Okta's developer advocate in the Community Corner during the Devday@Oktane or open an issue and tag @jtemporal.

## More information

### Files description

- `characters`: collection of images that can be used to display on your badge
    - Images in the Tufty2040 need to be `.jpg` and need to have 120x120 pixels.
- `upload_these`: contents to upload and replace the current files on the `Tufty2040`

To adjust the information written on the screen use the `.txt` files.

### Creating personalized badges

You'll probably want a personalized badge, so you'll need an image with your with the following dimensions:

* width: 120px
* height: 120px

[Here's a Canva template you can use](https://www.canva.com/design/DAFrDHrarLs/VLCVo4faRglf4UDhOhiQoQ/view?utm_content=DAFrDHrarLs&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink&mode=preview), it already has the correct dimensions, just remember to add an image of your own.
