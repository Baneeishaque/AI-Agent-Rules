# Android App Launch: Automated Emulator Setup and Deployment

When user asks to run a Flutter app (with Android support) or native Android app, follow this protocol:

1. CHECK AVD STATUS
   - Run avdmanager list avd
   - If suitable AVD exists → Skip to step 4
   - If no AVD → Continue to step 2

2. SYSTEM IMAGE SELECTION PRIORITY
   - Image Type (First): default > google_apis_playstore > others
   - API Level (Second): Highest available
   - Architecture: ARM64 (arm64-v8a) preferred for Apple M2

3. AVD CREATION
   - Device: medium_phone (99% consumer phone coverage)
   - Name: Android_API_[XX]_ARM64_Phone
   - No --force flag (let avdmanager handle conflicts)

4. EMULATOR LAUNCH
   - Memory: 4096MB
   - Cores: 6 (optimal for user's 8-core M2)
   - GPU: auto
   - Flags: -no-boot-anim -no-audio (audio disabled by default)
   - Run in background with &
   - Wait 10-15 seconds for boot

5. VERIFY & LAUNCH
   - Check adb devices shows "device" status
   - Flutter: flutter run
   - Native Android: ./gradlew installDebug

6. FALLBACK
   - ARM64 fails → Try x86_64
   - medium_phone fails → Try pixel_4/pixel_5
