from fastapi import FastAPI
app = FastAPI(
    title='smart Summarizer API',
    description="AI-powered scientific research assistant",
    version="1.0.0"
)
@app.get('/')
def home():
    return {
        'message':'Smart Summarizer API is running',
        'status':'success'
    }
@app.get('/health')
def health():
    return {
        'status':'healthy'
    }