# click_yes

a script to accept the license agreement to the wifi network on an
ongoing and automated basis. ;-)

## Installing

    sudo install -m 0755 ./click_yes.py /usr/local/sbin/
    sudo install -m 0644 ./click_yes.service /etc/systemd/system/
    sudo systemctl enable click_yes.service
    sudo systemctl start click_yes.service
