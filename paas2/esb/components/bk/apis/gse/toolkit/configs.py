# -*- coding: utf-8 -*-
import os.path

from django.conf import settings

from esb.utils import SmartHost, get_ssl_root_dir


SYSTEM_NAME = "GSE"


gse_proc_host = SmartHost(host_prod=settings.GSE_PROC_HOST)
gse_proc_port = settings.GSE_PROC_PORT

# SSL 证书配置
SSL_ROOT_DIR = get_ssl_root_dir()
SERVER_CERT = os.path.join(SSL_ROOT_DIR, "gseca.crt")
CLIENT_CERT = os.path.join(SSL_ROOT_DIR, "gse_esb_api_client.crt")
CLIENT_KEY = os.path.join(SSL_ROOT_DIR, "gse_esb_api_client.key")