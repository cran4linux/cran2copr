#!/usr/bin/python3

from gi.repository import GLib
from functools import wraps
from contextlib import redirect_stdout
import signal

import dbus
import dbus.service
import dbus.mainloop.glib

import dnf
import dnf.cli.progress
import dnf.cli.output

from os.path import realpath, dirname
exec(open(dirname(realpath(__file__)) + "/dbus-paths").read())

class DnfException(dbus.DBusException):
    _dbus_error_name = IFACE + ".DnfException"

def stderr(pid):
    return open("/proc/" + str(pid) + "/fd/2", "w")

def redirect_stdout_handle_exceptions(timeout):
    def _redirect_stdout_handle_exceptions(fn):
        @wraps(fn)
        def wrapper(self, pid, *args, **kw):
            signal.alarm(0)
            with stderr(pid) as f, redirect_stdout(f):
                try:
                    out = fn(self, pid, *args, **kw)
                except Exception as err:
                    raise DnfException(str(err))
                finally:
                    signal.alarm(timeout)
            return out
        return wrapper
    return _redirect_stdout_handle_exceptions

class PackageManager(dbus.service.Object):
    
    @dbus.service.method(IFACE, in_signature="ias", out_signature="as")
    @redirect_stdout_handle_exceptions(10)
    def install(self, pid, pkgs):
        print("Installing Copr packages...", flush=True)
        base = dnf.Base()
        base.read_all_repos()
        base.fill_sack()
        
        notavail = []
        for pkg in pkgs:
            try:
                base.install("R-CRAN-" + pkg)
                base.upgrade("R-CRAN-" + pkg)
            except dnf.exceptions.PackagesNotInstalledError:
                pass
            except:
                notavail.append(pkg)
        
        base.resolve()
        progress = dnf.cli.progress.MultiFileProgressMeter()
        base.download_packages(base.transaction.install_set, progress)
        base.do_transaction(dnf.cli.output.CliTransactionDisplay())
        base.close()
        
        return notavail
    
    @dbus.service.method(IFACE, in_signature="ias", out_signature="as")
    @redirect_stdout_handle_exceptions(10)
    def remove(self, pid, pkgs):
        print("Removing Copr packages...", flush=True)
        base = dnf.Base()
        base.fill_sack()
        
        notavail = []
        for pkg in pkgs:
            try:
                base.remove("R-CRAN-" + pkg)
            except:
                notavail.append(pkg)
        
        base.resolve(True)
        base.do_transaction(dnf.cli.output.CliTransactionDisplay())
        base.close()
        
        return notavail

def sigterm_handler(_signo, _stack_frame):
    mainloop.quit()

if __name__ == "__main__":
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
    signal.signal(signal.SIGINT, sigterm_handler)
    signal.signal(signal.SIGTERM, sigterm_handler)
    signal.signal(signal.SIGALRM, sigterm_handler)

    bus = dbus.SystemBus()
    bus.request_name(BUS_NAME)
    pm = PackageManager(bus, OPATH)

    mainloop = GLib.MainLoop()
    mainloop.run()
