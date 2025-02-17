# coding: utf-8
"""
    Requisition

    Here's our story,  It all began with the frustration of using software that sucks. Prior to starting Keka, our core team was a 100 person business that needed an easy to use software for managing employees. We looked everywhere and all we found were software that was lousy and hard to use. We felt SME businesses in India deserved something better. Something awesome actually!  Thus emerged Keka!

    The version of the OpenAPI document: v1
    Generated by: https://konfigthis.com
"""

import typing
import inspect
from datetime import date, datetime
from keka_hr_python_sdk.client_custom import ClientCustom
from keka_hr_python_sdk.configuration import Configuration
from keka_hr_python_sdk.api_client import ApiClient
from keka_hr_python_sdk.type_util import copy_signature
from keka_hr_python_sdk.apis.tags.asset_api import AssetApi
from keka_hr_python_sdk.apis.tags.asset_category_api import AssetCategoryApi
from keka_hr_python_sdk.apis.tags.asset_condition_api import AssetConditionApi
from keka_hr_python_sdk.apis.tags.asset_type_api import AssetTypeApi
from keka_hr_python_sdk.apis.tags.attendance_api import AttendanceApi
from keka_hr_python_sdk.apis.tags.attendance_capture_scheme_api import AttendanceCaptureSchemeApi
from keka_hr_python_sdk.apis.tags.authentication_api import AuthenticationApi
from keka_hr_python_sdk.apis.tags.badge_api import BadgeApi
from keka_hr_python_sdk.apis.tags.clients_api import ClientsApi
from keka_hr_python_sdk.apis.tags.currency_api import CurrencyApi
from keka_hr_python_sdk.apis.tags.departments_api import DepartmentsApi
from keka_hr_python_sdk.apis.tags.employees_api import EmployeesApi
from keka_hr_python_sdk.apis.tags.expense_api import ExpenseApi
from keka_hr_python_sdk.apis.tags.expense_category_api import ExpenseCategoryApi
from keka_hr_python_sdk.apis.tags.expense_policy_api import ExpensePolicyApi
from keka_hr_python_sdk.apis.tags.goal_api import GoalApi
from keka_hr_python_sdk.apis.tags.groups_api import GroupsApi
from keka_hr_python_sdk.apis.tags.holiday_calendar_api import HolidayCalendarApi
from keka_hr_python_sdk.apis.tags.job_title_api import JobTitleApi
from keka_hr_python_sdk.apis.tags.jobs_api import JobsApi
from keka_hr_python_sdk.apis.tags.leave_balance_api import LeaveBalanceApi
from keka_hr_python_sdk.apis.tags.leave_requests_api import LeaveRequestsApi
from keka_hr_python_sdk.apis.tags.leave_types_api import LeaveTypesApi
from keka_hr_python_sdk.apis.tags.locations_api import LocationsApi
from keka_hr_python_sdk.apis.tags.notice_period_api import NoticePeriodApi
from keka_hr_python_sdk.apis.tags.pay_bands_api import PayBandsApi
from keka_hr_python_sdk.apis.tags.pay_cycles_api import PayCyclesApi
from keka_hr_python_sdk.apis.tags.pay_grades_api import PayGradesApi
from keka_hr_python_sdk.apis.tags.pay_groups_api import PayGroupsApi
from keka_hr_python_sdk.apis.tags.praise_api import PraiseApi
from keka_hr_python_sdk.apis.tags.project_phases_api import ProjectPhasesApi
from keka_hr_python_sdk.apis.tags.projects_api import ProjectsApi
from keka_hr_python_sdk.apis.tags.requisition_request_api import RequisitionRequestApi
from keka_hr_python_sdk.apis.tags.salary_components_api import SalaryComponentsApi
from keka_hr_python_sdk.apis.tags.talent_pool_api import TalentPoolApi
from keka_hr_python_sdk.apis.tags.tasks_api import TasksApi
from keka_hr_python_sdk.apis.tags.time_frames_api import TimeFramesApi
from keka_hr_python_sdk.apis.tags.timesheet_entries_api import TimesheetEntriesApi



class KekaHr(ClientCustom):

    def __init__(self, configuration: typing.Union[Configuration, None] = None, **kwargs):
        super().__init__(configuration, **kwargs)
        if (len(kwargs) > 0):
            configuration = Configuration(**kwargs)
        if (configuration is None):
            raise Exception("configuration is required")
        api_client = ApiClient(configuration)
        self.asset: AssetApi = AssetApi(api_client)
        self.asset_category: AssetCategoryApi = AssetCategoryApi(api_client)
        self.asset_condition: AssetConditionApi = AssetConditionApi(api_client)
        self.asset_type: AssetTypeApi = AssetTypeApi(api_client)
        self.attendance: AttendanceApi = AttendanceApi(api_client)
        self.attendance_capture_scheme: AttendanceCaptureSchemeApi = AttendanceCaptureSchemeApi(api_client)
        self.authentication: AuthenticationApi = AuthenticationApi(api_client)
        self.badge: BadgeApi = BadgeApi(api_client)
        self.clients: ClientsApi = ClientsApi(api_client)
        self.currency: CurrencyApi = CurrencyApi(api_client)
        self.departments: DepartmentsApi = DepartmentsApi(api_client)
        self.employees: EmployeesApi = EmployeesApi(api_client)
        self.expense: ExpenseApi = ExpenseApi(api_client)
        self.expense_category: ExpenseCategoryApi = ExpenseCategoryApi(api_client)
        self.expense_policy: ExpensePolicyApi = ExpensePolicyApi(api_client)
        self.goal: GoalApi = GoalApi(api_client)
        self.groups: GroupsApi = GroupsApi(api_client)
        self.holiday_calendar: HolidayCalendarApi = HolidayCalendarApi(api_client)
        self.job_title: JobTitleApi = JobTitleApi(api_client)
        self.jobs: JobsApi = JobsApi(api_client)
        self.leave_balance: LeaveBalanceApi = LeaveBalanceApi(api_client)
        self.leave_requests: LeaveRequestsApi = LeaveRequestsApi(api_client)
        self.leave_types: LeaveTypesApi = LeaveTypesApi(api_client)
        self.locations: LocationsApi = LocationsApi(api_client)
        self.notice_period: NoticePeriodApi = NoticePeriodApi(api_client)
        self.pay_bands: PayBandsApi = PayBandsApi(api_client)
        self.pay_cycles: PayCyclesApi = PayCyclesApi(api_client)
        self.pay_grades: PayGradesApi = PayGradesApi(api_client)
        self.pay_groups: PayGroupsApi = PayGroupsApi(api_client)
        self.praise: PraiseApi = PraiseApi(api_client)
        self.project_phases: ProjectPhasesApi = ProjectPhasesApi(api_client)
        self.projects: ProjectsApi = ProjectsApi(api_client)
        self.requisition_request: RequisitionRequestApi = RequisitionRequestApi(api_client)
        self.salary_components: SalaryComponentsApi = SalaryComponentsApi(api_client)
        self.talent_pool: TalentPoolApi = TalentPoolApi(api_client)
        self.tasks: TasksApi = TasksApi(api_client)
        self.time_frames: TimeFramesApi = TimeFramesApi(api_client)
        self.timesheet_entries: TimesheetEntriesApi = TimesheetEntriesApi(api_client)
