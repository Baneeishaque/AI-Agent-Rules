<!--
title: Android App Launch Rules
description: Automated protocol for emulator setup and deployment, optimized for M2 machines, with architecture and device fallbacks.
category: Android Development
-->

# Android App Launch Rules

### Android App Launch Protocol: Advanced Emulator Management and Deployment ⚙️

This document provides a robust, automated protocol for configuring, launching, and deploying an Android application for development and testing. This process is optimized for command-line execution on Apple Silicon (M2) machines.

***

### 1. Pre-Flight Check: Verify Java JDK ☕

Before running any Android SDK command-line tools, it is crucial to ensure a compatible Java Development Kit (JDK) is available in your system's PATH. `avdmanager` and other tools are Java-based and will fail without it.

* **Requirement:** Ensure a compatible JDK is installed and configured. Currently, **JDK 17** is the required version for the latest Android SDK.
* **Verification:** Run `java -version` to confirm the installed version.
* **User Instruction:** If Java is not found or is outdated, the user must install a compatible JDK (e.g., OpenJDK 17) and set the `JAVA_HOME` and `PATH` environment variables. For instance, on a modern shell, this could be: `export JAVA_HOME=/path/to/your/jdk && export PATH=$PATH:$JAVA_HOME/bin`.

***

### 2. Check Existing AVD Status & System Image and AVD Creation 🔎

The first step is to check if a suitable Android Virtual Device (AVD) already exists to avoid redundant creation. If a suitable AVD does not exist, a new one must be created.

* **Command:** The `avdmanager list avd` command is used to list all pre-configured AVDs.
* **Logic:** The script will parse the command output to identify an AVD that meets the specified criteria (API level, architecture, etc.). If a match is found, the process proceeds directly to the launch step, saving time and resources.
* **Image Selection Priority:**
    1.  **Image Type:** The `default` system image is preferred for a basic, un-bloated environment. If not available, `google_apis_playstore` is the next choice, as it includes Google Play Services, which is essential for many modern applications.
    2.  **API Level:** The **highest available API level** will be chosen to ensure compatibility with the latest Android features and security updates.
    3.  **Architecture:** **ARM64 (arm64-v8a)** is the top priority for Apple Silicon (M1/M2) machines. The ARM architecture of the host machine is a native match for the ARM-based Android emulator image, resulting in significantly better performance and lower resource consumption compared to `x86_64` emulation.
* **AVD Creation:**
    * **Device:** The `medium_phone` device profile is selected as a sensible default. It provides a screen size and resolution that covers roughly 99% of consumer phones, making it a reliable choice for general-purpose testing.
    * **Name:** The AVD will be named consistently as `Android_API_[XX]_ARM64_Phone`, where `[XX]` is the API level. This naming convention makes it easy to identify and manage different AVDs.
    * **Flag:** The `--force` flag will **not** be used to prevent accidental overwrites of existing AVDs.

***

### 3. Emulator Launch Configuration & Application Launch 🚀

Once an AVD is ready, the emulator is launched with optimized settings. After the emulator is running, the application is installed and launched.

* **Memory:** `4096MB` (4GB) of RAM is allocated for smooth performance without starving the host machine.
* **Cores:** `6` cores are allocated, which is optimal for an 8-core M2.
* **GPU:** The `auto` setting is used for the GPU, which typically defaults to **hardware acceleration (OpenGL ES)** and is crucial for a responsive UI.
* **Flags:** `-no-boot-anim` skips the boot animation, and `-no-audio` disables audio, preventing conflicts. The process is run in the background using `&` to allow the script to continue.
* **Wait Time:** A 10-15 second wait is implemented to give the emulator sufficient time to boot up and for the Android Debug Bridge (`adb`) to recognize it.
* **Device Verification:** The `adb devices` command is run to confirm the emulator is connected and recognized.
* **Application Launch:**
    * For **Flutter apps**, the `flutter run` command is used, which automatically installs and launches the app.
    * For **Native Android apps**, `./gradlew installDebug` is executed to build and install the debug version of the application, which will automatically launch upon successful installation.
    * The protocol also applies to other frameworks like **React Native**, where a similar `npx react-native run-android` command would be used to install and launch the app.

***

### 4. Debugging & Fallback Protocol 🔄

A systematic approach to debugging is essential for productivity. In the event of a failure, the protocol includes a fallback mechanism.

* **Environment Check:** Always begin by running `flutter doctor` to ensure the development environment is correctly set up.
* **Real-time Logs:** Use `flutter logs` to view the live log stream from a running application.
* **IDE Debugger:** Leverage the IDE's integrated debugger to set breakpoints, inspect variables, and step through code execution.
* **Architecture Fallback:** If the ARM64 setup fails, the system will automatically fall back to using an `x86_64` architecture. While slower due to binary translation, it provides a reliable backup.
* **Device Fallback:** If the `medium_phone` profile fails, the system will try a known-good device profile like `pixel_4` or `pixel_5`.

***

### 5. Additional Considerations

* **Android Debug Bridge (ADB):** The entire process relies on the Android Debug Bridge, a versatile command-line tool that allows for communication with Android devices and emulators. It's a client-server program that manages the connection and facilitates commands like installing apps and viewing logs.
* **CI/CD Integration:** This protocol is perfectly suited for use in a CI/CD environment like GitHub Actions. The scripts can be easily integrated into a workflow to automatically run tests on a freshly provisioned emulator, ensuring consistent and reliable results.
* **Snapshotting:** For further performance optimization, a future enhancement could involve creating and using **emulator snapshots**. This would allow the emulator to boot almost instantly from a pre-saved state, bypassing the lengthy cold-boot process. This is a game-changer for CI/CD pipelines where multiple emulator launches are required.

***

### 6. General Guidelines

* **General Adherence:** Adhere to all general rule documents, including `ai-agent-planning-rules.md`, `ai-tools-rules.md`, and `shell-execution-rules.md`, to ensure a unified and secure development environment.
