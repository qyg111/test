# _*_ coding: utf-8 _*_
__author__ = 'qyg'
__date__ = '2019/1/30 10:29'
from django.core.files.storage import Storage
from fdfs_client.client import Fdfs_client
from django.conf import settings

class FDFSStorage(Storage):
    '''fdfs文件存储类'''
    def __init__(self, client_conf=None, base_url=None):
        if client_conf is None:
            client_conf =settings.FDFS_CLIENT_CONF
            self.client_conf = client_conf
        if base_url is None:
            base_url = settings.FDFS_URL
            self.base_url = base_url
    def _open(self,name,mode='rb'):
        '''打开文件时使用'''
        pass

    def _save(self,name,content):
        '''保存文件时使用'''
        # name:你选择的上传文件的名字
        # content:File对象

        # 创建一个fdfs_client对象
        client=Fdfs_client(self.client_conf)

        # 上传文件-》fdfs
        res = client.upload_appender_by_buffer(content.read())
        # dict
        # {
        #     'Group name': group_name,
        #     'Remote file_id': remote_file_id,
        #     'Status': 'Upload successed.',
        #     'Local file name': '',
        #     'Uploaded size': upload_size,
        #     'Storage IP': storage_ip
        # }
        if res.get('Status')!='Upload successed.':
            # 上传失败
            raise Exception('文件上传失败')
        # 获取返回的文件ID
        filename = res.get('Remote file_id')
        return filename

    def exists(self,name):
        '''django判断文件名是否可用'''
        return False

    def url(self,name):
        '''django 返回文件的url; 数据表里保存的url'''
        return self.base_url+name