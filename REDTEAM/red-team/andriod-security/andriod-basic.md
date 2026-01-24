# Andriod Basic





<figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

## Introduction

The andiod architecture are

* Linux Kernel&#x20;
* Hardware abstraction layer
* Libraries
* Andriod Runtimes
* Andriod Framework
* Application





<figure><img src="../../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>





#### Hardware Absraction Layer

* HAL is the bridge between Kernal and native libararies( Drivers of camera/bluethoon).

<figure><img src="../../.gitbook/assets/image (56).png" alt=""><figcaption></figcaption></figure>



Native Libarires

* Libaries provide essitails servies&#x20;

Andriod runtime.

Initially, Android used the **Dalvik Virtual Machine (DVM)**, which executed **Dalvik bytecode (`.dex`)** using **Just-In-Time (JIT)** compilation.

Later, Dalvik was replaced by **Android Runtime (ART)**, which **executes APK files** using **Ahead-Of-Time (AOT)** compilation.

With AOT, app code is compiled **once during installation**, which:

* Improves performance
* Reduces CPU and memory usage
* Saves battery
