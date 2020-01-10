import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_config_file(host):
    f = host.file('/etc/dnsmasq.conf')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_resolve_domain(host):
    cmd = host.run('nslookup dev.example.com localhost')

    assert 'Name:	dev.example.com' in cmd.stdout
    assert 'Address: 127.0.0.1' in cmd.stdout
