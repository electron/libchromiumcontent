import argparse
import os
import subprocess
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-o', dest='out')
parser.add_argument('-s', dest='stamp')
parser.add_argument('-t', dest='target_cpu')
args = parser.parse_args()

def gen_list(out, name, obj_dirs):
    out.write(name + " = [\n")
    for base_dir in obj_dirs:
        for dir, subdirs, files in os.walk(os.path.join('obj', base_dir)):
            for f in files:
                if f.endswith('.obj') or f.endswith('.o'):
                    out.write('"' + os.path.abspath(os.path.join(dir, f)) + '",\n')
    out.write("]\n")

with open(args.out, 'w') as out:
    additional_libchromiumcontent = []
    if sys.platform in ['win32', 'cygwin'] and args.target_cpu == "x64":
        additional_libchromiumcontent = [
            "../clang_x64/obj/third_party/libyuv",
        ]
    gen_list(
        out,
        "obj_libchromiumcontent",
        [
            "build",
            "chrome/browser/ui/libgtkui",
            "content",
            "crypto",
            "dbus",
            "device",
            "gin",
            "google_apis",
            "gpu",
            "ipc",
            "jingle",
            "mojo",
            "pdf",
            "printing",
            "sandbox",
            "sdch",
            "sql/sql",
            "storage",
            "third_party/adobe",
            "third_party/boringssl",
            "third_party/brotli/common",
            "third_party/brotli/dec",
            "third_party/ced/ced",
            "third_party/crc32c",  # for "third_party/leveldatabase"
            "third_party/decklink",
            "third_party/expat",
            "third_party/flac",
            "third_party/harfbuzz-ng",
            "third_party/iaccessible2",
            "third_party/iccjpeg",
            "third_party/isimpledom",
            "third_party/leveldatabase",
            "third_party/libdrm",
            "third_party/libXNVCtrl",
            "third_party/libjingle",
            "third_party/libjpeg_turbo",
            "third_party/libpng",
            "third_party/libsrtp",
            "third_party/libusb",
            "third_party/libvpx",
            "third_party/libwebm",
            "third_party/libwebp",
            "third_party/libxml",
            "third_party/libxslt",
            "third_party/libyuv",
            "third_party/mesa",
            "third_party/modp_b64",
            "third_party/mozilla",
            "third_party/openh264",
            "third_party/openmax_dl",
            "third_party/opus",
            "third_party/ots",
            "third_party/protobuf/protobuf_lite",
            "third_party/qcms",
            "third_party/re2",
            "third_party/sfntly",
            "third_party/smhasher",
            "third_party/snappy",
            "third_party/sqlite",
            "third_party/sudden_motion_sensor",
            "third_party/usrsctp",
            "third_party/woff2",
            "third_party/zlib",
            "tools",
            "ui",
            "url",
        ] + additional_libchromiumcontent)

    gen_list(
        out,
        "obj_base",
        [
            "base",
        ])

    gen_list(
        out,
        "obj_cc",
        [
            "cc/animation",
            "cc/base",
            "cc/blink",
            "cc/cc",
            "cc/debug",
            "cc/ipc",
            "cc/paint",
            "cc/proto",
            "cc/surfaces",
        ])

    gen_list(
        out,
        "obj_components",
        [
            "components/bitmap_uploader",
            "components/cdm",
            "components/cookie_config",
            "components/crash/core/common",
            "components/device_event_log",
            "components/discardable_memory",
            "components/display_compositor",
            "components/filesystem",
            "components/leveldb",
            "components/link_header_util",
            "components/memory_coordinator",
            "components/metrics/public/interfaces",
            "components/metrics/single_sample_metrics",
            "components/mime_util",
            "components/mus/clipboard",
            "components/mus/common",
            "components/mus/gles2",
            "components/mus/gpu",
            "components/mus/input_devices",
            "components/mus/public",
            "components/network_session_configurator/browser",
            "components/network_session_configurator/common",
            "components/os_crypt",
            "components/payments",
            "components/prefs",
            "components/rappor",
            "components/scheduler/common",
            "components/scheduler/scheduler",
            "components/security_state",
            "components/tracing/proto",
            "components/tracing/startup_tracing",
            "components/tracing/tracing",
            "components/url_formatter",
            "components/variations",
            "components/vector_icons",
            "components/viz/client",
            "components/viz/common",
            "components/viz/hit_test",
            "components/viz/host",
            "components/viz/service/service",
            "components/webcrypto",
            "components/webmessaging",
        ])

    gen_list(
        out,
        "obj_ppapi",
        [
            "ppapi/cpp/objects",
            "ppapi/cpp/private",
            "ppapi/host",
            "ppapi/proxy",
            "ppapi/shared_impl",
            "ppapi/thunk",
        ])

    gen_list(
        out,
        "obj_media",
        [
            "media",
        ])

    gen_list(
        out,
        "obj_net",
        [
            "net/base",
            "net/constants",
            "net/extras",
            "net/http_server",
            "net/net",
            "net/net_with_v8",
        ])

    gen_list(
        out,
        "obj_services",
        [
            "services/catalog",
            "services/data_decoder",
            "services/device",
            "services/file",
            "services/metrics/public",
            "services/network/public",
            "services/resource_coordinator",
            "services/service_manager/background",
            "services/service_manager/embedder",
            "services/service_manager/public/cpp/cpp",
            "services/service_manager/public/cpp/cpp_types",
            "services/service_manager/public/cpp/standalone_service/standalone_service",
            "services/service_manager/public/interfaces",
            "services/service_manager/runner",
            "services/service_manager/service_manager",
            "services/service_manager/standalone",
            "services/shape_detection",
            "services/shell/public",
            "services/shell/runner",
            "services/shell/shell",
            "services/tracing/public",
            "services/ui/public",
            "services/ui/gpu",
            "services/user",
            "services/video_capture",
            "services/viz/privileged/interfaces",
            "services/viz/public/interfaces",
        ])

    gen_list(
        out,
        "obj_skia",
        [
            "skia",
        ])

    gen_list(
        out,
        "obj_angle",
        [
            "third_party/angle/angle_common",
            "third_party/angle/angle_gpu_info_util",
            "third_party/angle/angle_image_util",
            "third_party/angle/libANGLE",
            "third_party/angle/libEGL",
            "third_party/angle/libGLESv2",
            "third_party/angle/preprocessor",
            "third_party/angle/src/third_party/libXNVCtrl",
            "third_party/angle/src/vulkan_support/glslang",
            "third_party/angle/src/vulkan_support/vulkan_loader",
            "third_party/angle/translator",
            "third_party/angle/translator_lib",
        ])

    gen_list(
        out,
        "obj_pdfium",
        [
            "third_party/freetype",
            "third_party/pdfium",
        ])

    gen_list(
        out,
        "obj_webkit",
        [
            "third_party/WebKit/common",
            "third_party/WebKit/public",
            "third_party/WebKit/Source/core",
            "third_party/WebKit/Source/controller",
            "third_party/WebKit/Source/platform/heap",
            "third_party/WebKit/Source/platform/blink_common",
            "third_party/WebKit/Source/platform/instrumentation",
            "third_party/WebKit/Source/platform/loader",
            "third_party/WebKit/Source/platform/mojo",
            "third_party/WebKit/Source/platform/platform",
            "third_party/WebKit/Source/platform/scheduler",
            "third_party/WebKit/Source/platform/wtf",
            "third_party/WebKit/Source/web",
        ])

    gen_list(
        out,
        "obj_webkitbindings",
        [
            "third_party/WebKit/Source/bindings",
        ])

    gen_list(
        out,
        "obj_webkitmodules",
        [
            "third_party/WebKit/Source/modules",
        ])

    gen_list(
        out,
        "obj_webrtc",
        [
            "third_party/webrtc",
            "third_party/webrtc_overrides",
        ])

    gen_list(
        out,
        "obj_v8",
        [
            "v8/src/inspector",
            "v8/v8_base",
            "v8/v8_external_snapshot",
            "v8/v8_libbase",
            "v8/v8_libplatform",
            "v8/v8_libsampler",
            "third_party/icu",
        ])

open(args.stamp, 'w')
