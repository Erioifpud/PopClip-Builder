from enum import Enum
import plistlib


class BeforeAfter(Enum):
    CUT = 'cut'
    COPY = 'copy'
    PASTE = 'paste'
    PASTE_PLAIN = 'paste-plain'
    POPCLIP_APPEAR = 'popclip-appear'
    COPY_SELECTION = 'copy-selection'
    COPY_RESULT = 'copy-result'
    PASTE_RESULT = 'paste-result'
    PREVIEW_RESULT = 'preview-result'
    SHOW_RESULT = 'show-result'
    SHOW_STATUS = 'show-status'


class Requirement(Enum):
    COPY = 'copy'
    CUT = 'cut'
    PASTE = 'paste'
    FORMATTING = 'formatting'
    HTTP_URL = 'httpurl'
    HTTP_URLS = 'httpurls'
    EMAIL = 'email'
    PATH = 'path'
    HTML = 'html'
    OPTION = lambda k, v: 'option-{}={}'.format(k, v)


class OptionType(Enum):
    STRING = 'string'
    BOOLEAN = 'boolean'
    MULTIPLE = 'multiple'


class ActionType(Enum):
    def Service(name: str):
        return {'Service': name}

    def AppleScript(fileName: str):
        return {'AppleScript File': fileName}

    def ShellScript(fileName: str, interpreter: str):
        return {'Shell Script File': fileName,
                'Script Interpreter': interpreter}

    def URL(url: str):
        return {'URL': url}

    def Keypress(keyCombo: list):
        return {'Key Combo': keyCombo}


class KeysValue(Enum):
    NONE = 0
    SHIFT = 131072
    CONTROL = 262144
    OPTION = 524288
    COMMAND = 1048576


class Option:
    def __init__(self, optIdentifier: str, optType: OptionType, optLabel,
                 optDefault: str=None, optValues: list=None):
        self.optIdentifier = optIdentifier
        self.optType = optType
        self.optLabel = optLabel
        self.optDefault = optDefault
        self.optValues = optValues

    @property
    def data(self):
        obj = {
            'Option Identifier': self.optIdentifier,
            'Option Type': self.optType.value,
            'Option Label': self.optLabel
        }

        if self.optType.value in 'multiple':
            obj['Option Values'] = self.optValues

        if self.optDefault is not None:
            obj['Option Default Value'] = self.optDefault

        return obj


class Apps:
    def __init__(self, name: str, checkInstalled: bool=None, link: str=None,
                 bundleIndentifier: str=None, bundleIndentifiers: list=None):
        self.name = name,
        self.checkInstalled = checkInstalled,
        self.link = link,
        self.bundleIndentifier = bundleIndentifier,
        self.bundleIndentifiers = bundleIndentifiers

    @property
    def data(self):
        obj = {
            'Name': self.name
        }

        if self.checkInstalled is not None:
            obj['Check Installed'] = self.checkInstalled

        if self.checkInstalled:
            if self.link is not None:
                obj['Link'] = self.link
            if self.bundleIndentifier is not None:
                obj['Bundle Identifier'] = self.bundleIndentifier
            else:
                obj['Bundle Identifiers'] = self.bundleIndentifiers

        return obj


class Action:
    def __init__(self, title, type: ActionType, image: str=None,
                 before: str=None, after: str=None, blockedApps: list=None,
                 requiredApps: list=None, regex: str=None,
                 requirements: list=None, stayVisible: bool=None,
                 preserveColor: bool=None, passHtml: bool=None,
                 restorePasteBoard: bool=None, longRunning: bool=None):
        self.title = title
        self.type = type
        self.image = image
        self.before = before
        self.after = after
        self.blockedApps = blockedApps
        self.requiredApps = requiredApps
        self.regex = regex
        self.requirements = requirements
        self.stayVisible = stayVisible
        self.preserveColor = preserveColor
        self.passHtml = passHtml
        self.restorePasteBoard = restorePasteBoard
        self.longRunning = longRunning

    @property
    def data(self):
        obj = {
            'Title': self.title
        }

        if self.image is not None:
            obj['Image File'] = self.image

        if self.before is not None:
            #obj['Before'] = self.before
            obj['Before'] = self.before.value

        if self.after is not None:
            #obj['After'] = self.after
            obj['After'] = self.after.value

        if self.blockedApps is not None:
            obj['Blocked Apps'] = self.blockedApps

        if self.requiredApps is not None:
            obj['Required Apps'] = self.requiredApps

        if self.regex is not None:
            obj['regex'] = self.regex

        if self.requirements is not None:
            #obj['Requirements'] = self.requirements
            obj['Requirements'] = [r.value for r in self.requirements]


        if self.stayVisible is not None:
            obj['Stay Visible'] = self.stayVisible

        if self.preserveColor is not None:
            obj['Preserve Image Color'] = self.preserveColor

        if self.passHtml is not None:
            obj['Pass HTML'] = self.passHtml

        if self.restorePasteBoard is not None:
            obj['Restore Pasteboard'] = self.restorePasteBoard

        if self.longRunning is not None:
            obj['Long Running'] = self.longRunning

        obj.update(self.type)
        return obj


