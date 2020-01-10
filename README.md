Ansible role for dnsmasq
=========

[![Build Status](https://github.com/clayman74/ansible-dnsmasq/workflows/Tests/badge.svg)](https://github.com/clayman74/ansible-dnsmasq)

This role installs and configures the dnsmasq.

Requirements
------------

This role requires Ansible 1.4 or higher and platform requirements are listed in the metadata file.

How to use
----------------

Add `requirements.yml` to your project:

    ---

      - src: https://github.com/clayman74/ansible-dnsmasq
        version: v1.0.0
        name: dnsmasq


And then install it with Ansible Galaxy

    $ ansible-galaxy install -r requirements.yml


Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: all
      become: true

      roles:
         - role: dnsmasq


License
-------

MIT

Author Information
------------------

Kirill Sumorokov
