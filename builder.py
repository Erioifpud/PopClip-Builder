import popclip as pc
import icon
import os
import plistlib
import errno
import subprocess


def generate(projectName, config, path='./', iconText=None):
    ''' generate extension from your PopClip object '''
    if not iconText:
        iconText = projectName

    dirPath = '{}{}/'.format(path, projectName)
    if not os.path.exists(os.path.dirname(dirPath)):
        try:
            os.makedirs(os.path.dirname(dirPath))
        except OSError as ex:
            if ex.errno != errno.EEXIST:
                raise

    with open('{}Config.plist'.format(dirPath), 'wb') as f:
        plistlib.dump(config.data, f)

    with open('{}icon.png'.format(dirPath), 'wb') as f:
        icon.create(iconText, f)


def pack(projectName, path='./'):
    ''' convert project to popclipext '''
    dirPath = '{}{}/'.format(path, projectName)
    extName = '{}.dev.popclipext'.format(projectName)
    subprocess.call('rm -rf {}{}'.format(dirPath, extName), shell=True)
    subprocess.call('cp -rf {} ./{}'.format(dirPath, extName), shell=True)


def build(projectName, config, path='./', iconText=None):
    ''' include generate and pack '''
    generate(projectName, config, path, iconText)
    pack(projectName, path)