class Config:
    def __init__(self, extName, extIdentifier: str, actions: list,
                 extImage: str=None, blockedApps: list=None, regex: str=None,
                 requirements: list=None, stayVisible: bool=None,
                 preserveColor: bool=None, passHtml: bool=None,
                 longRunning: bool=None, restorePasteBoard: bool=None,
                 extLongName=None, credits: list=None, apps: list=None,
                 requiredOSVer: str=None, requiredSoftwareVer: int=None,
                 options: list=None, optionsTitle=None,
                 requiredApps: list=None, extDesc=None):
        self.extName = extName
        self.extIdentifier = extIdentifier
        self.actions = actions
        self.extImage = extImage
        self.blockedApps = blockedApps
        self.regex = regex
        self.requirements = requirements
        self.stayVisible = stayVisible
        self.preserveColor = preserveColor
        self.passHtml = passHtml
        self.longRunning = longRunning
        self.restorePasteBoard = restorePasteBoard
        self.extLongName = extLongName
        self.credits = credits
        self.apps = apps
        self.requiredOSVer = requiredOSVer
        self.requiredSoftwareVer = requiredSoftwareVer
        self.options = options
        self.optionsTitle = optionsTitle
        self.requiredApps = requiredApps
        self.extDesc = extDesc

    @property
    def data(self):
        obj = {
            'Extension Name': self.extName,
            'Extension Identifier': self.extIdentifier
        }

        obj['Actions'] = [a.data for a in self.actions]

        if self.blockedApps is not None:
            obj['Blocked Apps'] = self.blockedApps

        if self.requiredApps is not None:
            obj['Required Apps'] = self.requiredApps

        if self.regex is not None:
            obj['regex'] = self.regex

        if self.requirements is not None:
            #obj['Requirements'] = self.requirements
            obj['Requirements'] = [r.value for r in self.requirements]

        if self.stayVisible is not None:
            obj['Stay Visible'] = self.stayVisible

        if self.preserveColor is not None:
            obj['Preserve Image Color'] = self.preserveColor

        if self.passHtml is not None:
            obj['Pass HTML'] = self.passHtml

        if self.restorePasteBoard is not None:
            obj['Restore Pasteboard'] = self.restorePasteBoard

        if self.longRunning is not None:
            obj['Long Running'] = self.longRunning

        if self.extImage is not None:
            obj['Extension Image File'] = self.extImage

        if self.extLongName is not None:
            obj['Extension Long Name'] = self.extLongName

        if self.credits is not None:
            obj['Credits'] = self.credits

        if self.apps is not None:
            obj['Apps'] = self.apps

        if self.requiredOSVer is not None:
            obj['Apps'] = self.requiredOSVer

        if self.requiredSoftwareVer is not None:
            obj['Apps'] = self.requiredSoftwareVer

        if self.options is not None:
            obj['Options'] = self.options

        if self.optionsTitle is not None:
            obj['Options Title'] = self.optionsTitle

        if self.extDesc is not None:
            obj['Extension Description'] = self.extDesc

        return obj

'''
a1 = Action('a1', type=ActionType.ShellScript('shell', 'inter'),
            image='image1', after=BeforeAfter.CUT)
a2 = Action('a2', type=ActionType.Service('service'), image='image2',
            before=BeforeAfter.COPY, requirements=[Requirement.HTML])
b = Config('extName', 'work.erio', [a1, a2])
print(b.data)
with open('test.plist', 'wb') as f:
    plistlib.dump(b.data, f)
# --------------
action = Action('echo', type=ActionType.ShellScript('echo.sh', '/bin/zsh'),
                after=BeforeAfter.SHOW_RESULT, image='icon.png')
config = Config('EchoTest', 'work.erio', actions=[action])
with open('Config.plist', 'wb') as f:
    plistlib.dump(config.data, f)
'''
