import typing_extensions

from keka_hr_python_sdk.apis.tags import TagValues
from keka_hr_python_sdk.apis.tags.jobs_api import JobsApi
from keka_hr_python_sdk.apis.tags.employees_api import EmployeesApi
from keka_hr_python_sdk.apis.tags.projects_api import ProjectsApi
from keka_hr_python_sdk.apis.tags.pay_cycles_api import PayCyclesApi
from keka_hr_python_sdk.apis.tags.clients_api import ClientsApi
from keka_hr_python_sdk.apis.tags.tasks_api import TasksApi
from keka_hr_python_sdk.apis.tags.talent_pool_api import TalentPoolApi
from keka_hr_python_sdk.apis.tags.groups_api import GroupsApi
from keka_hr_python_sdk.apis.tags.leave_requests_api import LeaveRequestsApi
from keka_hr_python_sdk.apis.tags.project_phases_api import ProjectPhasesApi
from keka_hr_python_sdk.apis.tags.goal_api import GoalApi
from keka_hr_python_sdk.apis.tags.praise_api import PraiseApi
from keka_hr_python_sdk.apis.tags.departments_api import DepartmentsApi
from keka_hr_python_sdk.apis.tags.locations_api import LocationsApi
from keka_hr_python_sdk.apis.tags.job_title_api import JobTitleApi
from keka_hr_python_sdk.apis.tags.currency_api import CurrencyApi
from keka_hr_python_sdk.apis.tags.notice_period_api import NoticePeriodApi
from keka_hr_python_sdk.apis.tags.leave_types_api import LeaveTypesApi
from keka_hr_python_sdk.apis.tags.leave_balance_api import LeaveBalanceApi
from keka_hr_python_sdk.apis.tags.attendance_api import AttendanceApi
from keka_hr_python_sdk.apis.tags.attendance_capture_scheme_api import AttendanceCaptureSchemeApi
from keka_hr_python_sdk.apis.tags.holiday_calendar_api import HolidayCalendarApi
from keka_hr_python_sdk.apis.tags.salary_components_api import SalaryComponentsApi
from keka_hr_python_sdk.apis.tags.pay_groups_api import PayGroupsApi
from keka_hr_python_sdk.apis.tags.pay_grades_api import PayGradesApi
from keka_hr_python_sdk.apis.tags.pay_bands_api import PayBandsApi
from keka_hr_python_sdk.apis.tags.timesheet_entries_api import TimesheetEntriesApi
from keka_hr_python_sdk.apis.tags.time_frames_api import TimeFramesApi
from keka_hr_python_sdk.apis.tags.badge_api import BadgeApi
from keka_hr_python_sdk.apis.tags.expense_category_api import ExpenseCategoryApi
from keka_hr_python_sdk.apis.tags.expense_api import ExpenseApi
from keka_hr_python_sdk.apis.tags.expense_policy_api import ExpensePolicyApi
from keka_hr_python_sdk.apis.tags.asset_api import AssetApi
from keka_hr_python_sdk.apis.tags.asset_type_api import AssetTypeApi
from keka_hr_python_sdk.apis.tags.asset_category_api import AssetCategoryApi
from keka_hr_python_sdk.apis.tags.asset_condition_api import AssetConditionApi
from keka_hr_python_sdk.apis.tags.requisition_request_api import RequisitionRequestApi
from keka_hr_python_sdk.apis.tags.authentication_api import AuthenticationApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.JOBS: JobsApi,
        TagValues.EMPLOYEES: EmployeesApi,
        TagValues.PROJECTS: ProjectsApi,
        TagValues.PAY_CYCLES: PayCyclesApi,
        TagValues.CLIENTS: ClientsApi,
        TagValues.TASKS: TasksApi,
        TagValues.TALENT_POOL: TalentPoolApi,
        TagValues.GROUPS: GroupsApi,
        TagValues.LEAVE_REQUESTS: LeaveRequestsApi,
        TagValues.PROJECT_PHASES: ProjectPhasesApi,
        TagValues.GOAL: GoalApi,
        TagValues.PRAISE: PraiseApi,
        TagValues.DEPARTMENTS: DepartmentsApi,
        TagValues.LOCATIONS: LocationsApi,
        TagValues.JOB_TITLE: JobTitleApi,
        TagValues.CURRENCY: CurrencyApi,
        TagValues.NOTICE_PERIOD: NoticePeriodApi,
        TagValues.LEAVE_TYPES: LeaveTypesApi,
        TagValues.LEAVE_BALANCE: LeaveBalanceApi,
        TagValues.ATTENDANCE: AttendanceApi,
        TagValues.ATTENDANCE_CAPTURE_SCHEME: AttendanceCaptureSchemeApi,
        TagValues.HOLIDAY_CALENDAR: HolidayCalendarApi,
        TagValues.SALARY_COMPONENTS: SalaryComponentsApi,
        TagValues.PAY_GROUPS: PayGroupsApi,
        TagValues.PAY_GRADES: PayGradesApi,
        TagValues.PAY_BANDS: PayBandsApi,
        TagValues.TIMESHEET_ENTRIES: TimesheetEntriesApi,
        TagValues.TIME_FRAMES: TimeFramesApi,
        TagValues.BADGE: BadgeApi,
        TagValues.EXPENSE_CATEGORY: ExpenseCategoryApi,
        TagValues.EXPENSE: ExpenseApi,
        TagValues.EXPENSE_POLICY: ExpensePolicyApi,
        TagValues.ASSET: AssetApi,
        TagValues.ASSET_TYPE: AssetTypeApi,
        TagValues.ASSET_CATEGORY: AssetCategoryApi,
        TagValues.ASSET_CONDITION: AssetConditionApi,
        TagValues.REQUISITION_REQUEST: RequisitionRequestApi,
        TagValues.AUTHENTICATION: AuthenticationApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.JOBS: JobsApi,
        TagValues.EMPLOYEES: EmployeesApi,
        TagValues.PROJECTS: ProjectsApi,
        TagValues.PAY_CYCLES: PayCyclesApi,
        TagValues.CLIENTS: ClientsApi,
        TagValues.TASKS: TasksApi,
        TagValues.TALENT_POOL: TalentPoolApi,
        TagValues.GROUPS: GroupsApi,
        TagValues.LEAVE_REQUESTS: LeaveRequestsApi,
        TagValues.PROJECT_PHASES: ProjectPhasesApi,
        TagValues.GOAL: GoalApi,
        TagValues.PRAISE: PraiseApi,
        TagValues.DEPARTMENTS: DepartmentsApi,
        TagValues.LOCATIONS: LocationsApi,
        TagValues.JOB_TITLE: JobTitleApi,
        TagValues.CURRENCY: CurrencyApi,
        TagValues.NOTICE_PERIOD: NoticePeriodApi,
        TagValues.LEAVE_TYPES: LeaveTypesApi,
        TagValues.LEAVE_BALANCE: LeaveBalanceApi,
        TagValues.ATTENDANCE: AttendanceApi,
        TagValues.ATTENDANCE_CAPTURE_SCHEME: AttendanceCaptureSchemeApi,
        TagValues.HOLIDAY_CALENDAR: HolidayCalendarApi,
        TagValues.SALARY_COMPONENTS: SalaryComponentsApi,
        TagValues.PAY_GROUPS: PayGroupsApi,
        TagValues.PAY_GRADES: PayGradesApi,
        TagValues.PAY_BANDS: PayBandsApi,
        TagValues.TIMESHEET_ENTRIES: TimesheetEntriesApi,
        TagValues.TIME_FRAMES: TimeFramesApi,
        TagValues.BADGE: BadgeApi,
        TagValues.EXPENSE_CATEGORY: ExpenseCategoryApi,
        TagValues.EXPENSE: ExpenseApi,
        TagValues.EXPENSE_POLICY: ExpensePolicyApi,
        TagValues.ASSET: AssetApi,
        TagValues.ASSET_TYPE: AssetTypeApi,
        TagValues.ASSET_CATEGORY: AssetCategoryApi,
        TagValues.ASSET_CONDITION: AssetConditionApi,
        TagValues.REQUISITION_REQUEST: RequisitionRequestApi,
        TagValues.AUTHENTICATION: AuthenticationApi,
    }
)
