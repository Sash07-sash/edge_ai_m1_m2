# M1 Assessment Criterion 2: OpenCV Pipeline Implementation

**Assessment Item:** 02_opencv_pipeline
**Mark Weighting:** 4 Marks
**Status:** Complete & Verified

---

## 1. Overview

This module documents the real-time computer vision pipeline responsible for frame ingestion, preprocessing, letterbox transformation, HUD overlay rendering, and post-inference bounding box visualization.

For the comprehensive technical analysis of each detection scenario, refer to:
* **Dedicated Pipeline Report:** [`M1_OpenCV_Pipeline_Report.md`](./M1_OpenCV_Pipeline_Report.md)

---

## 2. Live OpenCV Detection Screenshots

The pipeline captures and annotates genuine edge frames in real time:

| Evidence Screenshot | Detection Description | Telemetry Metrics |
| :---: | :--- | :--- |
| ![High Conf Detection](./detection_screenshots/opencv_det_01_high_confidence_enclosure.jpg) | **Single Enclosure Detection:** High-confidence center alignment on bench setup ([Inspect](./detection_screenshots/opencv_det_01_high_confidence_enclosure.jpg)) | **Confidence:** 72.1%<br>**Latency:** 272.7 ms<br>**FPS:** 3.5 FPS |
| ![Handheld Detection](./detection_screenshots/opencv_det_02_handheld_enclosure.jpg) | **Handheld Enclosure:** Stable box tracking omitting holding fingers ([Inspect](./detection_screenshots/opencv_det_02_handheld_enclosure.jpg)) | **Confidence:** 64.8%<br>**Latency:** 283.3 ms<br>**FPS:** 3.5 FPS |
| ![Bench Telemetry Detection](./detection_screenshots/opencv_det_03_multi_instance_detection.jpg) | **Bench Telemetry Detection:** Real-time tracking with sustained frame rate ([Inspect](./detection_screenshots/opencv_det_03_multi_instance_detection.jpg)) | **Confidence:** 78.1%<br>**Latency:** 270.8 ms<br>**FPS:** 3.5 FPS |
| ![Angled Detection](./detection_screenshots/opencv_det_04_angled_enclosure_perspective.jpg) | **Angled Perspective:** Geometric invariance under active bench testing ([Inspect](./detection_screenshots/opencv_det_04_angled_enclosure_perspective.jpg)) | **Confidence:** 72.1%<br>**Latency:** 272.7 ms<br>**FPS:** 3.5 FPS |
| ![Background Scan](./detection_screenshots/opencv_det_05_background_scanning_no_false_positive.jpg) | **Zero False Positives:** Clean background scanning ([Inspect](./detection_screenshots/opencv_det_05_background_scanning_no_false_positive.jpg)) | **Status:** SCANNING<br>**Detections:** 0<br>**FP Rate:** 0.0% |

---

## 3. Key Pipeline Artifacts

- **Detailed Technical Report:** [`M1_OpenCV_Pipeline_Report.md`](./M1_OpenCV_Pipeline_Report.md)
- **Organized Detection Screenshots:** [`detection_screenshots/`](./detection_screenshots/)
- **Inference & Pipeline Driver:** [`src/detect.py`](../../../src/detect.py)
- **Visualizer & Telemetry HUD:** [`src/utils.py`](../../../src/utils.py)
- **Desktop Launcher:** [`run_webcam.bat`](../../../run_webcam.bat)
- **Roboflow v3 Launcher:** [`run_webcam_roboflow_v3.bat`](../../../run_webcam_roboflow_v3.bat)
