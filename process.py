#!/usr/bin/env python
# -*- coding: utf-8 -*-

import shlex
import subprocess


def _call(cmd, env=None):
    try:
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE, env=env)
    except (OSError, TypeError) as err:
        raise err
    out, err = process.communicate()
    out = str(out)
    err = str(err)

    result = {}
    result['returncode'] = process.returncode
    result['stdout'] = out
    result['stderr'] = err
    result['fullcmd'] = " ".join(cmd)
    return result


# TODO: add doctests
class Process(object):
    def __init__(self, cmds=None):
        self.cmds = cmds or []

    def __getattr__(self, name):
        name = name.replace('_', '-')  # e.g. format_patch -> format-patch
        return self.bake(name)

    def __call__(self, *a, **kw):
        proc = self.bake()
        env = kw.pop('env', {})
        proc._parse_args(*a, **kw)
        return proc.call(env=env)

    def _parse_args(self, *a, **kw):
        cmds = []
        for p in a:
            if not isinstance(p, str):
                raise KeyError
            cmds.append(p)

        for k, v in kw.iteritems():
            if len(k) == 1:
                k = '-' + k
            else:
                k = '--' + k
            if '_' in k:  # e.g. --no_ff -> --no-ff
                k = k.replace('_', '-')
            if not v:  # v in (None, '', False)
                continue
            elif isinstance(v, bool):  # v is True
                cmds.append(k)
            elif isinstance(v, str):
                cmds.append(k)
                cmds.append(v)
            else:
                raise KeyError
        self.cmds += cmds

    def bake(self, *a, **kw):
        cmds = list(self.cmds)
        proc = Process(cmds)
        proc._parse_args(*a, **kw)
        return proc

    def call(self, cmdstr='', env=None):
        extra_cmds = shlex.split(cmdstr)
        return _call(self.cmds + extra_cmds, env=env)


process = Process()
