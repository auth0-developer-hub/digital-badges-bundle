# Badger 2040

## Start here

### Set up

1. **Thonny:** The IDE we are going to use to communicate with the Badger2040
1. **Badger 2040:** Your board for all things fun.
1. **This folder**.

### Uploading assets to the Badger2040

1. Follow the instructions on [getting started with Badger 2040](https://learn.pimoroni.com/article/getting-started-with-badger-2040#introduction);
1. Open Thonny;
1. Choose your preferred character in the _badges/_ and update the seventh line `upload_these/badges/badge.txt` to correspond to the character image
1. Add your name in the second line of the `upload_these/badges/badge.txt`;
1. Upload all the files in the _upload\_these_ folder into your badge, [detailed instructions here](https://www.thoughtasylum.com/2022/04/29/the-badger-2040-set-up/);
1. After everything is uploaded into your device, reset the Bagder2040 and navigate to _badge_ to see your badge.

### Need help?

For further assistance either find any of Auth0 by Okta's developer advocates at developer events or open an issue and tag @jtemporal.

## More information

### Files description

- `upload_these`: contents to upload and replace the current files on the `Badger2040`.
    - Images in the Badger2040 need to be `.jpg` and need to have 104x128 pixels.

To adjust the information written on the screen use the `.txt` files.

### Creating personalized badges

You'll probably want a personalized badge, so you'll need an image with your with the following dimensions:

* width: 104px
* height: 128px

[Here's a Canva template you can use](https://www.canva.com/design/DAFrALs4Y9M/jaOvDF6RzTROxnDUyuEWnA/view?utm_content=DAFrALs4Y9M&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink&mode=preview), it already has the correct dimensions, just remember to add an image of your own.

### Troubleshooting

If you are getting the `ImportError` for `jpegdec` you'll need to reinstall micropython in the badge.

- Download the most recent MicroPython .uf2 from the Releases page of our badger2040 Github repository. Click on 'assets' to expand the list of files - for the version with examples built in you'll want to download pimoroni-badger2040-vx.x.x-micropython-with-badger-os.uf2 (for Badger 2040) or pimoroni-badger2040w-vx.x.x-micropython-with-badger-os.uf2 (for Badger 2040 W). Make sure you download the correct one for your board!
- Connect Badger to your computer with a USB cable.
- Hold down BOOT/USR (on Badger 2040) or the BOOTSEL button (on Badger 2040 W), and then tap the RESET button. This will put it into bootloader mode, and it should appear as a drive on your computer called RPI-RP2.
- Copy the .uf2 file to the RPI-RP2 drive - once you've done that Badger will reboot.

For [more details refer to this page](https://learn.pimoroni.com/article/getting-started-with-badger-2040#troubleshooting)