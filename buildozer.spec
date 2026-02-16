[app]
title = RAVANA AGENT
package.name = ravanaagent
package.domain = lk.ravana
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# ඔයා කිව්ව Requirements ටික හරියටම මෙතන තියෙනවා
requirements = python3,kivy,plyer,requests,urllib3,charset-normalizer,idna

orientation = portrait
fullscreen = 0

# Android Permissions (GPS සහ Internet අනිවාර්යයි)
android.permissions = INTERNET,ACCESS_FINE_LOCATION,ACCESS_COARSE_LOCATION
android.api = 31
android.minapi = 21
android.ndk_api = 21
android.archs = arm64-v8a

# GitHub එකේදී Exit Code 100 නොවෙන්න මේ පේළිය අනිවාර්යයි
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
