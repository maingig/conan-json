#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from conans import ConanFile, CMake, tools

class SigslotConan(ConanFile):
    name = "json"
    version = "3.9.1"
    license = "https://github.com/nlohmann/json/blob/develop/LICENSE.MIT"
    author = "https://github.com/nlohmann/json/graphs/contributors"
    url = "https://github.com/nlohmann/json.git"
    description = "header-only, thread safe implementation of json for C++"
    no_copy_source = True

    def source(self):
        self.run("git clone %s %s" % (self.url, self.name))
        self.run("cd %s && git checkout tags/v%s -b master" % (self.name, self.version))

    def package(self):
        self.copy("*.hpp", src=self.name)

    def package_id(self):
        self.info.header_only()
        


