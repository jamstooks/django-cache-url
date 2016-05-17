import django_cache_url

# pub-memcache-13869.us-east-1-4.2.ec2.garantiadata.com:13869

#
# BMemcached
#

def test_bmemcached():
    url = 'bmemcached://127.0.0.1:6379'
    config = django_cache_url.parse(url)

    assert config['BACKEND'] == 'django_bmemcached.memcached.BMemcached'
    assert config['LOCATION'] == '127.0.0.1:6379'

def test_bmemcached_url_multiple_locations():
    url = 'bmemcached://127.0.0.1:11211,192.168.0.100:11211'
    config = django_cache_url.parse(url)

    assert config['BACKEND'] == 'django_bmemcached.memcached.BMemcached'
    assert config['LOCATION'] == '127.0.0.1:11211;192.168.0.100:11211'

def test_bmemcached_with_user_and_password():
    url = 'bmemcached://user:pass@127.0.0.1:6379'
    config = django_cache_url.parse(url)

    assert config['BACKEND'] == 'django_bmemcached.memcached.BMemcached'
    assert config['LOCATION'] == '127.0.0.1:6379'
    assert config['OPTIONS']['username'] == 'user'
    assert config['OPTIONS']['password'] == 'pass'
    
def test_bmemcached_with_password_only():
    url = 'bmemcached://:pass@127.0.0.1:6379'
    config = django_cache_url.parse(url)

    assert config['BACKEND'] == 'django_bmemcached.memcached.BMemcached'
    assert config['LOCATION'] == '127.0.0.1:6379'
    assert 'username' not in config['OPTIONS'].keys()
    assert config['OPTIONS']['password'] == 'pass'
    
def test_bmemcached_with_user_only():
    url = 'bmemcached://user@127.0.0.1:6379'
    config = django_cache_url.parse(url)

    assert config['BACKEND'] == 'django_bmemcached.memcached.BMemcached'
    assert config['LOCATION'] == '127.0.0.1:6379'
    assert config['OPTIONS']['username'] == 'user'
    assert 'password' not in config['OPTIONS'].keys()
