# DDO Group Notifier
@author: Dan Z

All data pertaining to players and groups is attributed to DDO Audit. https://www.playeraudit.com/

You can read more about DDO Audit's API here: https://www.playeraudit.com/api/

This tool is unofficial and is not approved/endorsed by Dungeons & Dragons Online.

## Summary
This tool is a Python app for Windows 10 that will notify you of open LFM (Looking For Members) groups in the online game, Dungeons & Dragons Online.

When you run the ddo_group_notifier module, a Windows system tray icon will start up in your system tray (usually the bottom_right area on your desktop with all the icons). Right-clicking this icon will let you configure the program and let you define group filters. You may also quit the program with the Quit option.

Every N seconds, (where N is defined in configs/configs.yaml), the tool will pull group data from DDO Audit. The tool will then search this group data for groups that fit your character (defined in configs/filters.yaml). The tool will then put up a notification to your Windows 10 machine about this group.