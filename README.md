<div align="left">

[![Visit Keka hr](./header.png)](https://keka.com)

# Keka hr<a id="keka-hr"></a>

Here's our story,

It all began with the frustration of using software that sucks. Prior to starting Keka, our core team was a 100 person business that needed an easy to use software for managing employees. We looked everywhere and all we found were software that was lousy and hard to use. We felt SME businesses in India deserved something better. Something awesome actually!

Thus emerged Keka!


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`kekahr.asset.get_all`](#kekahrassetget_all)
  * [`kekahr.asset_category.get_all`](#kekahrasset_categoryget_all)
  * [`kekahr.asset_condition.get_all`](#kekahrasset_conditionget_all)
  * [`kekahr.asset_type.get_all`](#kekahrasset_typeget_all)
  * [`kekahr.attendance.get_records_in_range`](#kekahrattendanceget_records_in_range)
  * [`kekahr.attendance_capture_scheme.get_all`](#kekahrattendance_capture_schemeget_all)
  * [`kekahr.authentication.get_access_token`](#kekahrauthenticationget_access_token)
  * [`kekahr.badge.get_list`](#kekahrbadgeget_list)
  * [`kekahr.clients.create_client_identifier`](#kekahrclientscreate_client_identifier)
  * [`kekahr.clients.get_all`](#kekahrclientsget_all)
  * [`kekahr.clients.get_by_id`](#kekahrclientsget_by_id)
  * [`kekahr.clients.update_details`](#kekahrclientsupdate_details)
  * [`kekahr.currency.get_all`](#kekahrcurrencyget_all)
  * [`kekahr.departments.get_all`](#kekahrdepartmentsget_all)
  * [`kekahr.employees.create_employee`](#kekahremployeescreate_employee)
  * [`kekahr.employees.get_all`](#kekahremployeesget_all)
  * [`kekahr.employees.get_all_update_fields`](#kekahremployeesget_all_update_fields)
  * [`kekahr.employees.get_by_id`](#kekahremployeesget_by_id)
  * [`kekahr.employees.update_job_details`](#kekahremployeesupdate_job_details)
  * [`kekahr.employees.update_personal_details`](#kekahremployeesupdate_personal_details)
  * [`kekahr.expense.get_all_claims`](#kekahrexpenseget_all_claims)
  * [`kekahr.expense_category.get_all_categories`](#kekahrexpense_categoryget_all_categories)
  * [`kekahr.expense_policy.list_all_expense_policies`](#kekahrexpense_policylist_all_expense_policies)
  * [`kekahr.goal.list_with_hierarchy`](#kekahrgoallist_with_hierarchy)
  * [`kekahr.goal.update_progress`](#kekahrgoalupdate_progress)
  * [`kekahr.groups.get_all`](#kekahrgroupsget_all)
  * [`kekahr.groups.get_all_group_types`](#kekahrgroupsget_all_group_types)
  * [`kekahr.holiday_calendar.get_all_holidays_calendar`](#kekahrholiday_calendarget_all_holidays_calendar)
  * [`kekahr.job_title.get_all`](#kekahrjob_titleget_all)
  * [`kekahr.jobs.add_candidate_note`](#kekahrjobsadd_candidate_note)
  * [`kekahr.jobs.get_all_published_jobs`](#kekahrjobsget_all_published_jobs)
  * [`kekahr.jobs.get_application_fields`](#kekahrjobsget_application_fields)
  * [`kekahr.jobs.get_candidate_interviews`](#kekahrjobsget_candidate_interviews)
  * [`kekahr.jobs.get_candidate_scorecards`](#kekahrjobsget_candidate_scorecards)
  * [`kekahr.jobs.get_candidates`](#kekahrjobsget_candidates)
  * [`kekahr.jobs.post_candidate`](#kekahrjobspost_candidate)
  * [`kekahr.jobs.update_candidate`](#kekahrjobsupdate_candidate)
  * [`kekahr.leave_balance.get_all_balances`](#kekahrleave_balanceget_all_balances)
  * [`kekahr.leave_requests.create_request_identifier`](#kekahrleave_requestscreate_request_identifier)
  * [`kekahr.leave_requests.get_all_between_dates`](#kekahrleave_requestsget_all_between_dates)
  * [`kekahr.leave_types.list_all`](#kekahrleave_typeslist_all)
  * [`kekahr.locations.get_all`](#kekahrlocationsget_all)
  * [`kekahr.notice_period.get_all`](#kekahrnotice_periodget_all)
  * [`kekahr.pay_bands.get_all`](#kekahrpay_bandsget_all)
  * [`kekahr.pay_cycles.get_all`](#kekahrpay_cyclesget_all)
  * [`kekahr.pay_cycles.get_batch_payments`](#kekahrpay_cyclesget_batch_payments)
  * [`kekahr.pay_cycles.get_pay_batches`](#kekahrpay_cyclesget_pay_batches)
  * [`kekahr.pay_cycles.get_pay_register`](#kekahrpay_cyclesget_pay_register)
  * [`kekahr.pay_cycles.update_payments_status`](#kekahrpay_cyclesupdate_payments_status)
  * [`kekahr.pay_grades.get_all`](#kekahrpay_gradesget_all)
  * [`kekahr.pay_groups.get_all`](#kekahrpay_groupsget_all)
  * [`kekahr.praise.create_praise_identifier`](#kekahrpraisecreate_praise_identifier)
  * [`kekahr.praise.list_employees_praises`](#kekahrpraiselist_employees_praises)
  * [`kekahr.project_phases.create_phase_identifier`](#kekahrproject_phasescreate_phase_identifier)
  * [`kekahr.project_phases.get_all`](#kekahrproject_phasesget_all)
  * [`kekahr.projects.create_project_identifier`](#kekahrprojectscreate_project_identifier)
  * [`kekahr.projects.get_all`](#kekahrprojectsget_all)
  * [`kekahr.projects.get_allocations`](#kekahrprojectsget_allocations)
  * [`kekahr.projects.get_by_id`](#kekahrprojectsget_by_id)
  * [`kekahr.projects.get_timesheet_entries_between_dates`](#kekahrprojectsget_timesheet_entries_between_dates)
  * [`kekahr.projects.update_details`](#kekahrprojectsupdate_details)
  * [`kekahr.requisition_request.get_all`](#kekahrrequisition_requestget_all)
  * [`kekahr.salary_components.get_all_components`](#kekahrsalary_componentsget_all_components)
  * [`kekahr.talent_pool.add_candidate`](#kekahrtalent_pooladd_candidate)
  * [`kekahr.talent_pool.get_all`](#kekahrtalent_poolget_all)
  * [`kekahr.talent_pool.get_application_fields`](#kekahrtalent_poolget_application_fields)
  * [`kekahr.talent_pool.get_candidates`](#kekahrtalent_poolget_candidates)
  * [`kekahr.tasks.create_task_identifier`](#kekahrtaskscreate_task_identifier)
  * [`kekahr.tasks.get_all`](#kekahrtasksget_all)
  * [`kekahr.tasks.list_time_entries_between_dates`](#kekahrtaskslist_time_entries_between_dates)
  * [`kekahr.tasks.update_task`](#kekahrtasksupdate_task)
  * [`kekahr.time_frames.get_all`](#kekahrtime_framesget_all)
  * [`kekahr.timesheet_entries.get_between_dates`](#kekahrtimesheet_entriesget_between_dates)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Keka%20HR&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from keka_hr_python_sdk import KekaHr, ApiException

kekahr = KekaHr(

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',,

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',
)

try:
    # Get all Assets
    get_all_response = kekahr.asset.get_all(
        asset_ids="string_example",
        employee_ids="string_example",
        asset_status="string_example",
        last_modified="1970-01-01T00:00:00.00Z",
        page_number=1,
        page_size=1,
    )
    print(get_all_response)
except ApiException as e:
    print("Exception when calling AssetApi.get_all: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python

import asyncio
from pprint import pprint
from keka_hr_python_sdk import KekaHr, ApiException

kekahr = KekaHr(

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',,

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',
)

async def main():
    try:
        # Get all Assets
        get_all_response = await kekahr.asset.aget_all(
            asset_ids="string_example",
            employee_ids="string_example",
            asset_status="string_example",
            last_modified="1970-01-01T00:00:00.00Z",
            page_number=1,
            page_size=1,
        )
        print(get_all_response)
    except ApiException as e:
        print("Exception when calling AssetApi.get_all: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)

asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from keka_hr_python_sdk import KekaHr, ApiException

kekahr = KekaHr(

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',,

    client_id = 'YOUR_CLIENT_ID',
    client_secret = 'YOUR_CLIENT_SECRET',
)

try:
    # Get all Assets
    get_all_response = kekahr.asset.raw.get_all(
        asset_ids="string_example",
        employee_ids="string_example",
        asset_status="string_example",
        last_modified="1970-01-01T00:00:00.00Z",
        page_number=1,
        page_size=1,
    )
    pprint(get_all_response.body)
    pprint(get_all_response.body["succeeded"])
    pprint(get_all_response.body["message"])
    pprint(get_all_response.body["errors"])
    pprint(get_all_response.body["data"])
    pprint(get_all_response.body["page_number"])
    pprint(get_all_response.body["page_size"])
    pprint(get_all_response.body["first_page"])
    pprint(get_all_response.body["last_page"])
    pprint(get_all_response.body["total_pages"])
    pprint(get_all_response.body["total_records"])
    pprint(get_all_response.body["next_page"])
    pprint(get_all_response.body["previous_page"])
    pprint(get_all_response.headers)
    pprint(get_all_response.status)
    pprint(get_all_response.round_trip_time)
except ApiException as e:
    print("Exception when calling AssetApi.get_all: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `kekahr.asset.get_all`<a id="kekahrassetget_all"></a>

Get all Assets

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_response = kekahr.asset.get_all(
    asset_ids="string_example",
    employee_ids="string_example",
    asset_status="string_example",
    last_modified="1970-01-01T00:00:00.00Z",
    page_number=1,
    page_size=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### asset_ids: `str`<a id="asset_ids-str"></a>

The asset ids.

##### employee_ids: `str`<a id="employee_ids-str"></a>

The employee ids.

##### asset_status: `str`<a id="asset_status-str"></a>

The asset status.

##### last_modified: `datetime`<a id="last_modified-datetime"></a>

The last modified.

##### page_number: `int`<a id="page_number-int"></a>

##### page_size: `int`<a id="page_size-int"></a>

Represents how many results you'd like to retrieve per request (page). Default is 100. Max is 200

#### 🔄 Return<a id="🔄-return"></a>

[`AssetPagedResponse`](./keka_hr_python_sdk/pydantic/asset_paged_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/assets` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kekahr.asset_category.get_all`<a id="kekahrasset_categoryget_all"></a>

Get all Asset Categories

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_response = kekahr.asset_category.get_all(
    asset_category_ids="string_example",
    last_modified="1970-01-01T00:00:00.00Z",
    page_number=1,
    page_size=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### asset_category_ids: `str`<a id="asset_category_ids-str"></a>

The asset category ids.

##### last_modified: `datetime`<a id="last_modified-datetime"></a>

The last modified.

##### page_number: `int`<a id="page_number-int"></a>

##### page_size: `int`<a id="page_size-int"></a>

Represents how many results you'd like to retrieve per request (page). Default is 100. Max is 200

#### 🔄 Return<a id="🔄-return"></a>

[`ApiLookupPagedResponse`](./keka_hr_python_sdk/pydantic/api_lookup_paged_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/assets/categories` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kekahr.asset_condition.get_all`<a id="kekahrasset_conditionget_all"></a>

Get all Asset Conditions

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_response = kekahr.asset_condition.get_all(
    asset_condition_ids="string_example",
    last_modified="1970-01-01T00:00:00.00Z",
    page_number=1,
    page_size=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### asset_condition_ids: `str`<a id="asset_condition_ids-str"></a>

The asset condition ids.

##### last_modified: `datetime`<a id="last_modified-datetime"></a>

The last modified.

##### page_number: `int`<a id="page_number-int"></a>

##### page_size: `int`<a id="page_size-int"></a>

Represents how many results you'd like to retrieve per request (page). Default is 100. Max is 200

#### 🔄 Return<a id="🔄-return"></a>

[`ApiLookupPagedResponse`](./keka_hr_python_sdk/pydantic/api_lookup_paged_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/assets/conditions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kekahr.asset_type.get_all`<a id="kekahrasset_typeget_all"></a>

Get all Asset Types

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_response = kekahr.asset_type.get_all(
    asset_type_ids="string_example",
    last_modified="1970-01-01T00:00:00.00Z",
    page_number=1,
    page_size=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### asset_type_ids: `str`<a id="asset_type_ids-str"></a>

The asset type ids.

##### last_modified: `datetime`<a id="last_modified-datetime"></a>

The last modified.

##### page_number: `int`<a id="page_number-int"></a>

##### page_size: `int`<a id="page_size-int"></a>

Represents how many results you'd like to retrieve per request (page). Default is 100. Max is 200

#### 🔄 Return<a id="🔄-return"></a>

[`ApiLookupPagedResponse`](./keka_hr_python_sdk/pydantic/api_lookup_paged_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/assets/types` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kekahr.attendance.get_records_in_range`<a id="kekahrattendanceget_records_in_range"></a>

Gets all Attendance records between date range `from` and `to`.If both `from` and `to` are not specified, last 30 days records are returned.From `date` should be before `to` date.The difference between `from` and `to` date cannot be more than **90** days.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_records_in_range_response = kekahr.attendance.get_records_in_range(
    employee_ids="string_example",
    _from="1970-01-01T00:00:00.00Z",
    to="1970-01-01T00:00:00.00Z",
    page_number=1,
    page_size=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_ids: `str`<a id="employee_ids-str"></a>

Comma separated list of one or more Employee ids you'd like to filter on.

##### _from: `datetime`<a id="_from-datetime"></a>

Date from records to retrieve. If not specified defaults to `to - 30` days.

##### to: `datetime`<a id="to-datetime"></a>

Date to records can be retrieved. If not specified defaults to `today`.

##### page_number: `int`<a id="page_number-int"></a>

##### page_size: `int`<a id="page_size-int"></a>

Represents how many results you'd like to retrieve per request (page). Default is 100. Max is 200

#### 🔄 Return<a id="🔄-return"></a>

[`AttendanceSummaryPagedResponse`](./keka_hr_python_sdk/pydantic/attendance_summary_paged_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/time/attendance` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kekahr.attendance_capture_scheme.get_all`<a id="kekahrattendance_capture_schemeget_all"></a>

Get all captureschemes

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_response = kekahr.attendance_capture_scheme.get_all(
    capturescheme_ids="string_example",
    page_number=1,
    page_size=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### capturescheme_ids: `str`<a id="capturescheme_ids-str"></a>

The capturescheme ids.

##### page_number: `int`<a id="page_number-int"></a>

##### page_size: `int`<a id="page_size-int"></a>

Represents how many results you'd like to retrieve per request (page). Default is 100. Max is 200

#### 🔄 Return<a id="🔄-return"></a>

[`ApiLookupPagedResponse`](./keka_hr_python_sdk/pydantic/api_lookup_paged_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/time/capturescheme` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kekahr.authentication.get_access_token`<a id="kekahrauthenticationget_access_token"></a>

Use this API to fetch access token by passing authentication parameters ( grant_type, scope, client_id, client_secret, api_key) as form-url encoded in the body.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_access_token_response = kekahr.authentication.get_access_token(
    grant_type="kekaapi",
    scope="kekaapi",
    client_id="string_example",
    client_secret="string_example",
    api_key="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### grant_type: `str`<a id="grant_type-str"></a>

##### scope: `str`<a id="scope-str"></a>

##### client_id: `str`<a id="client_id-str"></a>

##### client_secret: `str`<a id="client_secret-str"></a>

##### api_key: `str`<a id="api_key-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AuthenticationGetAccessTokenRequest`](./keka_hr_python_sdk/type/authentication_get_access_token_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AuthenticationGetAccessTokenResponse`](./keka_hr_python_sdk/pydantic/authentication_get_access_token_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/connect/token` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kekahr.badge.get_list`<a id="kekahrbadgeget_list"></a>

Gets all badge.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_list_response = kekahr.badge.get_list(
    badge_ids="string_example",
    page_number=1,
    page_size=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### badge_ids: `str`<a id="badge_ids-str"></a>

Comma separated list of one or more Badge ids you'd like to filter on.

##### page_number: `int`<a id="page_number-int"></a>

##### page_size: `int`<a id="page_size-int"></a>

Represents how many results you'd like to retrieve per request (page). Default is 100. Max is 200

#### 🔄 Return<a id="🔄-return"></a>

[`APIBadgePagedResponse`](./keka_hr_python_sdk/pydantic/api_badge_paged_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/pms/badges` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kekahr.clients.create_client_identifier`<a id="kekahrclientscreate_client_identifier"></a>

Create a Client and returns created client identifier.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_client_identifier_response = kekahr.clients.create_client_identifier(
    name="string_example",
    code="string_example",
    description="string_example",
    billing_info={
        "billing_currency_id": "billing_currency_id_example",
    },
    phone="string_example",
    website="string_example",
    email="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

##### code: `str`<a id="code-str"></a>

##### description: `Optional[str]`<a id="description-optionalstr"></a>

##### billing_info: [`BillingInfo`](./keka_hr_python_sdk/type/billing_info.py)<a id="billing_info-billinginfokeka_hr_python_sdktypebilling_infopy"></a>


##### phone: `Optional[str]`<a id="phone-optionalstr"></a>

##### website: `Optional[str]`<a id="website-optionalstr"></a>

##### email: `Optional[str]`<a id="email-optionalstr"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Client`](./keka_hr_python_sdk/type/client.py)
The client.

#### 🔄 Return<a id="🔄-return"></a>

[`StringResponse`](./keka_hr_python_sdk/pydantic/string_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/psa/clients` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kekahr.clients.get_all`<a id="kekahrclientsget_all"></a>

Get all clients

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_response = kekahr.clients.get_all(
    client_ids="string_example",
    last_modified="1970-01-01T00:00:00.00Z",
    page_number=1,
    page_size=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### client_ids: `str`<a id="client_ids-str"></a>

Comma separated list of one or more employee ids you'd like to filter on.

##### last_modified: `datetime`<a id="last_modified-datetime"></a>

Date/time when this time off request was last modified, in ISO 8601 format (YYYY-MM-DDThh:mm:ss±hh:mm).

##### page_number: `int`<a id="page_number-int"></a>

##### page_size: `int`<a id="page_size-int"></a>

Represents how many results you'd like to retrieve per request (page). Default is 100. Max is 200

#### 🔄 Return<a id="🔄-return"></a>

[`APIClientPagedResponse`](./keka_hr_python_sdk/pydantic/api_client_paged_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/psa/clients` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kekahr.clients.get_by_id`<a id="kekahrclientsget_by_id"></a>

Gets the specified client based on identifier.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = kekahr.clients.get_by_id(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The identifier.

#### 🔄 Return<a id="🔄-return"></a>

[`APIClientResponse`](./keka_hr_python_sdk/pydantic/api_client_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/psa/clients/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kekahr.clients.update_details`<a id="kekahrclientsupdate_details"></a>

Update Client Details.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_details_response = kekahr.clients.update_details(
    id="id_example",
    description="string_example",
    name="string_example",
    code="string_example",
    billing_address={
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The identifier.

##### description: `Optional[str]`<a id="description-optionalstr"></a>

##### name: `Optional[str]`<a id="name-optionalstr"></a>

##### code: `Optional[str]`<a id="code-optionalstr"></a>

##### billing_address: [`Address`](./keka_hr_python_sdk/type/address.py)<a id="billing_address-addresskeka_hr_python_sdktypeaddresspy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateClient`](./keka_hr_python_sdk/type/update_client.py)
The update client.

#### 🔄 Return<a id="🔄-return"></a>

[`BooleanResponse`](./keka_hr_python_sdk/pydantic/boolean_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/psa/clients/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kekahr.currency.get_all`<a id="kekahrcurrencyget_all"></a>

Get all currencies

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_response = kekahr.currency.get_all(
    page_number=1,
    page_size=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page_number: `int`<a id="page_number-int"></a>

##### page_size: `int`<a id="page_size-int"></a>

Represents how many results you'd like to retrieve per request (page). Default is 100. Max is 200

#### 🔄 Return<a id="🔄-return"></a>

[`CurrencyPagedResponse`](./keka_hr_python_sdk/pydantic/currency_paged_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/hris/currencies` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kekahr.departments.get_all`<a id="kekahrdepartmentsget_all"></a>

Get all departments

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_response = kekahr.departments.get_all(
    department_ids="string_example",
    last_modified="1970-01-01T00:00:00.00Z",
    page_number=1,
    page_size=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### department_ids: `str`<a id="department_ids-str"></a>

##### last_modified: `datetime`<a id="last_modified-datetime"></a>

The Last Modified Date.

##### page_number: `int`<a id="page_number-int"></a>

##### page_size: `int`<a id="page_size-int"></a>

Represents how many results you'd like to retrieve per request (page). Default is 100. Max is 200

#### 🔄 Return<a id="🔄-return"></a>

[`APIDepartmentViewPagedResponse`](./keka_hr_python_sdk/pydantic/api_department_view_paged_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/hris/departments` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kekahr.employees.create_employee`<a id="kekahremployeescreate_employee"></a>

Create an Employee and returns created employee identifier.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_employee_response = kekahr.employees.create_employee(
    display_name="string_example",
    first_name="string_example",
    last_name="string_example",
    email="string_example",
    gender=0,
    date_of_birth="1970-01-01T00:00:00.00Z",
    date_joined="1970-01-01T00:00:00.00Z",
    department="string_example",
    business_unit="string_example",
    job_title="string_example",
    location="string_example",
    employee_number="string_example",
    middle_name="string_example",
    mobile_number="string_example",
    secondary_job_title="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### display_name: `str`<a id="display_name-str"></a>

##### first_name: `str`<a id="first_name-str"></a>

##### last_name: `str`<a id="last_name-str"></a>

##### email: `str`<a id="email-str"></a>

##### gender: [`Gender`](./keka_hr_python_sdk/type/gender.py)<a id="gender-genderkeka_hr_python_sdktypegenderpy"></a>

##### date_of_birth: `datetime`<a id="date_of_birth-datetime"></a>

##### date_joined: `datetime`<a id="date_joined-datetime"></a>

##### department: `str`<a id="department-str"></a>

##### business_unit: `str`<a id="business_unit-str"></a>

##### job_title: `str`<a id="job_title-str"></a>

##### location: `str`<a id="location-str"></a>

##### employee_number: `Optional[str]`<a id="employee_number-optionalstr"></a>

##### middle_name: `Optional[str]`<a id="middle_name-optionalstr"></a>

##### mobile_number: `Optional[str]`<a id="mobile_number-optionalstr"></a>

##### secondary_job_title: `Optional[str]`<a id="secondary_job_title-optionalstr"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Employee`](./keka_hr_python_sdk/type/employee.py)
The employee.

#### 🔄 Return<a id="🔄-return"></a>

[`StringResponse`](./keka_hr_python_sdk/pydantic/string_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/hris/employees` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kekahr.employees.get_all`<a id="kekahremployeesget_all"></a>

Gets all employees / the specified employees based on employee search parameters.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_response = kekahr.employees.get_all(
    employee_ids="string_example",
    employee_numbers="string_example",
    employment_status="string_example",
    in_probation=False,
    in_notice_period=False,
    last_modified="1970-01-01T00:00:00.00Z",
    page_number=1,
    page_size=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_ids: `str`<a id="employee_ids-str"></a>

Comma separated list of one or more Employee ids you'd like to filter on.

##### employee_numbers: `str`<a id="employee_numbers-str"></a>

Comma separated list of one or more Employee numbers you'd like to filter on.

##### employment_status: `str`<a id="employment_status-str"></a>

Comma separated list of one or more Employment Status you'd like to filter on, allowed values are Working, Relieved.

##### in_probation: `bool`<a id="in_probation-bool"></a>

Fetches employees who are in probation. The allowed value is true or false.

##### in_notice_period: `bool`<a id="in_notice_period-bool"></a>

Fetches employees who are in notice period. The allowed value is true or false.

##### last_modified: `datetime`<a id="last_modified-datetime"></a>

Date/time when this time off request was last modified, in ISO 8601 format (YYYY-MM-DDThh:mm:ss±hh:mm).

##### page_number: `int`<a id="page_number-int"></a>

##### page_size: `int`<a id="page_size-int"></a>

Represents how many results you'd like to retrieve per request (page). Default is 100. Max is 200

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeProfilePagedResponse`](./keka_hr_python_sdk/pydantic/employee_profile_paged_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/hris/employees` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kekahr.employees.get_all_update_fields`<a id="kekahremployeesget_all_update_fields"></a>

Get all update fields

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_update_fields_response = kekahr.employees.get_all_update_fields(
    page_number=1,
    page_size=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page_number: `int`<a id="page_number-int"></a>

##### page_size: `int`<a id="page_size-int"></a>

Represents how many results you'd like to retrieve per request (page). Default is 100. Max is 200

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeFieldResponse`](./keka_hr_python_sdk/pydantic/employee_field_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/hris/employees/updatefields` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kekahr.employees.get_by_id`<a id="kekahremployeesget_by_id"></a>

Get an employee with specified identifier.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = kekahr.employees.get_by_id(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The identifier.

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeProfileResponse`](./keka_hr_python_sdk/pydantic/employee_profile_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/hris/employees/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kekahr.employees.update_job_details`<a id="kekahremployeesupdate_job_details"></a>

Update employee job details.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_job_details_response = kekahr.employees.update_job_details(
    id="id_example",
    employee_number="string_example",
    location="string_example",
    business_unit="string_example",
    department="string_example",
    job_title="string_example",
    reporting_manager="string_example",
    attendance_number="string_example",
    time_type=0,
    attendance_capture_scheme="string_example",
    expense_policy="string_example",
    notice_period="string_example",
    holiday_list="string_example",
    cost_center="string_example",
    pay_band="string_example",
    pay_grade="string_example",
    custom_fields={
        "key": None,
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The identifier.

##### employee_number: `Optional[str]`<a id="employee_number-optionalstr"></a>

##### location: `Optional[str]`<a id="location-optionalstr"></a>

##### business_unit: `Optional[str]`<a id="business_unit-optionalstr"></a>

##### department: `Optional[str]`<a id="department-optionalstr"></a>

##### job_title: `Optional[str]`<a id="job_title-optionalstr"></a>

##### reporting_manager: `Optional[str]`<a id="reporting_manager-optionalstr"></a>

##### attendance_number: `Optional[str]`<a id="attendance_number-optionalstr"></a>

##### time_type: [`TimeType`](./keka_hr_python_sdk/type/time_type.py)<a id="time_type-timetypekeka_hr_python_sdktypetime_typepy"></a>

##### attendance_capture_scheme: `Optional[str]`<a id="attendance_capture_scheme-optionalstr"></a>

##### expense_policy: `Optional[str]`<a id="expense_policy-optionalstr"></a>

##### notice_period: `Optional[str]`<a id="notice_period-optionalstr"></a>

##### holiday_list: `Optional[str]`<a id="holiday_list-optionalstr"></a>

##### cost_center: `Optional[str]`<a id="cost_center-optionalstr"></a>

##### pay_band: `Optional[str]`<a id="pay_band-optionalstr"></a>

##### pay_grade: `Optional[str]`<a id="pay_grade-optionalstr"></a>

##### custom_fields: [`JobDetailsUpdateRequestCustomFields`](./keka_hr_python_sdk/type/job_details_update_request_custom_fields.py)<a id="custom_fields-jobdetailsupdaterequestcustomfieldskeka_hr_python_sdktypejob_details_update_request_custom_fieldspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`JobDetailsUpdateRequest`](./keka_hr_python_sdk/type/job_details_update_request.py)
The job details.

#### 🔄 Return<a id="🔄-return"></a>

[`BooleanResponse`](./keka_hr_python_sdk/pydantic/boolean_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/hris/employees/{id}/jobdetails` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kekahr.employees.update_personal_details`<a id="kekahremployeesupdate_personal_details"></a>

Update Employee personal details.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_personal_details_response = kekahr.employees.update_personal_details(
    id="id_example",
    display_name="string_example",
    first_name="string_example",
    middle_name="string_example",
    last_name="string_example",
    gender=0,
    date_of_birth="1970-01-01T00:00:00.00Z",
    work_phone="string_example",
    home_phone="string_example",
    personal_email="string_example",
    skype_id="string_example",
    marital_status=0,
    marriage_date="1970-01-01T00:00:00.00Z",
    relations=[
        {
            "relation_type": 0,
            "gender": 0,
        }
    ],
    blood_group=0,
    current_address={
    },
    permanent_address={
    },
    professional_summary="string_example",
    custom_fields={
        "key": None,
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The identifier.

##### display_name: `Optional[str]`<a id="display_name-optionalstr"></a>

##### first_name: `Optional[str]`<a id="first_name-optionalstr"></a>

##### middle_name: `Optional[str]`<a id="middle_name-optionalstr"></a>

##### last_name: `Optional[str]`<a id="last_name-optionalstr"></a>

##### gender: [`Gender`](./keka_hr_python_sdk/type/gender.py)<a id="gender-genderkeka_hr_python_sdktypegenderpy"></a>

##### date_of_birth: `Optional[datetime]`<a id="date_of_birth-optionaldatetime"></a>

##### work_phone: `Optional[str]`<a id="work_phone-optionalstr"></a>

##### home_phone: `Optional[str]`<a id="home_phone-optionalstr"></a>

##### personal_email: `Optional[str]`<a id="personal_email-optionalstr"></a>

##### skype_id: `Optional[str]`<a id="skype_id-optionalstr"></a>

##### marital_status: [`MaritalStatus`](./keka_hr_python_sdk/type/marital_status.py)<a id="marital_status-maritalstatuskeka_hr_python_sdktypemarital_statuspy"></a>

##### marriage_date: `Optional[datetime]`<a id="marriage_date-optionaldatetime"></a>

##### relations: List[`Relation`]<a id="relations-listrelation"></a>

##### blood_group: [`BloodGroup`](./keka_hr_python_sdk/type/blood_group.py)<a id="blood_group-bloodgroupkeka_hr_python_sdktypeblood_grouppy"></a>

##### current_address: [`Address`](./keka_hr_python_sdk/type/address.py)<a id="current_address-addresskeka_hr_python_sdktypeaddresspy"></a>


##### permanent_address: [`Address`](./keka_hr_python_sdk/type/address.py)<a id="permanent_address-addresskeka_hr_python_sdktypeaddresspy"></a>


##### professional_summary: `Optional[str]`<a id="professional_summary-optionalstr"></a>

##### custom_fields: [`PersonalDetailsUpdateRequestCustomFields`](./keka_hr_python_sdk/type/personal_details_update_request_custom_fields.py)<a id="custom_fields-personaldetailsupdaterequestcustomfieldskeka_hr_python_sdktypepersonal_details_update_request_custom_fieldspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PersonalDetailsUpdateRequest`](./keka_hr_python_sdk/type/personal_details_update_request.py)
The personal details.

#### 🔄 Return<a id="🔄-return"></a>

[`BooleanResponse`](./keka_hr_python_sdk/pydantic/boolean_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/hris/employees/{id}/personaldetails` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kekahr.expense.get_all_claims`<a id="kekahrexpenseget_all_claims"></a>

Get all Expense Claims

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_claims_response = kekahr.expense.get_all_claims(
    page_number=1,
    page_size=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page_number: `int`<a id="page_number-int"></a>

##### page_size: `int`<a id="page_size-int"></a>

Represents how many results you'd like to retrieve per request (page). Default is 100. Max is 200

#### 🔄 Return<a id="🔄-return"></a>

[`ExpenseClaimPagedResponse`](./keka_hr_python_sdk/pydantic/expense_claim_paged_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/expense/claims` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kekahr.expense_category.get_all_categories`<a id="kekahrexpense_categoryget_all_categories"></a>

Get all Expense Categories

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_categories_response = kekahr.expense_category.get_all_categories(
    expense_category_ids="string_example",
    page_number=1,
    page_size=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### expense_category_ids: `str`<a id="expense_category_ids-str"></a>

Comma separated list of one or more  expense categories identifiers you'd like to filter on.

##### page_number: `int`<a id="page_number-int"></a>

##### page_size: `int`<a id="page_size-int"></a>

Represents how many results you'd like to retrieve per request (page). Default is 100. Max is 200

#### 🔄 Return<a id="🔄-return"></a>

[`ExpenseCategoryPagedResponse`](./keka_hr_python_sdk/pydantic/expense_category_paged_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/expense/categories` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kekahr.expense_policy.list_all_expense_policies`<a id="kekahrexpense_policylist_all_expense_policies"></a>

Get all expensepolicies

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_expense_policies_response = kekahr.expense_policy.list_all_expense_policies(
    expensepolicy_ids="string_example",
    page_number=1,
    page_size=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### expensepolicy_ids: `str`<a id="expensepolicy_ids-str"></a>

The expensepolicy ids.

##### page_number: `int`<a id="page_number-int"></a>

##### page_size: `int`<a id="page_size-int"></a>

Represents how many results you'd like to retrieve per request (page). Default is 100. Max is 200

#### 🔄 Return<a id="🔄-return"></a>

[`ApiLookupPagedResponse`](./keka_hr_python_sdk/pydantic/api_lookup_paged_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/expensepolicies` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kekahr.goal.list_with_hierarchy`<a id="kekahrgoallist_with_hierarchy"></a>

Gets all goals along with parent goal and child goals

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_with_hierarchy_response = kekahr.goal.list_with_hierarchy(
    goal_ids="string_example",
    time_frame_ids="string_example",
    employee_ids="string_example",
    _from="1970-01-01T00:00:00.00Z",
    to="1970-01-01T00:00:00.00Z",
    page_number=1,
    page_size=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### goal_ids: `str`<a id="goal_ids-str"></a>

Comma separated list of one or more Goal ids you'd like to filter on.

##### time_frame_ids: `str`<a id="time_frame_ids-str"></a>

Comma separated list of one or more Time Frame ids you'd like to filter on.

##### employee_ids: `str`<a id="employee_ids-str"></a>

Comma separated list of one or more Employee ids you'd like to filter on.

##### _from: `datetime`<a id="_from-datetime"></a>

Date/time when goal time period will start, in ISO 8601 format (YYYY-MM-DDThh:mm:ss±hh). If not specified  defaults `to` - 60 days.

##### to: `datetime`<a id="to-datetime"></a>

Date/time when goal time period will end, in ISO 8601 format (YYYY-MM-DDThh:mm:ss±hh). If not specified  defaults `from` + 60 days.

##### page_number: `int`<a id="page_number-int"></a>

##### page_size: `int`<a id="page_size-int"></a>

Represents how many results you'd like to retrieve per request (page). Default is 100. Max is 200

#### 🔄 Return<a id="🔄-return"></a>

[`APIGoalPagedResponse`](./keka_hr_python_sdk/pydantic/api_goal_paged_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/pms/goals` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kekahr.goal.update_progress`<a id="kekahrgoalupdate_progress"></a>

Update the goal progress

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_progress_response = kekahr.goal.update_progress(
    current_value=3.14,
    status=0,
    updated_by="string_example",
    goal_id="goalId_example",
    note="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### current_value: `Union[int, float]`<a id="current_value-unionint-float"></a>

##### status: [`GoalStatus`](./keka_hr_python_sdk/type/goal_status.py)<a id="status-goalstatuskeka_hr_python_sdktypegoal_statuspy"></a>

##### updated_by: `str`<a id="updated_by-str"></a>

##### goal_id: `str`<a id="goal_id-str"></a>

The goal identifier.

##### note: `Optional[str]`<a id="note-optionalstr"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`APIUpdateGoalProgress`](./keka_hr_python_sdk/type/api_update_goal_progress.py)
The update goal progress view.

#### 🔄 Return<a id="🔄-return"></a>

[`BooleanResponse`](./keka_hr_python_sdk/pydantic/boolean_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/pms/goals/{goalId}/progress` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kekahr.groups.get_all`<a id="kekahrgroupsget_all"></a>

Get all Groups

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_response = kekahr.groups.get_all(
    group_type_ids="string_example",
    system_group_types="string_example",
    last_modified="1970-01-01T00:00:00.00Z",
    page_number=1,
    page_size=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### group_type_ids: `str`<a id="group_type_ids-str"></a>

Comma separated list of one or more Group Type Ids you’d like to filter on.

##### system_group_types: `str`<a id="system_group_types-str"></a>

Comma separated list of one or more System Group Type you’d like to filter on.

##### last_modified: `datetime`<a id="last_modified-datetime"></a>

The Last Modified.

##### page_number: `int`<a id="page_number-int"></a>

##### page_size: `int`<a id="page_size-int"></a>

Represents how many results you'd like to retrieve per request (page). Default is 100. Max is 200

#### 🔄 Return<a id="🔄-return"></a>

[`GroupPagedResponse`](./keka_hr_python_sdk/pydantic/group_paged_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/hris/groups` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kekahr.groups.get_all_group_types`<a id="kekahrgroupsget_all_group_types"></a>

Gets all Group Types.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_group_types_response = kekahr.groups.get_all_group_types(
    page_number=1,
    page_size=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page_number: `int`<a id="page_number-int"></a>

##### page_size: `int`<a id="page_size-int"></a>

Represents how many results you'd like to retrieve per request (page). Default is 100. Max is 200

#### 🔄 Return<a id="🔄-return"></a>

[`GroupTypePagedResponse`](./keka_hr_python_sdk/pydantic/group_type_paged_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/hris/grouptypes` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kekahr.holiday_calendar.get_all_holidays_calendar`<a id="kekahrholiday_calendarget_all_holidays_calendar"></a>

Get all holidays Calendar

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_holidays_calendar_response = kekahr.holiday_calendar.get_all_holidays_calendar(
    holidays_calendar_ids="string_example",
    page_number=1,
    page_size=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### holidays_calendar_ids: `str`<a id="holidays_calendar_ids-str"></a>

The holidaysCalendar ids.

##### page_number: `int`<a id="page_number-int"></a>

##### page_size: `int`<a id="page_size-int"></a>

Represents how many results you'd like to retrieve per request (page). Default is 100. Max is 200

#### 🔄 Return<a id="🔄-return"></a>

[`ApiLookupPagedResponse`](./keka_hr_python_sdk/pydantic/api_lookup_paged_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/time/holidayscalendar` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kekahr.job_title.get_all`<a id="kekahrjob_titleget_all"></a>

Get all jobtitles

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_response = kekahr.job_title.get_all(
    last_modified="1970-01-01T00:00:00.00Z",
    page_number=1,
    page_size=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### last_modified: `datetime`<a id="last_modified-datetime"></a>

The Last Modified.

##### page_number: `int`<a id="page_number-int"></a>

##### page_size: `int`<a id="page_size-int"></a>

Represents how many results you'd like to retrieve per request (page). Default is 100. Max is 200

#### 🔄 Return<a id="🔄-return"></a>

[`JobTitlePagedResponse`](./keka_hr_python_sdk/pydantic/job_title_paged_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/hris/jobtitles` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kekahr.jobs.add_candidate_note`<a id="kekahrjobsadd_candidate_note"></a>

Updated the candidate

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_candidate_note_response = kekahr.jobs.add_candidate_note(
    candidate_id="candidateId_example",
    job_id="jobId_example",
    tags=[
        "string_example"
    ],
    comments="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### candidate_id: `str`<a id="candidate_id-str"></a>

##### job_id: `str`<a id="job_id-str"></a>

##### tags: [`CandidateNoteDTOTags`](./keka_hr_python_sdk/type/candidate_note_dto_tags.py)<a id="tags-candidatenotedtotagskeka_hr_python_sdktypecandidate_note_dto_tagspy"></a>

##### comments: `Optional[str]`<a id="comments-optionalstr"></a>

Gets or sets the commnet

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CandidateNoteDTO`](./keka_hr_python_sdk/type/candidate_note_dto.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/hire/jobs/{jobId}/candidate/{candidateId}/notes` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kekahr.jobs.get_all_published_jobs`<a id="kekahrjobsget_all_published_jobs"></a>

Get all Published, Confidential and Archived jobs

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_published_jobs_response = kekahr.jobs.get_all_published_jobs(
    last_modified="1970-01-01T00:00:00.00Z",
    job_status=1,
    page_number=1,
    page_size=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### last_modified: `datetime`<a id="last_modified-datetime"></a>

##### job_status: `int`<a id="job_status-int"></a>

##### page_number: `int`<a id="page_number-int"></a>

##### page_size: `int`<a id="page_size-int"></a>

Represents how many results you'd like to retrieve per request (page). Default is 100. Max is 200

#### 🔄 Return<a id="🔄-return"></a>

[`JobsGetAllPublishedJobsResponse`](./keka_hr_python_sdk/pydantic/jobs_get_all_published_jobs_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/hire/jobs` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kekahr.jobs.get_application_fields`<a id="kekahrjobsget_application_fields"></a>

Get job application fields

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_application_fields_response = kekahr.jobs.get_application_fields(
    job_id="jobId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### job_id: `str`<a id="job_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`JobsGetApplicationFieldsResponse`](./keka_hr_python_sdk/pydantic/jobs_get_application_fields_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/hire/jobs/{jobId}/applicationfields` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kekahr.jobs.get_candidate_interviews`<a id="kekahrjobsget_candidate_interviews"></a>

Get interview scheduled and completed for a job and a candidate

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_candidate_interviews_response = kekahr.jobs.get_candidate_interviews(
    candidate_id="candidateId_example",
    job_id="jobId_example",
    page_number=1,
    page_size=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### candidate_id: `str`<a id="candidate_id-str"></a>

##### job_id: `str`<a id="job_id-str"></a>

##### page_number: `int`<a id="page_number-int"></a>

##### page_size: `int`<a id="page_size-int"></a>

Represents how many results you'd like to retrieve per request (page). Default is 100. Max is 200

#### 🔄 Return<a id="🔄-return"></a>

[`JobsGetCandidateInterviewsResponse`](./keka_hr_python_sdk/pydantic/jobs_get_candidate_interviews_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/hire/jobs/{jobId}/candidate/{candidateId}/interviews` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kekahr.jobs.get_candidate_scorecards`<a id="kekahrjobsget_candidate_scorecards"></a>

Get the scorecards which are submitted for a specified job candidate

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_candidate_scorecards_response = kekahr.jobs.get_candidate_scorecards(
    candidate_id="candidateId_example",
    job_id="jobId_example",
    page_number=1,
    page_size=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### candidate_id: `str`<a id="candidate_id-str"></a>

##### job_id: `str`<a id="job_id-str"></a>

##### page_number: `int`<a id="page_number-int"></a>

##### page_size: `int`<a id="page_size-int"></a>

Represents how many results you'd like to retrieve per request (page). Default is 100. Max is 200

#### 🔄 Return<a id="🔄-return"></a>

[`JobsGetCandidateScorecardsResponse`](./keka_hr_python_sdk/pydantic/jobs_get_candidate_scorecards_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/hire/jobs/{jobId}/candidate/{candidateId}/scorecards` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kekahr.jobs.get_candidates`<a id="kekahrjobsget_candidates"></a>

Get active or archived candidates in a specified job

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_candidates_response = kekahr.jobs.get_candidates(
    job_id="jobId_example",
    is_archived=False,
    last_modified="1970-01-01T00:00:00.00Z",
    page_number=1,
    page_size=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### job_id: `str`<a id="job_id-str"></a>

##### is_archived: `bool`<a id="is_archived-bool"></a>

##### last_modified: `datetime`<a id="last_modified-datetime"></a>

##### page_number: `int`<a id="page_number-int"></a>

##### page_size: `int`<a id="page_size-int"></a>

Represents how many results you'd like to retrieve per request (page). Default is 100. Max is 200

#### 🔄 Return<a id="🔄-return"></a>

[`JobsGetCandidatesResponse`](./keka_hr_python_sdk/pydantic/jobs_get_candidates_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/hire/jobs/{jobId}/candidates` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kekahr.jobs.post_candidate`<a id="kekahrjobspost_candidate"></a>

Post a candidate to a specified job

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
post_candidate_response = kekahr.jobs.post_candidate(
    job_id="jobId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### job_id: `str`<a id="job_id-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`JobsPostCandidateRequest1`](./keka_hr_python_sdk/type/jobs_post_candidate_request1.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/hire/jobs/{jobId}/candidate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kekahr.jobs.update_candidate`<a id="kekahrjobsupdate_candidate"></a>

Updated the candidate

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_candidate_response = kekahr.jobs.update_candidate(
    candidate_id="candidateId_example",
    job_id="jobId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### candidate_id: `str`<a id="candidate_id-str"></a>

##### job_id: `str`<a id="job_id-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`JobsUpdateCandidateRequest1`](./keka_hr_python_sdk/type/jobs_update_candidate_request1.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/hire/jobs/{jobId}/candidate/{candidateId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kekahr.leave_balance.get_all_balances`<a id="kekahrleave_balanceget_all_balances"></a>

Get all the leave balances

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_balances_response = kekahr.leave_balance.get_all_balances(
    employee_ids="string_example",
    leave_type_ids="string_example",
    page_number=1,
    page_size=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_ids: `str`<a id="employee_ids-str"></a>

The employee ids.

##### leave_type_ids: `str`<a id="leave_type_ids-str"></a>

The leave type ids.

##### page_number: `int`<a id="page_number-int"></a>

##### page_size: `int`<a id="page_size-int"></a>

Represents how many results you'd like to retrieve per request (page). Default is 100. Max is 200

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeeLeaveBalanceListItemPagedResponse`](./keka_hr_python_sdk/pydantic/employee_leave_balance_list_item_paged_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/time/leavebalance` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kekahr.leave_requests.create_request_identifier`<a id="kekahrleave_requestscreate_request_identifier"></a>

Create an leave request and returns leave request identifier.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_request_identifier_response = kekahr.leave_requests.create_request_identifier(
    employee_id="string_example",
    requested_by="string_example",
    from_date="1970-01-01T00:00:00.00Z",
    to_date="1970-01-01T00:00:00.00Z",
    leave_type_id="string_example",
    reason="string_example",
    from_session=0,
    to_session=0,
    note="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_id: `str`<a id="employee_id-str"></a>

##### requested_by: `str`<a id="requested_by-str"></a>

##### from_date: `datetime`<a id="from_date-datetime"></a>

##### to_date: `datetime`<a id="to_date-datetime"></a>

##### leave_type_id: `str`<a id="leave_type_id-str"></a>

##### reason: `str`<a id="reason-str"></a>

##### from_session: [`SessionType`](./keka_hr_python_sdk/type/session_type.py)<a id="from_session-sessiontypekeka_hr_python_sdktypesession_typepy"></a>

##### to_session: [`SessionType`](./keka_hr_python_sdk/type/session_type.py)<a id="to_session-sessiontypekeka_hr_python_sdktypesession_typepy"></a>

##### note: `Optional[str]`<a id="note-optionalstr"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PostLeaveRequest`](./keka_hr_python_sdk/type/post_leave_request.py)
The leave request.

#### 🔄 Return<a id="🔄-return"></a>

[`StringResponse`](./keka_hr_python_sdk/pydantic/string_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/time/leaverequests` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kekahr.leave_requests.get_all_between_dates`<a id="kekahrleave_requestsget_all_between_dates"></a>

Get all the leaves in the organization between `from` and `to` date.If both `from` and `to` are not specified, last 30 days records are returned.`from` date should be before `to` date.The difference between `from` and `to` date cannot be more than **90** days.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_between_dates_response = kekahr.leave_requests.get_all_between_dates(
    employee_ids="string_example",
    _from="1970-01-01T00:00:00.00Z",
    to="1970-01-01T00:00:00.00Z",
    page_number=1,
    page_size=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_ids: `str`<a id="employee_ids-str"></a>

Comma separated list of one or more Employee ids you'd like to filter on.

##### _from: `datetime`<a id="_from-datetime"></a>

From date.

##### to: `datetime`<a id="to-datetime"></a>

To date.

##### page_number: `int`<a id="page_number-int"></a>

##### page_size: `int`<a id="page_size-int"></a>

Represents how many results you'd like to retrieve per request (page). Default is 100. Max is 200

#### 🔄 Return<a id="🔄-return"></a>

[`LeaveRequestPagedResponse`](./keka_hr_python_sdk/pydantic/leave_request_paged_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/time/leaverequests` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kekahr.leave_types.list_all`<a id="kekahrleave_typeslist_all"></a>

Get all Leave Types

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_response = kekahr.leave_types.list_all(
    leave_type_ids="string_example",
    page_number=1,
    page_size=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### leave_type_ids: `str`<a id="leave_type_ids-str"></a>

Comma separated list of one or more leave type identifiers you'd like to filter on..

##### page_number: `int`<a id="page_number-int"></a>

##### page_size: `int`<a id="page_size-int"></a>

Represents how many results you'd like to retrieve per request (page). Default is 100. Max is 200

#### 🔄 Return<a id="🔄-return"></a>

[`LeaveTypePagedResponse`](./keka_hr_python_sdk/pydantic/leave_type_paged_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/time/leavetypes` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kekahr.locations.get_all`<a id="kekahrlocationsget_all"></a>

 Gets all Locations.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_response = kekahr.locations.get_all(
    last_modified="1970-01-01T00:00:00.00Z",
    page_number=1,
    page_size=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### last_modified: `datetime`<a id="last_modified-datetime"></a>

The Last Modified.

##### page_number: `int`<a id="page_number-int"></a>

##### page_size: `int`<a id="page_size-int"></a>

Represents how many results you'd like to retrieve per request (page). Default is 100. Max is 200

#### 🔄 Return<a id="🔄-return"></a>

[`LocationPagedResponse`](./keka_hr_python_sdk/pydantic/location_paged_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/hris/locations` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kekahr.notice_period.get_all`<a id="kekahrnotice_periodget_all"></a>

Get all noticeperiods

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_response = kekahr.notice_period.get_all(
    notice_period_ids="string_example",
    page_number=1,
    page_size=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### notice_period_ids: `str`<a id="notice_period_ids-str"></a>

The notice period ids.

##### page_number: `int`<a id="page_number-int"></a>

##### page_size: `int`<a id="page_size-int"></a>

Represents how many results you'd like to retrieve per request (page). Default is 100. Max is 200

#### 🔄 Return<a id="🔄-return"></a>

[`ApiLookupPagedResponse`](./keka_hr_python_sdk/pydantic/api_lookup_paged_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/hris/noticeperiods` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kekahr.pay_bands.get_all`<a id="kekahrpay_bandsget_all"></a>

Gets all Pay Bands.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_response = kekahr.pay_bands.get_all(
    pay_band_ids="string_example",
    page_number=1,
    page_size=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### pay_band_ids: `str`<a id="pay_band_ids-str"></a>

The payband ids.

##### page_number: `int`<a id="page_number-int"></a>

##### page_size: `int`<a id="page_size-int"></a>

Represents how many results you'd like to retrieve per request (page). Default is 100. Max is 200

#### 🔄 Return<a id="🔄-return"></a>

[`ApiLookupPagedResponse`](./keka_hr_python_sdk/pydantic/api_lookup_paged_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/payroll/paybands` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kekahr.pay_cycles.get_all`<a id="kekahrpay_cyclesget_all"></a>

Get all Pay Cycles

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_response = kekahr.pay_cycles.get_all(
    pay_group_id="payGroupId_example",
    run_status="string_example",
    page_number=1,
    page_size=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### pay_group_id: `str`<a id="pay_group_id-str"></a>

The Pay Group Id

##### run_status: `str`<a id="run_status-str"></a>

Comma separated list of one or more run Status you'd like to filter on, allowed values are Pending, Finalized, Partial.

##### page_number: `int`<a id="page_number-int"></a>

##### page_size: `int`<a id="page_size-int"></a>

Represents how many results you'd like to retrieve per request (page). Default is 100. Max is 200

#### 🔄 Return<a id="🔄-return"></a>

[`APIPayCycleViewPagedResponse`](./keka_hr_python_sdk/pydantic/api_pay_cycle_view_paged_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/payroll/paygroups/{payGroupId}/paycycles` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kekahr.pay_cycles.get_batch_payments`<a id="kekahrpay_cyclesget_batch_payments"></a>

Gets all payments for the specified pay group Id and pay cycle Id and pay batch Id / specified pay group id and pay cycle Id and pay batch Id and payment status filter

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_batch_payments_response = kekahr.pay_cycles.get_batch_payments(
    pay_group_id="payGroupId_example",
    pay_cycle_id="payCycleId_example",
    pay_batch_id="payBatchId_example",
    status="string_example",
    page_number=1,
    page_size=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### pay_group_id: `str`<a id="pay_group_id-str"></a>

The Pay Group Id

##### pay_cycle_id: `str`<a id="pay_cycle_id-str"></a>

The Pay cycle Id

##### pay_batch_id: `str`<a id="pay_batch_id-str"></a>

The Pay Batch Id

##### status: `str`<a id="status-str"></a>

Comma separated list of one or more payment Status you'd like to filter on, allowed values are UnPaid, Paid.

##### page_number: `int`<a id="page_number-int"></a>

##### page_size: `int`<a id="page_size-int"></a>

Represents how many results you'd like to retrieve per request (page). Default is 100. Max is 200

#### 🔄 Return<a id="🔄-return"></a>

[`EmployeePaymentPagedResponse`](./keka_hr_python_sdk/pydantic/employee_payment_paged_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/payroll/paygroups/{payGroupId}/paycycles/{payCycleId}/paybatches/{payBatchId}/payments` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kekahr.pay_cycles.get_pay_batches`<a id="kekahrpay_cyclesget_pay_batches"></a>

Get all Pay Batches

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_pay_batches_response = kekahr.pay_cycles.get_pay_batches(
    pay_group_id="payGroupId_example",
    pay_cycle_id="payCycleId_example",
    status="string_example",
    page_number=1,
    page_size=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### pay_group_id: `str`<a id="pay_group_id-str"></a>

The Pay Group Id

##### pay_cycle_id: `str`<a id="pay_cycle_id-str"></a>

The Pay cycle Id

##### status: `str`<a id="status-str"></a>

Comma separated list of one or more payment Status you'd like to filter on, allowed values are UnPaid, Paid.

##### page_number: `int`<a id="page_number-int"></a>

##### page_size: `int`<a id="page_size-int"></a>

Represents how many results you'd like to retrieve per request (page). Default is 100. Max is 200

#### 🔄 Return<a id="🔄-return"></a>

[`BatchPagedResponse`](./keka_hr_python_sdk/pydantic/batch_paged_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/payroll/paygroups/{payGroupId}/paycycles/{payCycleId}/paybatches` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kekahr.pay_cycles.get_pay_register`<a id="kekahrpay_cyclesget_pay_register"></a>

Get Pay Register

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_pay_register_response = kekahr.pay_cycles.get_pay_register(
    pay_group_id="payGroupId_example",
    pay_cycle_id="payCycleId_example",
    page_number=1,
    page_size=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### pay_group_id: `str`<a id="pay_group_id-str"></a>

The Pay Group Id

##### pay_cycle_id: `str`<a id="pay_cycle_id-str"></a>

The Pay cycle Id

##### page_number: `int`<a id="page_number-int"></a>

##### page_size: `int`<a id="page_size-int"></a>

Represents how many results you'd like to retrieve per request (page). Default is 100. Max is 200

#### 🔄 Return<a id="🔄-return"></a>

[`APIPayRegisterViewPagedResponse`](./keka_hr_python_sdk/pydantic/api_pay_register_view_paged_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/payroll/paygroups/{payGroupId}/paycycles/{payCycleId}/payregister` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kekahr.pay_cycles.update_payments_status`<a id="kekahrpay_cyclesupdate_payments_status"></a>

Update the Payments status.It will allow only 100 bulk transactions from that particular batch.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_payments_status_response = kekahr.pay_cycles.update_payments_status(
    body=[
        {
            "status": 0,
        }
    ],
    pay_group_id="payGroupId_example",
    pay_cycle_id="payCycleId_example",
    pay_batch_id="payBatchId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### pay_group_id: `str`<a id="pay_group_id-str"></a>

The Pay Group Id

##### pay_cycle_id: `str`<a id="pay_cycle_id-str"></a>

The Pay cycle Id

##### pay_batch_id: `str`<a id="pay_batch_id-str"></a>

The Pay Batch Id

##### requestBody: [`PayCyclesUpdatePaymentsStatusRequest1`](./keka_hr_python_sdk/type/pay_cycles_update_payments_status_request1.py)<a id="requestbody-paycyclesupdatepaymentsstatusrequest1keka_hr_python_sdktypepay_cycles_update_payments_status_request1py"></a>

The Payment Transactions.

#### 🔄 Return<a id="🔄-return"></a>

[`BooleanResponse`](./keka_hr_python_sdk/pydantic/boolean_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/payroll/paygroups/{payGroupId}/paycycles/{payCycleId}/paybatches/{payBatchId}/payments` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kekahr.pay_grades.get_all`<a id="kekahrpay_gradesget_all"></a>

Gets all Pay Grades.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_response = kekahr.pay_grades.get_all(
    pay_grade_ids="string_example",
    page_number=1,
    page_size=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### pay_grade_ids: `str`<a id="pay_grade_ids-str"></a>

The paygrade ids.

##### page_number: `int`<a id="page_number-int"></a>

##### page_size: `int`<a id="page_size-int"></a>

Represents how many results you'd like to retrieve per request (page). Default is 100. Max is 200

#### 🔄 Return<a id="🔄-return"></a>

[`ApiLookupPagedResponse`](./keka_hr_python_sdk/pydantic/api_lookup_paged_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/payroll/paygrades` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kekahr.pay_groups.get_all`<a id="kekahrpay_groupsget_all"></a>

Gets all Pay Groups.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_response = kekahr.pay_groups.get_all(
    page_number=1,
    page_size=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page_number: `int`<a id="page_number-int"></a>

##### page_size: `int`<a id="page_size-int"></a>

Represents how many results you'd like to retrieve per request (page). Default is 100. Max is 200

#### 🔄 Return<a id="🔄-return"></a>

[`APIPayGroupViewPagedResponse`](./keka_hr_python_sdk/pydantic/api_pay_group_view_paged_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/payroll/paygroups` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kekahr.praise.create_praise_identifier`<a id="kekahrpraisecreate_praise_identifier"></a>

Add an praise and returns created praise identifier.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_praise_identifier_response = kekahr.praise.create_praise_identifier(
    employee_ids=[
        "string_example"
    ],
    feedback="string_example",
    badge_id="string_example",
    given_by="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### employee_ids: [`AddPraiseEmployeeIds`](./keka_hr_python_sdk/type/add_praise_employee_ids.py)<a id="employee_ids-addpraiseemployeeidskeka_hr_python_sdktypeadd_praise_employee_idspy"></a>

##### feedback: `str`<a id="feedback-str"></a>

##### badge_id: `str`<a id="badge_id-str"></a>

##### given_by: `str`<a id="given_by-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AddPraise`](./keka_hr_python_sdk/type/add_praise.py)
The praise.

#### 🔄 Return<a id="🔄-return"></a>

[`StringResponse`](./keka_hr_python_sdk/pydantic/string_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/pms/praise` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kekahr.praise.list_employees_praises`<a id="kekahrpraiselist_employees_praises"></a>

Gets all employees praises

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_employees_praises_response = kekahr.praise.list_employees_praises(
    praise_ids="string_example",
    _from="1970-01-01T00:00:00.00Z",
    to="1970-01-01T00:00:00.00Z",
    page_number=1,
    page_size=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### praise_ids: `str`<a id="praise_ids-str"></a>

Comma separated list of one or more praise ids you'd like to filter on.

##### _from: `datetime`<a id="_from-datetime"></a>

Date/time from records to retrieve, in ISO 8601 format (YYYY-MM-DDThh:mm:ss±hh). If not specified defaults to `to - 30` days.

##### to: `datetime`<a id="to-datetime"></a>

Date/time to records to retrieve, in ISO 8601 format (YYYY-MM-DDThh:mm:ss±hh). If not specified defaults to `today`.

##### page_number: `int`<a id="page_number-int"></a>

##### page_size: `int`<a id="page_size-int"></a>

Represents how many results you'd like to retrieve per request (page). Default is 100. Max is 200

#### 🔄 Return<a id="🔄-return"></a>

[`APIPraisePagedResponse`](./keka_hr_python_sdk/pydantic/api_praise_paged_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/pms/praise` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kekahr.project_phases.create_phase_identifier`<a id="kekahrproject_phasescreate_phase_identifier"></a>

Create a Project Phase and returns created phase identifier

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_phase_identifier_response = kekahr.project_phases.create_phase_identifier(
    project_id="projectId_example",
    phase_name="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_id: `str`<a id="project_id-str"></a>

The project identifier.

##### phase_name: `str`<a id="phase_name-str"></a>

Name of the phase.

#### 🔄 Return<a id="🔄-return"></a>

[`StringResponse`](./keka_hr_python_sdk/pydantic/string_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/psa/projects/{projectId}/phases` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kekahr.project_phases.get_all`<a id="kekahrproject_phasesget_all"></a>

Get project phases.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_response = kekahr.project_phases.get_all(
    project_id="projectId_example",
    last_modified="1970-01-01T00:00:00.00Z",
    page_number=1,
    page_size=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_id: `str`<a id="project_id-str"></a>

The project identifier.

##### last_modified: `datetime`<a id="last_modified-datetime"></a>

Date/time when this time off request was last modified, in ISO 8601 format (YYYY-MM-DDThh:mm:ss±hh:mm).

##### page_number: `int`<a id="page_number-int"></a>

##### page_size: `int`<a id="page_size-int"></a>

Represents how many results you'd like to retrieve per request (page). Default is 100. Max is 200

#### 🔄 Return<a id="🔄-return"></a>

[`ProjectPhasePagedResponse`](./keka_hr_python_sdk/pydantic/project_phase_paged_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/psa/projects/{projectId}/phases` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kekahr.projects.create_project_identifier`<a id="kekahrprojectscreate_project_identifier"></a>

Create an Project and returns created project identifier.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_project_identifier_response = kekahr.projects.create_project_identifier(
    client_id="string_example",
    name="string_example",
    code="string_example",
    start_date="1970-01-01T00:00:00.00Z",
    end_date="1970-01-01T00:00:00.00Z",
    description="string_example",
    status=0,
    is_billable=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### client_id: `str`<a id="client_id-str"></a>

##### name: `str`<a id="name-str"></a>

##### code: `str`<a id="code-str"></a>

##### start_date: `datetime`<a id="start_date-datetime"></a>

##### end_date: `datetime`<a id="end_date-datetime"></a>

##### description: `Optional[str]`<a id="description-optionalstr"></a>

##### status: [`ProjectStatus`](./keka_hr_python_sdk/type/project_status.py)<a id="status-projectstatuskeka_hr_python_sdktypeproject_statuspy"></a>

##### is_billable: `bool`<a id="is_billable-bool"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Project`](./keka_hr_python_sdk/type/project.py)
The project.

#### 🔄 Return<a id="🔄-return"></a>

[`StringResponse`](./keka_hr_python_sdk/pydantic/string_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/psa/projects` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kekahr.projects.get_all`<a id="kekahrprojectsget_all"></a>

Get all projects.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_response = kekahr.projects.get_all(
    client_ids="string_example",
    last_modified="1970-01-01T00:00:00.00Z",
    page_number=1,
    page_size=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### client_ids: `str`<a id="client_ids-str"></a>

Comma separated list of one or more employee ids you'd like to filter on.

##### last_modified: `datetime`<a id="last_modified-datetime"></a>

Date/time when this time off request was last modified, in ISO 8601 format (YYYY-MM-DDThh:mm:ss±hh:mm).

##### page_number: `int`<a id="page_number-int"></a>

##### page_size: `int`<a id="page_size-int"></a>

Represents how many results you'd like to retrieve per request (page). Default is 100. Max is 200

#### 🔄 Return<a id="🔄-return"></a>

[`APIProjectPagedResponse`](./keka_hr_python_sdk/pydantic/api_project_paged_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/psa/projects` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kekahr.projects.get_allocations`<a id="kekahrprojectsget_allocations"></a>

Gets the specified project allocations based on identifier.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_allocations_response = kekahr.projects.get_allocations(
    id="id_example",
    last_modified="1970-01-01T00:00:00.00Z",
    page_number=1,
    page_size=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The identifier.

##### last_modified: `datetime`<a id="last_modified-datetime"></a>

The last modified.

##### page_number: `int`<a id="page_number-int"></a>

##### page_size: `int`<a id="page_size-int"></a>

Represents how many results you'd like to retrieve per request (page). Default is 100. Max is 200

#### 🔄 Return<a id="🔄-return"></a>

[`APIProjectAllocationPagedResponse`](./keka_hr_python_sdk/pydantic/api_project_allocation_paged_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/psa/projects/{id}/allocations` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kekahr.projects.get_by_id`<a id="kekahrprojectsget_by_id"></a>

Gets the specified project based on identifier.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = kekahr.projects.get_by_id(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The identifier.

#### 🔄 Return<a id="🔄-return"></a>

[`APIProjectResponse`](./keka_hr_python_sdk/pydantic/api_project_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/psa/projects/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kekahr.projects.get_timesheet_entries_between_dates`<a id="kekahrprojectsget_timesheet_entries_between_dates"></a>

Gets the project time entries between selected from and to date range.If both `from` and `to` are not specified, last 30 days records are returned.From `date` should be before `to` date.The difference between `from` and `to` date cannot be more than **90** days.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_timesheet_entries_between_dates_response = kekahr.projects.get_timesheet_entries_between_dates(
    id="id_example",
    _from="1970-01-01T00:00:00.00Z",
    to="1970-01-01T00:00:00.00Z",
    employee_ids="string_example",
    page_number=1,
    page_size=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The project identifier.

##### _from: `datetime`<a id="_from-datetime"></a>

Date from records to retrieve. If not specified defaults to `to - 30` days.

##### to: `datetime`<a id="to-datetime"></a>

Date to records can be retrieved. If not specified defaults to `today`.

##### employee_ids: `str`<a id="employee_ids-str"></a>

Comma separated list of one or more Employee ids you'd like to filter on.

##### page_number: `int`<a id="page_number-int"></a>

##### page_size: `int`<a id="page_size-int"></a>

Represents how many results you'd like to retrieve per request (page). Default is 100. Max is 200

#### 🔄 Return<a id="🔄-return"></a>

[`APITimesheetEntryPagedResponse`](./keka_hr_python_sdk/pydantic/api_timesheet_entry_paged_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/psa/projects/{id}/timeentries` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kekahr.projects.update_details`<a id="kekahrprojectsupdate_details"></a>

Update Project Details.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_details_response = kekahr.projects.update_details(
    id="id_example",
    description="string_example",
    name="string_example",
    code="string_example",
    status=0,
    start_date="1970-01-01T00:00:00.00Z",
    end_date="1970-01-01T00:00:00.00Z",
    is_billable=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The identifier.

##### description: `Optional[str]`<a id="description-optionalstr"></a>

##### name: `Optional[str]`<a id="name-optionalstr"></a>

##### code: `Optional[str]`<a id="code-optionalstr"></a>

##### status: [`ProjectStatus`](./keka_hr_python_sdk/type/project_status.py)<a id="status-projectstatuskeka_hr_python_sdktypeproject_statuspy"></a>

##### start_date: `Optional[datetime]`<a id="start_date-optionaldatetime"></a>

##### end_date: `Optional[datetime]`<a id="end_date-optionaldatetime"></a>

##### is_billable: `Optional[bool]`<a id="is_billable-optionalbool"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateProject`](./keka_hr_python_sdk/type/update_project.py)
The update project.

#### 🔄 Return<a id="🔄-return"></a>

[`BooleanResponse`](./keka_hr_python_sdk/pydantic/boolean_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/psa/projects/{id}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kekahr.requisition_request.get_all`<a id="kekahrrequisition_requestget_all"></a>

Get all Requisition Requests

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_response = kekahr.requisition_request.get_all(
    requisition_request_ids="string_example",
    status="string_example",
    last_modified="1970-01-01T00:00:00.00Z",
    page_number=1,
    page_size=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### requisition_request_ids: `str`<a id="requisition_request_ids-str"></a>

The requisition request ids.

##### status: `str`<a id="status-str"></a>

The status.

##### last_modified: `datetime`<a id="last_modified-datetime"></a>

The last modified.

##### page_number: `int`<a id="page_number-int"></a>

##### page_size: `int`<a id="page_size-int"></a>

Represents how many results you'd like to retrieve per request (page). Default is 100. Max is 200

#### 🔄 Return<a id="🔄-return"></a>

[`RequisitionRequestPagedResponse`](./keka_hr_python_sdk/pydantic/requisition_request_paged_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/requisition/requests` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kekahr.salary_components.get_all_components`<a id="kekahrsalary_componentsget_all_components"></a>

Gets all the salary components.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_components_response = kekahr.salary_components.get_all_components()
```

#### 🔄 Return<a id="🔄-return"></a>

[`APISalaryComponentPagedResponse`](./keka_hr_python_sdk/pydantic/api_salary_component_paged_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/payroll/salarycomponents` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kekahr.talent_pool.add_candidate`<a id="kekahrtalent_pooladd_candidate"></a>

Post a candidate to a specified talent pool

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_candidate_response = kekahr.talent_pool.add_candidate(
    talent_pool_id="talentPoolId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### talent_pool_id: `str`<a id="talent_pool_id-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TalentPoolAddCandidateRequest1`](./keka_hr_python_sdk/type/talent_pool_add_candidate_request1.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/hire/talentpool/{talentPoolId}/candidate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kekahr.talent_pool.get_all`<a id="kekahrtalent_poolget_all"></a>

Get all active talent pools

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_response = kekahr.talent_pool.get_all(
    last_modified="1970-01-01T00:00:00.00Z",
    page_number=1,
    page_size=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### last_modified: `datetime`<a id="last_modified-datetime"></a>

##### page_number: `int`<a id="page_number-int"></a>

##### page_size: `int`<a id="page_size-int"></a>

Represents how many results you'd like to retrieve per request (page). Default is 100. Max is 200

#### 🔄 Return<a id="🔄-return"></a>

[`TalentPoolGetAllResponse`](./keka_hr_python_sdk/pydantic/talent_pool_get_all_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/hire/talentpool` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kekahr.talent_pool.get_application_fields`<a id="kekahrtalent_poolget_application_fields"></a>

Get application fields of a specified talent pool

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_application_fields_response = kekahr.talent_pool.get_application_fields(
    talent_pool_id="talentPoolId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### talent_pool_id: `str`<a id="talent_pool_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`TalentPoolGetApplicationFieldsResponse`](./keka_hr_python_sdk/pydantic/talent_pool_get_application_fields_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/hire/talentpool/{talentPoolId}/applicationfields` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kekahr.talent_pool.get_candidates`<a id="kekahrtalent_poolget_candidates"></a>

Get candidates in a specified talent pool

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_candidates_response = kekahr.talent_pool.get_candidates(
    talent_pool_id="talentPoolId_example",
    last_modified="1970-01-01T00:00:00.00Z",
    page_number=1,
    page_size=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### talent_pool_id: `str`<a id="talent_pool_id-str"></a>

##### last_modified: `datetime`<a id="last_modified-datetime"></a>

##### page_number: `int`<a id="page_number-int"></a>

##### page_size: `int`<a id="page_size-int"></a>

Represents how many results you'd like to retrieve per request (page). Default is 100. Max is 200

#### 🔄 Return<a id="🔄-return"></a>

[`TalentPoolGetCandidatesResponse`](./keka_hr_python_sdk/pydantic/talent_pool_get_candidates_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/hire/talentpool/{talentPoolId}/candidates` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kekahr.tasks.create_task_identifier`<a id="kekahrtaskscreate_task_identifier"></a>

Create project task and returns created task identifier.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_task_identifier_response = kekahr.tasks.create_task_identifier(
    project_id="string_example",
    name="string_example",
    start_date="1970-01-01T00:00:00.00Z",
    end_date="1970-01-01T00:00:00.00Z",
    project_id="projectId_example",
    description="string_example",
    task_billing_type=0,
    assigned_to=[
        "string_example"
    ],
    estimated_hours=3.14,
    phase_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_id: `str`<a id="project_id-str"></a>

The project identifier.

##### requestBody: [`ProjectTask`](./keka_hr_python_sdk/type/project_task.py)<a id="requestbody-projecttaskkeka_hr_python_sdktypeproject_taskpy"></a>

The project task.

#### 🔄 Return<a id="🔄-return"></a>

[`StringResponse`](./keka_hr_python_sdk/pydantic/string_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/psa/projects/{projectId}/tasks` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kekahr.tasks.get_all`<a id="kekahrtasksget_all"></a>

Gets the project tasks.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_response = kekahr.tasks.get_all(
    project_id="projectId_example",
    last_modified="1970-01-01T00:00:00.00Z",
    page_number=1,
    page_size=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_id: `str`<a id="project_id-str"></a>

The project identifier.

##### last_modified: `datetime`<a id="last_modified-datetime"></a>

Date/time when this time off request was last modified, in ISO 8601 format (YYYY-MM-DDThh:mm:ss±hh:mm).

##### page_number: `int`<a id="page_number-int"></a>

##### page_size: `int`<a id="page_size-int"></a>

Represents how many results you'd like to retrieve per request (page). Default is 100. Max is 200

#### 🔄 Return<a id="🔄-return"></a>

[`APIProjectTaskPagedResponse`](./keka_hr_python_sdk/pydantic/api_project_task_paged_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/psa/projects/{projectId}/tasks` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kekahr.tasks.list_time_entries_between_dates`<a id="kekahrtaskslist_time_entries_between_dates"></a>

Gets the project task time entries between selected from and to date range.If both `from` and `to` are not specified, last 30 days records are returned.From `date` should be before `to` date.The difference between `from` and `to` date cannot be more than **90** days.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_time_entries_between_dates_response = kekahr.tasks.list_time_entries_between_dates(
    project_id="projectId_example",
    task_id="taskId_example",
    _from="1970-01-01T00:00:00.00Z",
    to="1970-01-01T00:00:00.00Z",
    employee_ids="string_example",
    page_number=1,
    page_size=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_id: `str`<a id="project_id-str"></a>

The project identifier.

##### task_id: `str`<a id="task_id-str"></a>

The task identifier.

##### _from: `datetime`<a id="_from-datetime"></a>

Date from records to retrieve. If not specified defaults to `to - 30` days.

##### to: `datetime`<a id="to-datetime"></a>

Date to records can be retrieved. If not specified defaults to `today`.

##### employee_ids: `str`<a id="employee_ids-str"></a>

Comma separated list of one or more Employee ids you'd like to filter on.

##### page_number: `int`<a id="page_number-int"></a>

##### page_size: `int`<a id="page_size-int"></a>

Represents how many results you'd like to retrieve per request (page). Default is 100. Max is 200

#### 🔄 Return<a id="🔄-return"></a>

[`APITimesheetEntryPagedResponse`](./keka_hr_python_sdk/pydantic/api_timesheet_entry_paged_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/psa/projects/{projectId}/tasks/{taskId}/timeentries` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kekahr.tasks.update_task`<a id="kekahrtasksupdate_task"></a>

Update project task.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_task_response = kekahr.tasks.update_task(
    project_id="projectId_example",
    task_id="taskId_example",
    description="string_example",
    name="string_example",
    task_billing_type=0,
    assigned_to=[
        "string_example"
    ],
    start_date="1970-01-01T00:00:00.00Z",
    end_date="1970-01-01T00:00:00.00Z",
    estimated_hours=3.14,
    phase_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_id: `str`<a id="project_id-str"></a>

The project identifier.

##### task_id: `str`<a id="task_id-str"></a>

The task identifier.

##### description: `Optional[str]`<a id="description-optionalstr"></a>

##### name: `Optional[str]`<a id="name-optionalstr"></a>

##### task_billing_type: [`TaskBillingType`](./keka_hr_python_sdk/type/task_billing_type.py)<a id="task_billing_type-taskbillingtypekeka_hr_python_sdktypetask_billing_typepy"></a>

##### assigned_to: [`UpdateProjectTaskAssignedTo`](./keka_hr_python_sdk/type/update_project_task_assigned_to.py)<a id="assigned_to-updateprojecttaskassignedtokeka_hr_python_sdktypeupdate_project_task_assigned_topy"></a>

##### start_date: `Optional[datetime]`<a id="start_date-optionaldatetime"></a>

##### end_date: `Optional[datetime]`<a id="end_date-optionaldatetime"></a>

##### estimated_hours: `Optional[Union[int, float]]`<a id="estimated_hours-optionalunionint-float"></a>

##### phase_id: `Optional[str]`<a id="phase_id-optionalstr"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UpdateProjectTask`](./keka_hr_python_sdk/type/update_project_task.py)
The project task.

#### 🔄 Return<a id="🔄-return"></a>

[`BooleanResponse`](./keka_hr_python_sdk/pydantic/boolean_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/psa/projects/{projectId}/tasks/{taskId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kekahr.time_frames.get_all`<a id="kekahrtime_framesget_all"></a>

Gets all time frames.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_response = kekahr.time_frames.get_all(
    time_frame_ids="string_example",
    page_number=1,
    page_size=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### time_frame_ids: `str`<a id="time_frame_ids-str"></a>

Comma separated list of one or more Time Frame ids you'd like to filter on.

##### page_number: `int`<a id="page_number-int"></a>

##### page_size: `int`<a id="page_size-int"></a>

Represents how many results you'd like to retrieve per request (page). Default is 100. Max is 200

#### 🔄 Return<a id="🔄-return"></a>

[`APITimeFramePagedResponse`](./keka_hr_python_sdk/pydantic/api_time_frame_paged_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/pms/timeframes` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `kekahr.timesheet_entries.get_between_dates`<a id="kekahrtimesheet_entriesget_between_dates"></a>

Gets the time entries between selected from and to date range.If both `from` and `to` are not specified, last 30 days records are returned.From `date` should be before `to` date.The difference between `from` and `to` date cannot be more than **90** days.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_between_dates_response = kekahr.timesheet_entries.get_between_dates(
    _from="1970-01-01T00:00:00.00Z",
    to="1970-01-01T00:00:00.00Z",
    employee_ids="string_example",
    project_ids="string_example",
    task_ids="string_example",
    page_number=1,
    page_size=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### _from: `datetime`<a id="_from-datetime"></a>

Date from records to retrieve. If not specified defaults to `to - 30` days.

##### to: `datetime`<a id="to-datetime"></a>

Date to records can be retrieved. If not specified defaults to `today`.

##### employee_ids: `str`<a id="employee_ids-str"></a>

Comma separated list of one or more Employee ids you'd like to filter on.

##### project_ids: `str`<a id="project_ids-str"></a>

Comma separated list of one or more project ids you'd like to filter on.

##### task_ids: `str`<a id="task_ids-str"></a>

Comma separated list of one or more task ids you'd like to filter on.

##### page_number: `int`<a id="page_number-int"></a>

##### page_size: `int`<a id="page_size-int"></a>

Represents how many results you'd like to retrieve per request (page). Default is 100. Max is 200

#### 🔄 Return<a id="🔄-return"></a>

[`APITimesheetEntryPagedResponse`](./keka_hr_python_sdk/pydantic/api_timesheet_entry_paged_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/psa/timeentries` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
