from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse

from app.domains.email.email_service import EmailService
from app.ports.email.api.email_deps import get_service
from app.ports.email.api.email_responses import EmailResponse

router = APIRouter(prefix="/api/email", tags=["email"])


@router.get(
    "/guess",
    response_model=EmailResponse,
    responses={
        200: {"model": EmailResponse, "description": "Guessed email of the contact"},
        400: {"description": "Email guess operation failed"},
    },
)
async def guess_email(
    fullname: str, domain: str, service: Annotated[EmailService, Depends(get_service)]
) -> JSONResponse:
    if fullname is None and domain is None:
        raise HTTPException(status_code=400, detail="Email can not be guessed")
    email = service.get_email_by_full_name_and_domain(fullname, domain)
    if email is None:
        raise HTTPException(status_code=400, detail="Email can not be guessed")
    return JSONResponse({"email": email})
