#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#    This script is based on script.randomitems & script.wacthlist
#    Thanks to their original authors

import os
import sys
import xbmc
import xbmcgui
import xbmcplugin
import xbmcaddon
import random
import urllib
import shutil
import glob, os

__addon__     = xbmcaddon.Addon()
__addonid__   = __addon__.getAddonInfo('id')
__language__  = __addon__.getLocalizedString


dialog = xbmcgui.Dialog()
localtxt2 = __language__(32007)
localtxt3 = __language__(32008)
prnum=""
try:
    prnum= sys.argv[ 1 ]
except:
    pass

def packages():

    localtxt1 = __language__(32002)

    destpath=xbmc.translatePath(os.path.join('special://home/addons/packages',''))

    if dialog.yesno(localtxt1, localtxt3):
        shutil.rmtree(destpath)
        os.mkdir(destpath)

        xbmc.executebuiltin("Notification(,"+localtxt2+")")

#-------------------

def musicdb():

    localtxt1 = __language__(32005)
    path = xbmc.translatePath(os.path.join('special://home/userdata/Database',''))


    if dialog.yesno(localtxt1, localtxt3):
        database = os.path.join(path, 'MyMusic*.db')
        print database
        filelist = glob.glob(database)
        print filelist
        if filelist != []:
            for f in filelist:
                print f
                os.remove(f)
                xbmc.executebuiltin("Notification(,"+localtxt2+")")
        else:
            print 'merdaa'
            xbmc.executebuiltin("Notification(,File doesn't exists)")

#-------------------

def videodb():

    localtxt1 = __language__(32004)
    path = xbmc.translatePath(os.path.join('special://home/userdata/Database',''))

    if dialog.yesno(localtxt1, localtxt3):
        database = os.path.join(path, 'MyVideos*.db')
        print database
        filelist = glob.glob(database)
        print filelist
        if filelist != []:
            for f in filelist:
                print f
                os.remove(f)
                xbmc.executebuiltin("Notification(,"+localtxt2+")")
        else:
            print 'merdaa'
            xbmc.executebuiltin("Notification(,File doesn't exists)")

#-------------------

def thumbs():

    localtxt1 = __language__(32001)

    thumbnails=xbmc.translatePath(os.path.join('special://home/userdata/Thumbnails',''))
    thumbdatabase=xbmc.translatePath(os.path.join('special://home/userdata/Database',''))

    dialog = xbmcgui.Dialog()
    if dialog.yesno(localtxt1, localtxt3):
        shutil.rmtree(thumbnails)
        os.mkdir(thumbnails)
        import glob
        for db in glob.glob(os.path.join(thumbdatabase, 'Textures*.*')):
            from sqlite3 import dbapi2 as sqlite3
            try:
                db   = xbmc.translatePath(db)
                conn = sqlite3.connect(db, timeout = 10, detect_types=sqlite3.PARSE_DECLTYPES, check_same_thread = False)
                c    = conn.cursor()

                c.execute("DELETE FROM texture WHERE id > 0")
                c.execute("VACUUM")

                conn.commit()
                c.close()
            except:
                pass

        xbmc.executebuiltin("Notification(,"+localtxt2+")")


#-------------------

def advanced():

    localtxt1 = __language__(32003)


    dialog = xbmcgui.Dialog()
    if dialog.yesno(localtxt1, localtxt3):
        path = xbmc.translatePath(os.path.join('special://home/userdata',''))
        advance=os.path.join(path, 'advancedsettings.xml')
        try:
            os.remove(advance)
            xbmc.executebuiltin("Notification(,"+localtxt2+")")
        except:
            xbmc.executebuiltin("Notification(,File doesn't exists)")


#-------------------


def viewsdb():

    localtxt1 = __language__(32011)

    if dialog.yesno(localtxt1, localtxt3):
        database = os.path.join(path, 'Database/ViewModes*.db')
        print database
        filelist = glob.glob(database)
        print filelist
        if filelist != []:
            for f in filelist:
                print f
                os.remove(f)
            xbmc.executebuiltin("Notification("+localtxt2+",Restart Kodi)")
        else:
            print 'merdaa'
            xbmc.executebuiltin("Notification(Error,File doesn't exists)")

#-------------------

def notify(header="", message="", icon=xbmcgui.NOTIFICATION_INFO, time=5000, sound=True):
    dialog = xbmcgui.Dialog()
    dialog.notification(heading="Service Clean Up", message="This Addon needs arguments to run", icon=icon, time=time, sound=sound)

#-------------------

if prnum == 'packages':
    packages()

elif prnum == 'videodb':
    videodb()

elif prnum == 'musicdb':
    musicdb()

elif prnum == 'thumbs':
    thumbs()

elif prnum == 'advanced':
    advanced()

elif prnum == 'videoviews':
    viewsdb()

elif prnum == "":
    notify()

else:
    print 'INVALID ARGUMENT'