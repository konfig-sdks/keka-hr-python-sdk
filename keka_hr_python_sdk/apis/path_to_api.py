import typing_extensions

from keka_hr_python_sdk.paths import PathValues
from keka_hr_python_sdk.apis.paths.connect_token import ConnectToken
from keka_hr_python_sdk.apis.paths.hris_employees import HrisEmployees
from keka_hr_python_sdk.apis.paths.hris_employees_id import HrisEmployeesId
from keka_hr_python_sdk.apis.paths.hris_employees_id_personaldetails import HrisEmployeesIdPersonaldetails
from keka_hr_python_sdk.apis.paths.hris_employees_id_jobdetails import HrisEmployeesIdJobdetails
from keka_hr_python_sdk.apis.paths.hris_employees_updatefields import HrisEmployeesUpdatefields
from keka_hr_python_sdk.apis.paths.hris_groups import HrisGroups
from keka_hr_python_sdk.apis.paths.hris_grouptypes import HrisGrouptypes
from keka_hr_python_sdk.apis.paths.hris_departments import HrisDepartments
from keka_hr_python_sdk.apis.paths.hris_locations import HrisLocations
from keka_hr_python_sdk.apis.paths.hris_jobtitles import HrisJobtitles
from keka_hr_python_sdk.apis.paths.hris_currencies import HrisCurrencies
from keka_hr_python_sdk.apis.paths.hris_noticeperiods import HrisNoticeperiods
from keka_hr_python_sdk.apis.paths.time_leavetypes import TimeLeavetypes
from keka_hr_python_sdk.apis.paths.time_leavebalance import TimeLeavebalance
from keka_hr_python_sdk.apis.paths.time_leaverequests import TimeLeaverequests
from keka_hr_python_sdk.apis.paths.time_attendance import TimeAttendance
from keka_hr_python_sdk.apis.paths.time_capturescheme import TimeCapturescheme
from keka_hr_python_sdk.apis.paths.time_holidayscalendar import TimeHolidayscalendar
from keka_hr_python_sdk.apis.paths.payroll_salarycomponents import PayrollSalarycomponents
from keka_hr_python_sdk.apis.paths.payroll_paygroups import PayrollPaygroups
from keka_hr_python_sdk.apis.paths.payroll_paygroups_pay_group_id_paycycles import PayrollPaygroupsPayGroupIdPaycycles
from keka_hr_python_sdk.apis.paths.payroll_paygroups_pay_group_id_paycycles_pay_cycle_id_payregister import PayrollPaygroupsPayGroupIdPaycyclesPayCycleIdPayregister
from keka_hr_python_sdk.apis.paths.payroll_paygroups_pay_group_id_paycycles_pay_cycle_id_paybatches import PayrollPaygroupsPayGroupIdPaycyclesPayCycleIdPaybatches
from keka_hr_python_sdk.apis.paths.payroll_paygroups_pay_group_id_paycycles_pay_cycle_id_paybatches_pay_batch_id_payments import PayrollPaygroupsPayGroupIdPaycyclesPayCycleIdPaybatchesPayBatchIdPayments
from keka_hr_python_sdk.apis.paths.payroll_paygrades import PayrollPaygrades
from keka_hr_python_sdk.apis.paths.payroll_paybands import PayrollPaybands
from keka_hr_python_sdk.apis.paths.psa_clients import PsaClients
from keka_hr_python_sdk.apis.paths.psa_clients_id import PsaClientsId
from keka_hr_python_sdk.apis.paths.psa_projects_project_id_phases import PsaProjectsProjectIdPhases
from keka_hr_python_sdk.apis.paths.psa_projects import PsaProjects
from keka_hr_python_sdk.apis.paths.psa_projects_id import PsaProjectsId
from keka_hr_python_sdk.apis.paths.psa_projects_id_allocations import PsaProjectsIdAllocations
from keka_hr_python_sdk.apis.paths.psa_projects_id_timeentries import PsaProjectsIdTimeentries
from keka_hr_python_sdk.apis.paths.psa_projects_project_id_tasks import PsaProjectsProjectIdTasks
from keka_hr_python_sdk.apis.paths.psa_projects_project_id_tasks_task_id import PsaProjectsProjectIdTasksTaskId
from keka_hr_python_sdk.apis.paths.psa_projects_project_id_tasks_task_id_timeentries import PsaProjectsProjectIdTasksTaskIdTimeentries
from keka_hr_python_sdk.apis.paths.psa_timeentries import PsaTimeentries
from keka_hr_python_sdk.apis.paths.pms_timeframes import PmsTimeframes
from keka_hr_python_sdk.apis.paths.pms_goals import PmsGoals
from keka_hr_python_sdk.apis.paths.pms_goals_goal_id_progress import PmsGoalsGoalIdProgress
from keka_hr_python_sdk.apis.paths.pms_badges import PmsBadges
from keka_hr_python_sdk.apis.paths.pms_praise import PmsPraise
from keka_hr_python_sdk.apis.paths.v1_hire_jobs import V1HireJobs
from keka_hr_python_sdk.apis.paths.v1_hire_jobs_job_id_applicationfields import V1HireJobsJobIdApplicationfields
from keka_hr_python_sdk.apis.paths.v1_hire_jobs_job_id_candidates import V1HireJobsJobIdCandidates
from keka_hr_python_sdk.apis.paths.v1_hire_jobs_job_id_candidate_candidate_id import V1HireJobsJobIdCandidateCandidateId
from keka_hr_python_sdk.apis.paths.v1_hire_jobs_job_id_candidate_candidate_id_notes import V1HireJobsJobIdCandidateCandidateIdNotes
from keka_hr_python_sdk.apis.paths.v1_hire_jobs_job_id_candidate import V1HireJobsJobIdCandidate
from keka_hr_python_sdk.apis.paths.v1_hire_jobs_job_id_candidate_candidate_id_interviews import V1HireJobsJobIdCandidateCandidateIdInterviews
from keka_hr_python_sdk.apis.paths.v1_hire_jobs_job_id_candidate_candidate_id_scorecards import V1HireJobsJobIdCandidateCandidateIdScorecards
from keka_hr_python_sdk.apis.paths.v1_hire_talentpool import V1HireTalentpool
from keka_hr_python_sdk.apis.paths.v1_hire_talentpool_talent_pool_id_applicationfields import V1HireTalentpoolTalentPoolIdApplicationfields
from keka_hr_python_sdk.apis.paths.v1_hire_talentpool_talent_pool_id_candidates import V1HireTalentpoolTalentPoolIdCandidates
from keka_hr_python_sdk.apis.paths.v1_hire_talentpool_talent_pool_id_candidate import V1HireTalentpoolTalentPoolIdCandidate
from keka_hr_python_sdk.apis.paths.expense_categories import ExpenseCategories
from keka_hr_python_sdk.apis.paths.expense_claims import ExpenseClaims
from keka_hr_python_sdk.apis.paths.expensepolicies import Expensepolicies
from keka_hr_python_sdk.apis.paths.assets import Assets
from keka_hr_python_sdk.apis.paths.assets_types import AssetsTypes
from keka_hr_python_sdk.apis.paths.assets_categories import AssetsCategories
from keka_hr_python_sdk.apis.paths.assets_conditions import AssetsConditions
from keka_hr_python_sdk.apis.paths.requisition_requests import RequisitionRequests

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.CONNECT_TOKEN: ConnectToken,
        PathValues.HRIS_EMPLOYEES: HrisEmployees,
        PathValues.HRIS_EMPLOYEES_ID: HrisEmployeesId,
        PathValues.HRIS_EMPLOYEES_ID_PERSONALDETAILS: HrisEmployeesIdPersonaldetails,
        PathValues.HRIS_EMPLOYEES_ID_JOBDETAILS: HrisEmployeesIdJobdetails,
        PathValues.HRIS_EMPLOYEES_UPDATEFIELDS: HrisEmployeesUpdatefields,
        PathValues.HRIS_GROUPS: HrisGroups,
        PathValues.HRIS_GROUPTYPES: HrisGrouptypes,
        PathValues.HRIS_DEPARTMENTS: HrisDepartments,
        PathValues.HRIS_LOCATIONS: HrisLocations,
        PathValues.HRIS_JOBTITLES: HrisJobtitles,
        PathValues.HRIS_CURRENCIES: HrisCurrencies,
        PathValues.HRIS_NOTICEPERIODS: HrisNoticeperiods,
        PathValues.TIME_LEAVETYPES: TimeLeavetypes,
        PathValues.TIME_LEAVEBALANCE: TimeLeavebalance,
        PathValues.TIME_LEAVEREQUESTS: TimeLeaverequests,
        PathValues.TIME_ATTENDANCE: TimeAttendance,
        PathValues.TIME_CAPTURESCHEME: TimeCapturescheme,
        PathValues.TIME_HOLIDAYSCALENDAR: TimeHolidayscalendar,
        PathValues.PAYROLL_SALARYCOMPONENTS: PayrollSalarycomponents,
        PathValues.PAYROLL_PAYGROUPS: PayrollPaygroups,
        PathValues.PAYROLL_PAYGROUPS_PAY_GROUP_ID_PAYCYCLES: PayrollPaygroupsPayGroupIdPaycycles,
        PathValues.PAYROLL_PAYGROUPS_PAY_GROUP_ID_PAYCYCLES_PAY_CYCLE_ID_PAYREGISTER: PayrollPaygroupsPayGroupIdPaycyclesPayCycleIdPayregister,
        PathValues.PAYROLL_PAYGROUPS_PAY_GROUP_ID_PAYCYCLES_PAY_CYCLE_ID_PAYBATCHES: PayrollPaygroupsPayGroupIdPaycyclesPayCycleIdPaybatches,
        PathValues.PAYROLL_PAYGROUPS_PAY_GROUP_ID_PAYCYCLES_PAY_CYCLE_ID_PAYBATCHES_PAY_BATCH_ID_PAYMENTS: PayrollPaygroupsPayGroupIdPaycyclesPayCycleIdPaybatchesPayBatchIdPayments,
        PathValues.PAYROLL_PAYGRADES: PayrollPaygrades,
        PathValues.PAYROLL_PAYBANDS: PayrollPaybands,
        PathValues.PSA_CLIENTS: PsaClients,
        PathValues.PSA_CLIENTS_ID: PsaClientsId,
        PathValues.PSA_PROJECTS_PROJECT_ID_PHASES: PsaProjectsProjectIdPhases,
        PathValues.PSA_PROJECTS: PsaProjects,
        PathValues.PSA_PROJECTS_ID: PsaProjectsId,
        PathValues.PSA_PROJECTS_ID_ALLOCATIONS: PsaProjectsIdAllocations,
        PathValues.PSA_PROJECTS_ID_TIMEENTRIES: PsaProjectsIdTimeentries,
        PathValues.PSA_PROJECTS_PROJECT_ID_TASKS: PsaProjectsProjectIdTasks,
        PathValues.PSA_PROJECTS_PROJECT_ID_TASKS_TASK_ID: PsaProjectsProjectIdTasksTaskId,
        PathValues.PSA_PROJECTS_PROJECT_ID_TASKS_TASK_ID_TIMEENTRIES: PsaProjectsProjectIdTasksTaskIdTimeentries,
        PathValues.PSA_TIMEENTRIES: PsaTimeentries,
        PathValues.PMS_TIMEFRAMES: PmsTimeframes,
        PathValues.PMS_GOALS: PmsGoals,
        PathValues.PMS_GOALS_GOAL_ID_PROGRESS: PmsGoalsGoalIdProgress,
        PathValues.PMS_BADGES: PmsBadges,
        PathValues.PMS_PRAISE: PmsPraise,
        PathValues.V1_HIRE_JOBS: V1HireJobs,
        PathValues.V1_HIRE_JOBS_JOB_ID_APPLICATIONFIELDS: V1HireJobsJobIdApplicationfields,
        PathValues.V1_HIRE_JOBS_JOB_ID_CANDIDATES: V1HireJobsJobIdCandidates,
        PathValues.V1_HIRE_JOBS_JOB_ID_CANDIDATE_CANDIDATE_ID: V1HireJobsJobIdCandidateCandidateId,
        PathValues.V1_HIRE_JOBS_JOB_ID_CANDIDATE_CANDIDATE_ID_NOTES: V1HireJobsJobIdCandidateCandidateIdNotes,
        PathValues.V1_HIRE_JOBS_JOB_ID_CANDIDATE: V1HireJobsJobIdCandidate,
        PathValues.V1_HIRE_JOBS_JOB_ID_CANDIDATE_CANDIDATE_ID_INTERVIEWS: V1HireJobsJobIdCandidateCandidateIdInterviews,
        PathValues.V1_HIRE_JOBS_JOB_ID_CANDIDATE_CANDIDATE_ID_SCORECARDS: V1HireJobsJobIdCandidateCandidateIdScorecards,
        PathValues.V1_HIRE_TALENTPOOL: V1HireTalentpool,
        PathValues.V1_HIRE_TALENTPOOL_TALENT_POOL_ID_APPLICATIONFIELDS: V1HireTalentpoolTalentPoolIdApplicationfields,
        PathValues.V1_HIRE_TALENTPOOL_TALENT_POOL_ID_CANDIDATES: V1HireTalentpoolTalentPoolIdCandidates,
        PathValues.V1_HIRE_TALENTPOOL_TALENT_POOL_ID_CANDIDATE: V1HireTalentpoolTalentPoolIdCandidate,
        PathValues.EXPENSE_CATEGORIES: ExpenseCategories,
        PathValues.EXPENSE_CLAIMS: ExpenseClaims,
        PathValues.EXPENSEPOLICIES: Expensepolicies,
        PathValues.ASSETS: Assets,
        PathValues.ASSETS_TYPES: AssetsTypes,
        PathValues.ASSETS_CATEGORIES: AssetsCategories,
        PathValues.ASSETS_CONDITIONS: AssetsConditions,
        PathValues.REQUISITION_REQUESTS: RequisitionRequests,
    }
)

