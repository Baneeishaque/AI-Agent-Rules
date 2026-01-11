<!--
title: Flutter Android Rules
description: Specific guidelines for Android configurations within Flutter projects.
category: Mobile Development
-->

# Flutter Android Rules

This document outlines specific rules for Android configuration in Flutter projects.

***

### 1. Versioning

- **minSdkVersion**: Must be pinned (e.g., 21) in `android/app/build.gradle`.
- **targetSdkVersion**: Must match the latest stable Android version.

### 2. Permissions

- Explicitly declare permissions in `AndroidManifest.xml`.
- Use the least privilege principle.
