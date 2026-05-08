import os
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

def push_to_blogger():
    # جلب البيانات من بيئة GitHub (Secrets)
    blog_id = os.environ.get('BLOG_ID')
    refresh_token = os.environ.get('GOOGLE_REFRESH_TOKEN')
    client_id = os.environ.get('GOOGLE_CLIENT_ID')
    client_secret = os.environ.get('GOOGLE_CLIENT_SECRET')

    # إعداد الصلاحيات
    creds = Credentials(
        token=None,
        refresh_token=refresh_token,
        client_id=client_id,
        client_secret=client_secret,
        token_uri="https://oauth2.googleapis.com/token"
    )

    try:
        service = build('blogger', 'v3', credentials=creds)
        
        # قراءة القالب المجمع من مجلد dist
        with open('dist/final_theme.xml', 'r', encoding='utf-8') as f:
            theme_content = f.read()

        # تحديث المظهر في بلوجر
        print(f"🚀 جاري الرفع إلى المدونة: {blog_id}...")
        service.themes().update(
            blogId=blog_id,
            body={'content': theme_content}
        ).execute()
        
        print("✅ تم تحديث مظهر تكنو بورصة بنجاح عبر GitHub Actions!")

    except Exception as e:
        print(f"❌ حدث خطأ أثناء الرفع: {str(e)}")
        exit(1)

if __name__ == "__main__":
    push_to_blogger()