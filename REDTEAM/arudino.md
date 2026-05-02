# Arudino

## ESP32 CODEs

### BLUTLOOTH ACTIVE SCANNER.

{% code title="bluactivescanner" overflow="wrap" %}
```cpp
// ================================================================
//  ESP32 BLE RAW SCANNER — ZERO FILTERS, PRINTS EVERYTHING
//  Every device, every packet, every RSSI, no limits at all
// ================================================================

#include <BLEDevice.h>
#include <BLEScan.h>
#include <BLEAdvertisedDevice.h>
#include "esp_bt.h"

static uint32_t packetCount = 0;

class RawScanCB : public BLEAdvertisedDeviceCallbacks {
  void onResult(BLEAdvertisedDevice dev) override {
    packetCount++;

    char mac[18] = {0};
    strncpy(mac, dev.getAddress().toString().c_str(), 17);

    int rssi = dev.getRSSI();

    Serial.print("[#");
    Serial.print(packetCount);
    Serial.print("]  MAC: ");
    Serial.print(mac);
    Serial.print("   RSSI: ");
    Serial.print(rssi);
    Serial.print(" dBm");

    if (dev.haveName()) {
      Serial.print("   Name: \"");
      Serial.print(dev.getName().c_str());
      Serial.print("\"");
    }

    if (dev.haveAppearance()) {
      Serial.print("   Appearance: ");
      Serial.print(dev.getAppearance());
    }

    if (dev.haveManufacturerData()) {
      Serial.print("   MfgData: YES");
    }

    Serial.println();
  }
};

void setup() {
  Serial.begin(115200);
  delay(1500);

  Serial.println();
  Serial.println("========================================");
  Serial.println("  ESP32 BLE RAW SCANNER — ALL DEVICES");
  Serial.println("  No filters. No limits. No thresholds.");
  Serial.println("  Printing every single BLE packet.");
  Serial.println("========================================");
  Serial.println();

  BLEDevice::init("ESP32-RAW");

  // Maximum TX power on all contexts
  esp_ble_tx_power_set(ESP_BLE_PWR_TYPE_DEFAULT,   ESP_PWR_LVL_P9);
  esp_ble_tx_power_set(ESP_BLE_PWR_TYPE_ADV,       ESP_PWR_LVL_P9);
  esp_ble_tx_power_set(ESP_BLE_PWR_TYPE_SCAN,      ESP_PWR_LVL_P9);
  esp_ble_tx_power_set(ESP_BLE_PWR_TYPE_CONN_HDL0, ESP_PWR_LVL_P9);
  esp_ble_tx_power_set(ESP_BLE_PWR_TYPE_CONN_HDL1, ESP_PWR_LVL_P9);

  BLEScan* scan = BLEDevice::getScan();

  // false = NO deduplication — every single packet fires callback
  scan->setAdvertisedDeviceCallbacks(new RawScanCB(), false);

  // Active scan = requests scan response (gets device names)
  scan->setActiveScan(true);

  // 40ms window == 40ms interval = 100% radio duty cycle
  scan->setInterval(40);
  scan->setWindow(40);

  // 0 = scan forever, non-blocking
  scan->start(0, nullptr, false);

  Serial.println("Scan running. Waiting for packets...");
  Serial.println();
}

void loop() {
  static uint32_t lastPrint = 0;
  uint32_t now = millis();

  // Heartbeat every 3 seconds so you know it's alive
  if (now - lastPrint >= 3000) {
    lastPrint = now;
    Serial.print("---- [ALIVE] Total packets received: ");
    Serial.print(packetCount);
    Serial.println(" ----");
  }

  delay(10);
}
```
{% endcode %}