path_to_api = PathToApi(
    {
        PathValues.CONNECT_TOKEN: ConnectToken,
        PathValues.HRIS_EMPLOYEES: HrisEmployees,
        PathValues.HRIS_EMPLOYEES_ID: HrisEmployeesId,
        PathValues.HRIS_EMPLOYEES_ID_PERSONALDETAILS: HrisEmployeesIdPersonaldetails,
        PathValues.HRIS_EMPLOYEES_ID_JOBDETAILS: HrisEmployeesIdJobdetails,
        PathValues.HRIS_EMPLOYEES_UPDATEFIELDS: HrisEmployeesUpdatefields,
        PathValues.HRIS_GROUPS: HrisGroups,
        PathValues.HRIS_GROUPTYPES: HrisGrouptypes,
        PathValues.HRIS_DEPARTMENTS: HrisDepartments,
        PathValues.HRIS_LOCATIONS: HrisLocations,
        PathValues.HRIS_JOBTITLES: HrisJobtitles,
        PathValues.HRIS_CURRENCIES: HrisCurrencies,
        PathValues.HRIS_NOTICEPERIODS: HrisNoticeperiods,
        PathValues.TIME_LEAVETYPES: TimeLeavetypes,
        PathValues.TIME_LEAVEBALANCE: TimeLeavebalance,
        PathValues.TIME_LEAVEREQUESTS: TimeLeaverequests,
        PathValues.TIME_ATTENDANCE: TimeAttendance,
        PathValues.TIME_CAPTURESCHEME: TimeCapturescheme,
        PathValues.TIME_HOLIDAYSCALENDAR: TimeHolidayscalendar,
        PathValues.PAYROLL_SALARYCOMPONENTS: PayrollSalarycomponents,
        PathValues.PAYROLL_PAYGROUPS: PayrollPaygroups,
        PathValues.PAYROLL_PAYGROUPS_PAY_GROUP_ID_PAYCYCLES: PayrollPaygroupsPayGroupIdPaycycles,
        PathValues.PAYROLL_PAYGROUPS_PAY_GROUP_ID_PAYCYCLES_PAY_CYCLE_ID_PAYREGISTER: PayrollPaygroupsPayGroupIdPaycyclesPayCycleIdPayregister,
        PathValues.PAYROLL_PAYGROUPS_PAY_GROUP_ID_PAYCYCLES_PAY_CYCLE_ID_PAYBATCHES: PayrollPaygroupsPayGroupIdPaycyclesPayCycleIdPaybatches,
        PathValues.PAYROLL_PAYGROUPS_PAY_GROUP_ID_PAYCYCLES_PAY_CYCLE_ID_PAYBATCHES_PAY_BATCH_ID_PAYMENTS: PayrollPaygroupsPayGroupIdPaycyclesPayCycleIdPaybatchesPayBatchIdPayments,
        PathValues.PAYROLL_PAYGRADES: PayrollPaygrades,
        PathValues.PAYROLL_PAYBANDS: PayrollPaybands,
        PathValues.PSA_CLIENTS: PsaClients,
        PathValues.PSA_CLIENTS_ID: PsaClientsId,
        PathValues.PSA_PROJECTS_PROJECT_ID_PHASES: PsaProjectsProjectIdPhases,
        PathValues.PSA_PROJECTS: PsaProjects,
        PathValues.PSA_PROJECTS_ID: PsaProjectsId,
        PathValues.PSA_PROJECTS_ID_ALLOCATIONS: PsaProjectsIdAllocations,
        PathValues.PSA_PROJECTS_ID_TIMEENTRIES: PsaProjectsIdTimeentries,
        PathValues.PSA_PROJECTS_PROJECT_ID_TASKS: PsaProjectsProjectIdTasks,
        PathValues.PSA_PROJECTS_PROJECT_ID_TASKS_TASK_ID: PsaProjectsProjectIdTasksTaskId,
        PathValues.PSA_PROJECTS_PROJECT_ID_TASKS_TASK_ID_TIMEENTRIES: PsaProjectsProjectIdTasksTaskIdTimeentries,
        PathValues.PSA_TIMEENTRIES: PsaTimeentries,
        PathValues.PMS_TIMEFRAMES: PmsTimeframes,
        PathValues.PMS_GOALS: PmsGoals,
        PathValues.PMS_GOALS_GOAL_ID_PROGRESS: PmsGoalsGoalIdProgress,
        PathValues.PMS_BADGES: PmsBadges,
        PathValues.PMS_PRAISE: PmsPraise,
        PathValues.V1_HIRE_JOBS: V1HireJobs,
        PathValues.V1_HIRE_JOBS_JOB_ID_APPLICATIONFIELDS: V1HireJobsJobIdApplicationfields,
        PathValues.V1_HIRE_JOBS_JOB_ID_CANDIDATES: V1HireJobsJobIdCandidates,
        PathValues.V1_HIRE_JOBS_JOB_ID_CANDIDATE_CANDIDATE_ID: V1HireJobsJobIdCandidateCandidateId,
        PathValues.V1_HIRE_JOBS_JOB_ID_CANDIDATE_CANDIDATE_ID_NOTES: V1HireJobsJobIdCandidateCandidateIdNotes,
        PathValues.V1_HIRE_JOBS_JOB_ID_CANDIDATE: V1HireJobsJobIdCandidate,
        PathValues.V1_HIRE_JOBS_JOB_ID_CANDIDATE_CANDIDATE_ID_INTERVIEWS: V1HireJobsJobIdCandidateCandidateIdInterviews,
        PathValues.V1_HIRE_JOBS_JOB_ID_CANDIDATE_CANDIDATE_ID_SCORECARDS: V1HireJobsJobIdCandidateCandidateIdScorecards,
        PathValues.V1_HIRE_TALENTPOOL: V1HireTalentpool,
        PathValues.V1_HIRE_TALENTPOOL_TALENT_POOL_ID_APPLICATIONFIELDS: V1HireTalentpoolTalentPoolIdApplicationfields,
        PathValues.V1_HIRE_TALENTPOOL_TALENT_POOL_ID_CANDIDATES: V1HireTalentpoolTalentPoolIdCandidates,
        PathValues.V1_HIRE_TALENTPOOL_TALENT_POOL_ID_CANDIDATE: V1HireTalentpoolTalentPoolIdCandidate,
        PathValues.EXPENSE_CATEGORIES: ExpenseCategories,
        PathValues.EXPENSE_CLAIMS: ExpenseClaims,
        PathValues.EXPENSEPOLICIES: Expensepolicies,
        PathValues.ASSETS: Assets,
        PathValues.ASSETS_TYPES: AssetsTypes,
        PathValues.ASSETS_CATEGORIES: AssetsCategories,
        PathValues.ASSETS_CONDITIONS: AssetsConditions,
        PathValues.REQUISITION_REQUESTS: RequisitionRequests,
    }
)
