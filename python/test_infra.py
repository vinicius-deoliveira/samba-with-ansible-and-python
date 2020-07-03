def test_samba_is_installed(host):
    samba = host.package("samba")
    assert samba.is_installed

def test_samba_common_is_installed(host):
    samba_common = host.package("samba-common")
    assert samba_common.is_installed

def test_cifs_utils_is_installed(host):
    cifs_utils = host.package("cifs-utils")
    assert cifs_utils.is_installed