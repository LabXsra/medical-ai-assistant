from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from services.nlp.pipeline import analyze_patient
from services.ml.predictor import predict_disease
from services.rag.pipeline import RAGPipeline


# ==========================================================
# FastAPI
# ==========================================================

app = FastAPI(
    title="Medical AI Assistant",
    version="3.0.0"
)


# ==========================================================
# Load RAG Pipeline (Loads Once)
# ==========================================================

print("=" * 60)
print("Loading Medical RAG Pipeline...")
print("=" * 60)

rag = RAGPipeline()

print("=" * 60)
print("Medical AI Assistant Ready!")
print("=" * 60)


# ==========================================================
# Templates
# ==========================================================

templates = Jinja2Templates(
    directory="frontend/templates"
)


# ==========================================================
# Static Files
# ==========================================================

app.mount(
    "/static",
    StaticFiles(directory="frontend/static"),
    name="static"
)


# ==========================================================
# Home
# ==========================================================

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


# ==========================================================
# Health
# ==========================================================

@app.get("/health")
async def health():

    return {

        "status": "Healthy",

        "version": "3.0.0",

        "services": {

            "clinical_nlp": "Running",

            "machine_learning": "Running",

            "rag_pipeline": "Running",

            "llama3.2": "Connected"

        }

    }


# ==========================================================
# About
# ==========================================================

@app.get("/about")
async def about():

    return {

        "project": "Medical AI Assistant",

        "developer": "Asra",

        "version": "3.0.0",

        "features": [

            "Clinical NLP",

            "Biomedical Transformer",

            "Hybrid NLP",

            "Ontology Mapping",

            "Machine Learning",

            "Disease Prediction",

            "Semantic Search",

            "FAISS Vector Database",

            "Retrieval-Augmented Generation",

            "Llama 3.2"

        ]

    }


# ==========================================================
# Request Model
# ==========================================================

class PatientInput(BaseModel):

    message: str


# ==========================================================
# Analyze Endpoint
# ==========================================================

@app.post("/analyze")
async def analyze(patient: PatientInput):

    try:

        # ==================================================
        # Clinical NLP
        # ==================================================

        analysis = analyze_patient(patient.message)

        age = analysis.get("age")

        if age is None:
            age = 30

        symptoms = []

        for symptom in analysis.get("symptoms", []):

            if symptom.get("present", True):

                symptoms.append(
                    symptom["name"]
                )

        # ==================================================
        # Machine Learning Prediction
        # ==================================================

        predictions = predict_disease(

            age=age,

            symptoms=symptoms

        )

        # ==================================================
        # Retrieval-Augmented Generation
        # ==================================================

        rag_result = rag.answer_question(

            patient.message

        )

        # ==================================================
        # Sources
        # ==================================================

        rag_sources = []

        for chunk in rag_result["retrieved_chunks"]:

            rag_sources.append({

                "disease": chunk["disease"],

                "chunk_id": chunk["chunk_id"],

                "distance": round(

                    chunk["distance"],

                    4

                )

            })

        # ==================================================
        # Response
        # ==================================================

        return {

            "success": True,

            "input": patient.message,

            "analysis": analysis,

            "predictions": predictions,

            "rag": {

                "answer": rag_result["generated_answer"],

                "sources": rag_sources

            }

        }

    except Exception as e:

        return {

            "success": False,

            "error": str(e)

        }


# ==========================================================
# Root API
# ==========================================================

@app.get("/api")
async def api():

    return {

        "message": "Medical AI Assistant API",

        "version": "3.0.0"

    }



