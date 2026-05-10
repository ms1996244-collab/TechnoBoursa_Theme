import os
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

def deploy():
    print("🚀 جاري بدء عملية الاتصال بمدونة تكنو بورصة...")
    
    # جلب البيانات من بيئة GitHub
    blog_id = os.environ.get('BLOG_ID')
    refresh_token = os.environ.get('GOOGLE_REFRESH_TOKEN')
    client_id = os.environ.get('GOOGLE_CLIENT_ID')
    client_secret = os.environ.get('GOOGLE_CLIENT_SECRET')

    creds = Credentials(
        token=None,
        refresh_token=refresh_token,
        client_id=client_id,
        client_secret=client_secret,
        token_uri="https://oauth2.googleapis.com/token"
    )

    try:
        service = build('blogger', 'v3', credentials=creds)
        # اختبار الاتصال عبر جلب معلومات المدونة
        blog = service.blogs().get(blogId=blog_id).execute()
        print(f"✅ تم الاتصال بنجاح بمدونة: {blog['name']}")
        print(f"🔗 الرابط الحالي: {blog['url']}")
        
    except Exception as e:
        print(f"❌ حدث خطأ أثناء الاتصال: {e}")
        exit(1)

if __name__ == "__main__":
    deploy()