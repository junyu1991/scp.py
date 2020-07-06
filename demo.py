#!encoding:utf-8
#author: yujun
#date: 2020-07-06

import os
import paramiko
import scp

def test_upload():
    '''
    Download file via SCPClient
    '''
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.client.AutoAddPolicy())
    client.connect(hostname='192.168.1.100', username='root', password='password')
    scp_client = scp.SCPClient(client.get_transport())
    local_path = 'c:/Users/admin/Desktop/upload'
    remote_path = '/home/test/temp'
    encode = 'GB18030'
    scp_client.put(files=local_path, remote_path=remote_path, recursive=True, encoding=encode)

def test_download():
    '''
    Upload file via SCPClient
    '''
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.client.AutoAddPolicy())
    client.connect(hostname='192.168.1.100', username='root', password='password')
    scp_client = scp.SCPClient(client.get_transport())
    local_path = 'c:/Users/admin/Desktop/upload'
    remote_path = '/home/test/temp'
    encode = 'GB18030'
    scp_client.get(local_path=local_path, remote_path=remote_path, recursive=True, encoding=encode)




if __name__ == '__main__':
    test_upload()
    test_download()
