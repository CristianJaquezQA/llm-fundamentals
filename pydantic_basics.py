from typing import Optional, Literal, Any
from pydantic import BaseModel, Field, EmailStr, ValidationError


class TestResult(BaseModel):
    test_id: str = Field(
        pattern=r"^TC-\d{3}$"
    )
    name: str = Field(min_length=5)
    status: Literal["passed", "failed", "skipped"]
    duration_ms: int = Field(ge=0)
    retries: int = Field(default=0, ge=0, le=3)
    error_message: Optional[str] = None

class BugReport(BaseModel):
    title: str = Field(min_length=10,
                       max_length = 200)
    severity: Literal["critical","high","medium","low"]
    steps_to_reproduce: list[str] = Field(min_length=1)
    reporter_email: EmailStr
    affected_versions: list[str]

class ApiResponse(BaseModel):
    status_code: int = Field(ge=100, le=599)
    body: dict[str,Any]
    latency_ms: float = Field(gt=0)
    headers: dict[str,str] = Field(default_factory=dict)



try:
    valid_result = TestResult(
        test_id= "TC-001",
        name= "Login Test",
        status= "passed",
        duration_ms= 1250,
        retries= 1
    )
    print("Caso válido 1 Test Result:")
    print(valid_result)
except ValidationError as e:
    print("\nCaso inválido:")
    print(e)

try:
    valid_result = TestResult(
        test_id= "TC-00T",
        name= "Login Test",
        status= "passed",
        duration_ms= 1250,
        retries= 1
    )
except ValidationError as e:
    print("\nCaso inválido 1 Test Result:")
    print(e)

try:
    valid_result = TestResult(
        test_id="TC-001",
        name="Login Test",
        status="unknown",
        duration_ms=1250,
        retries=1
        )
except ValidationError as e:
    print("\nCaso inválido 2 Test Result:")
    print(e)

try:
    valid_result = TestResult(
        test_id="TC-001",
        name="Login Test",
        status="passed",
        duration_ms=1250,
        retries=10
        )

except ValidationError as e:
    print("\nCaso inválido 3 Test Result:")
    print(e)

try:
    valid_result = BugReport(
        title= "Login Test",
        severity= "critical",
        steps_to_reproduce= ["veinte"],
        reporter_email= "cristian@hotmail.com",
        affected_versions= ["diez"],
    )
    print("Caso válido 1 BugReport:")
    print(valid_result)
except ValidationError as e:
    print("\nCaso inválido")
    print(e)

try:
    valid_result = BugReport(
        title= "Login Test",
        severity= "critical",
        steps_to_reproduce= ["veinte"],
        reporter_email= "esto-no-es-un-email",
        affected_versions= ["diez"],
    )
except ValidationError as e:
    print("\nCaso inválido 1 BugReport:")
    print(e)

try:
    valid_result = BugReport(
        title= "Login Test",
        severity= "critical",
        steps_to_reproduce= ["veinte"],
        reporter_email= "cristian@test.com",
        affected_versions= [10],
    )
except ValidationError as e:
    print("\nCaso inválido 2 BugReport:")
    print(e)


try:
    valid_result = BugReport(
        title= "Login Test",
        severity= "Lower",
        steps_to_reproduce= ["veinte"],
        reporter_email= "cristian@hotmail.com",
        affected_versions= ["diez"],
    )
except ValidationError as e:
    print("\nCaso inválido 3 BugReport:")
    print(e)


try:
    valid_result = ApiResponse(
        status_code=200,
        body= {"user_id": 42, "name": "Cristian", "active": True, "tags": ["qa", "automation"]},
        latency_ms= 100,
        headers= {"Content-Type": "application/json", "X-Request-Id": "abc-123"}
    )
    print("Caso válido ApiResponse:")
    print(valid_result)
except ValidationError as e:
    print("\nCaso inválido")
    print(e)

try:
    valid_result = ApiResponse(
        status_code=99,
        body= {"user_id": 42, "name": "Cristian", "active": False},
        latency_ms= 100,
        headers= {"Content-Type": "application/json", "X-Request-Id": "abc-123"}
    )
    print("Caso válido ApiResponse:")
    print(valid_result)
except ValidationError as e:
    print("\nCaso inválido 1 ApiResponse:")
    print(e)

try:
    valid_result = ApiResponse(
        status_code=404,
        body= {"user_id": "10", "name": "Cristian", "active": False},
        latency_ms= 0,
        headers= {"Content-Type": "application/json", "X-Request-Id": "abc-123"}
    )
    print("Caso válido ApiResponse:")
    print(valid_result)
except ValidationError as e:
    print("\nCaso inválido 2 ApiResponse:")
    print(e)

try:
    valid_result = ApiResponse(
        status_code=404,
        body= {"user_id": "10", "name": "Cristian", "active": False},
        latency_ms= 100,
        headers= {"Content-Type": "application/json", "X-Request-Id": "abc-123","user-agent":100}
    )
    print("Caso válido ApiResponse:")
    print(valid_result)
except ValidationError as e:
    print("\nCaso inválido 3 ApiResponse:")
    print(e)