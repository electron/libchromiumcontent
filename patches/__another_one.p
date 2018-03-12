diff --git a/chrome/browser/chrome_content_browser_client.cc b/chrome/browser/chrome_content_browser_client.cc
index 48f9d3975ffe..861d54282cae 100644
--- a/chrome/browser/chrome_content_browser_client.cc
+++ b/chrome/browser/chrome_content_browser_client.cc
@@ -2253,6 +2253,8 @@ bool ChromeContentBrowserClient::CanCreateWindow(
     const std::string& frame_name,
     WindowOpenDisposition disposition,
     const blink::mojom::WindowFeatures& features,
+    const std::vector<std::string>& additional_features,
+    const scoped_refptr<content::ResourceRequestBody>& body,
     bool user_gesture,
     bool opener_suppressed,
     bool* no_javascript_access) {
diff --git a/chrome/browser/chrome_content_browser_client.h b/chrome/browser/chrome_content_browser_client.h
index e5220bc834ca..5ec9d8fea4bf 100644
--- a/chrome/browser/chrome_content_browser_client.h
+++ b/chrome/browser/chrome_content_browser_client.h
@@ -213,6 +213,8 @@ class ChromeContentBrowserClient : public content::ContentBrowserClient {
                        const std::string& frame_name,
                        WindowOpenDisposition disposition,
                        const blink::mojom::WindowFeatures& features,
+                       const std::vector<std::string>& additional_features,
+                       const scoped_refptr<content::ResourceRequestBody>& body,
                        bool user_gesture,
                        bool opener_suppressed,
                        bool* no_javascript_access) override;
diff --git a/content/shell/browser/layout_test/layout_test_content_browser_client.cc b/content/shell/browser/layout_test/layout_test_content_browser_client.cc
index 3a4fab7568d4..4f9178da3363 100644
--- a/content/shell/browser/layout_test/layout_test_content_browser_client.cc
+++ b/content/shell/browser/layout_test/layout_test_content_browser_client.cc
@@ -175,6 +175,8 @@ bool LayoutTestContentBrowserClient::CanCreateWindow(
     const std::string& frame_name,
     WindowOpenDisposition disposition,
     const blink::mojom::WindowFeatures& features,
+    const std::vector<std::string>& additional_features,
+    const scoped_refptr<content::ResourceRequestBody>& body,
     bool user_gesture,
     bool opener_suppressed,
     bool* no_javascript_access) {
diff --git a/content/shell/browser/layout_test/layout_test_content_browser_client.h b/content/shell/browser/layout_test/layout_test_content_browser_client.h
index 310c72792004..69d6c1460999 100644
--- a/content/shell/browser/layout_test/layout_test_content_browser_client.h
+++ b/content/shell/browser/layout_test/layout_test_content_browser_client.h
@@ -58,6 +58,8 @@ class LayoutTestContentBrowserClient : public ShellContentBrowserClient {
                        const std::string& frame_name,
                        WindowOpenDisposition disposition,
                        const blink::mojom::WindowFeatures& features,
+                       const std::vector<std::string>& additional_features,
+                       const scoped_refptr<content::ResourceRequestBody>& body,
                        bool user_gesture,
                        bool opener_suppressed,
                        bool* no_javascript_access) override;
