Multitouch on newer Elantech Touchpads in Linux
###############################################

:date: 2013/06/23
:tags: linux, hardware, mint

I'm running Linux Mint 14 XFCE on a Gigabyte U2442.  The touchpad ends up recognized as a PS2 mouse and therefore lacks touchpad features.  Several symptoms:

 "Couldn't find synaptics properties. No synaptics driver loaded?" when running ``synclient``.

 The device showing up as "PS/2 Generic Mouse" when running ``xinput list``.

 The device now showing up as a trackpad in the control panel (varies from distro to distro, but it is Settings > Mouse and Trackpad in XFCE.



The biggest annoyance is the inability to disable the touchpad while typing, which can send the cursor flying across the screen while I'm coding, disrupting flow and requiring undos when it deletes huge sections as well.  Once this fix is applied, that option can be set in the control panel.

There was no clear fix for a while - the Ubuntu documentation on `Debugging HAL <https://wiki.ubuntu.com/DebuggingHal>`_ bugs is over five years out of date.

Finally, in the last month, some users found `a workaround <https://bugs.launchpad.net/ubuntu/+source/linux/+bug/1166442>`_ while the kernel team works on a similar bug with Samsung S9-series laptops.  

The short version::

 sudo apt-get install dkms
 cd /usr/src/
 sudo wget http://planet76.com/drivers/elantech/psmouse-elantech-v6.tar.bz2
 sudo tar jxvf psmouse-elantech-v6.tar.bz2
 sudo dkms add -m psmouse -v elantech-v6
 sudo dkms build -m psmouse -v elantech-v6
 sudo dkms install -m psmouse -v elantech-v6

Then reboot.
