# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from keka_hr_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    CONNECT_TOKEN = "/connect/token"
    HRIS_EMPLOYEES = "/hris/employees"
    HRIS_EMPLOYEES_ID = "/hris/employees/{id}"
    HRIS_EMPLOYEES_ID_PERSONALDETAILS = "/hris/employees/{id}/personaldetails"
    HRIS_EMPLOYEES_ID_JOBDETAILS = "/hris/employees/{id}/jobdetails"
    HRIS_EMPLOYEES_UPDATEFIELDS = "/hris/employees/updatefields"
    HRIS_GROUPS = "/hris/groups"
    HRIS_GROUPTYPES = "/hris/grouptypes"
    HRIS_DEPARTMENTS = "/hris/departments"
    HRIS_LOCATIONS = "/hris/locations"
    HRIS_JOBTITLES = "/hris/jobtitles"
    HRIS_CURRENCIES = "/hris/currencies"
    HRIS_NOTICEPERIODS = "/hris/noticeperiods"
    TIME_LEAVETYPES = "/time/leavetypes"
    TIME_LEAVEBALANCE = "/time/leavebalance"
    TIME_LEAVEREQUESTS = "/time/leaverequests"
    TIME_ATTENDANCE = "/time/attendance"
    TIME_CAPTURESCHEME = "/time/capturescheme"
    TIME_HOLIDAYSCALENDAR = "/time/holidayscalendar"
    PAYROLL_SALARYCOMPONENTS = "/payroll/salarycomponents"
    PAYROLL_PAYGROUPS = "/payroll/paygroups"
    PAYROLL_PAYGROUPS_PAY_GROUP_ID_PAYCYCLES = "/payroll/paygroups/{payGroupId}/paycycles"
    PAYROLL_PAYGROUPS_PAY_GROUP_ID_PAYCYCLES_PAY_CYCLE_ID_PAYREGISTER = "/payroll/paygroups/{payGroupId}/paycycles/{payCycleId}/payregister"
    PAYROLL_PAYGROUPS_PAY_GROUP_ID_PAYCYCLES_PAY_CYCLE_ID_PAYBATCHES = "/payroll/paygroups/{payGroupId}/paycycles/{payCycleId}/paybatches"
    PAYROLL_PAYGROUPS_PAY_GROUP_ID_PAYCYCLES_PAY_CYCLE_ID_PAYBATCHES_PAY_BATCH_ID_PAYMENTS = "/payroll/paygroups/{payGroupId}/paycycles/{payCycleId}/paybatches/{payBatchId}/payments"
    PAYROLL_PAYGRADES = "/payroll/paygrades"
    PAYROLL_PAYBANDS = "/payroll/paybands"
    PSA_CLIENTS = "/psa/clients"
    PSA_CLIENTS_ID = "/psa/clients/{id}"
    PSA_PROJECTS_PROJECT_ID_PHASES = "/psa/projects/{projectId}/phases"
    PSA_PROJECTS = "/psa/projects"
    PSA_PROJECTS_ID = "/psa/projects/{id}"
    PSA_PROJECTS_ID_ALLOCATIONS = "/psa/projects/{id}/allocations"
    PSA_PROJECTS_ID_TIMEENTRIES = "/psa/projects/{id}/timeentries"
    PSA_PROJECTS_PROJECT_ID_TASKS = "/psa/projects/{projectId}/tasks"
    PSA_PROJECTS_PROJECT_ID_TASKS_TASK_ID = "/psa/projects/{projectId}/tasks/{taskId}"
    PSA_PROJECTS_PROJECT_ID_TASKS_TASK_ID_TIMEENTRIES = "/psa/projects/{projectId}/tasks/{taskId}/timeentries"
    PSA_TIMEENTRIES = "/psa/timeentries"
    PMS_TIMEFRAMES = "/pms/timeframes"
    PMS_GOALS = "/pms/goals"
    PMS_GOALS_GOAL_ID_PROGRESS = "/pms/goals/{goalId}/progress"
    PMS_BADGES = "/pms/badges"
    PMS_PRAISE = "/pms/praise"
    V1_HIRE_JOBS = "/v1/hire/jobs"
    V1_HIRE_JOBS_JOB_ID_APPLICATIONFIELDS = "/v1/hire/jobs/{jobId}/applicationfields"
    V1_HIRE_JOBS_JOB_ID_CANDIDATES = "/v1/hire/jobs/{jobId}/candidates"
    V1_HIRE_JOBS_JOB_ID_CANDIDATE_CANDIDATE_ID = "/v1/hire/jobs/{jobId}/candidate/{candidateId}"
    V1_HIRE_JOBS_JOB_ID_CANDIDATE_CANDIDATE_ID_NOTES = "/v1/hire/jobs/{jobId}/candidate/{candidateId}/notes"
    V1_HIRE_JOBS_JOB_ID_CANDIDATE = "/v1/hire/jobs/{jobId}/candidate"
    V1_HIRE_JOBS_JOB_ID_CANDIDATE_CANDIDATE_ID_INTERVIEWS = "/v1/hire/jobs/{jobId}/candidate/{candidateId}/interviews"
    V1_HIRE_JOBS_JOB_ID_CANDIDATE_CANDIDATE_ID_SCORECARDS = "/v1/hire/jobs/{jobId}/candidate/{candidateId}/scorecards"
    V1_HIRE_TALENTPOOL = "/v1/hire/talentpool"
    V1_HIRE_TALENTPOOL_TALENT_POOL_ID_APPLICATIONFIELDS = "/v1/hire/talentpool/{talentPoolId}/applicationfields"
    V1_HIRE_TALENTPOOL_TALENT_POOL_ID_CANDIDATES = "/v1/hire/talentpool/{talentPoolId}/candidates"
    V1_HIRE_TALENTPOOL_TALENT_POOL_ID_CANDIDATE = "/v1/hire/talentpool/{talentPoolId}/candidate"
    EXPENSE_CATEGORIES = "/expense/categories"
    EXPENSE_CLAIMS = "/expense/claims"
    EXPENSEPOLICIES = "/expensepolicies"
    ASSETS = "/assets"
    ASSETS_TYPES = "/assets/types"
    ASSETS_CATEGORIES = "/assets/categories"
    ASSETS_CONDITIONS = "/assets/conditions"
    REQUISITION_REQUESTS = "/requisition/requests"
