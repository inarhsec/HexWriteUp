# Andriod Basic

#### Introduction

An Andriod is an open source linux based operation system/software, it is na arrary of devices which can run on phone, watch , IOT etc.

* Srart with linux kernal.
* Hardware abstration layer containing drivces to connected the hardware.
* Libararies, Native libarries written in C++.
* Andriod runtime enviorment with EEN specific VM like Java runtime enviroment.
* Andriod framework with different APIs written in JAVA.
* App build in APP platform like camera,Alarm Etc.



<figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

## Introduction

The andiod architecture are

* Linux Kernel&#x20;
* Hardware abstraction layer
* Libraries
* Andriod Runtimes
* Andriod Framework
* Application



Linux kernel also called ring zero because is the heard of OS. the kernel handles basic system service like memory and so device connecting to the hardware and for the security part linux kernel so the any security assessment when get the and check the kernel in the exploit DB for expoits

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
