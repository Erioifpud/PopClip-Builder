import builder
import popclip as pc


say = pc.Action('say', type=pc.ActionType.ShellScript('say.sh', '/bin/zsh'),
                image='icon.png', after=pc.BeforeAfter.COPY)
config = pc.Config('SayTest', extIdentifier='work.erio', actions=[say])

builder.build("SayTest", config, iconText='say')
