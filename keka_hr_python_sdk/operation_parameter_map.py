operation_parameter_map = {
    '/assets-GET': {
        'parameters': [
            {
                'name': 'assetIds'
            },
            {
                'name': 'employeeIds'
            },
            {
                'name': 'assetStatus'
            },
            {
                'name': 'lastModified'
            },
            {
                'name': 'pageNumber'
            },
            {
                'name': 'pageSize'
            },
        ]
    },
    '/assets/categories-GET': {
        'parameters': [
            {
                'name': 'assetCategoryIds'
            },
            {
                'name': 'lastModified'
            },
            {
                'name': 'pageNumber'
            },
            {
                'name': 'pageSize'
            },
        ]
    },
    '/assets/conditions-GET': {
        'parameters': [
            {
                'name': 'assetConditionIds'
            },
            {
                'name': 'lastModified'
            },
            {
                'name': 'pageNumber'
            },
            {
                'name': 'pageSize'
            },
        ]
    },
    '/assets/types-GET': {
        'parameters': [
            {
                'name': 'assetTypeIds'
            },
            {
                'name': 'lastModified'
            },
            {
                'name': 'pageNumber'
            },
            {
                'name': 'pageSize'
            },
        ]
    },
    '/time/attendance-GET': {
        'parameters': [
            {
                'name': 'employeeIds'
            },
            {
                'name': 'from'
            },
            {
                'name': 'to'
            },
            {
                'name': 'pageNumber'
            },
            {
                'name': 'pageSize'
            },
        ]
    },
    '/time/capturescheme-GET': {
        'parameters': [
            {
                'name': 'captureschemeIds'
            },
            {
                'name': 'pageNumber'
            },
            {
                'name': 'pageSize'
            },
        ]
    },
    '/connect/token-POST': {
        'parameters': [
            {
                'name': 'grant_type'
            },
            {
                'name': 'scope'
            },
            {
                'name': 'client_id'
            },
            {
                'name': 'client_secret'
            },
            {
                'name': 'api_key'
            },
        ]
    },
    '/pms/badges-GET': {
        'parameters': [
            {
                'name': 'badgeIds'
            },
            {
                'name': 'pageNumber'
            },
            {
                'name': 'pageSize'
            },
        ]
    },
    '/psa/clients-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'code'
            },
            {
                'name': 'description'
            },
            {
                'name': 'billingInfo'
            },
            {
                'name': 'phone'
            },
            {
                'name': 'website'
            },
            {
                'name': 'email'
            },
        ]
    },
    '/psa/clients-GET': {
        'parameters': [
            {
                'name': 'clientIds'
            },
            {
                'name': 'lastModified'
            },
            {
                'name': 'pageNumber'
            },
            {
                'name': 'pageSize'
            },
        ]
    },
    '/psa/clients/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/psa/clients/{id}-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'description'
            },
            {
                'name': 'name'
            },
            {
                'name': 'code'
            },
            {
                'name': 'billingAddress'
            },
        ]
    },
    '/hris/currencies-GET': {
        'parameters': [
            {
                'name': 'pageNumber'
            },
            {
                'name': 'pageSize'
            },
        ]
    },
    '/hris/departments-GET': {
        'parameters': [
            {
                'name': 'departmentIds'
            },
            {
                'name': 'lastModified'
            },
            {
                'name': 'pageNumber'
            },
            {
                'name': 'pageSize'
            },
        ]
    },
    '/hris/employees-POST': {
        'parameters': [
            {
                'name': 'displayName'
            },
            {
                'name': 'firstName'
            },
            {
                'name': 'lastName'
            },
            {
                'name': 'email'
            },
            {
                'name': 'gender'
            },
            {
                'name': 'dateOfBirth'
            },
            {
                'name': 'dateJoined'
            },
            {
                'name': 'department'
            },
            {
                'name': 'businessUnit'
            },
            {
                'name': 'jobTitle'
            },
            {
                'name': 'location'
            },
            {
                'name': 'employeeNumber'
            },
            {
                'name': 'middleName'
            },
            {
                'name': 'mobileNumber'
            },
            {
                'name': 'secondaryJobTitle'
            },
        ]
    },
    '/hris/employees-GET': {
        'parameters': [
            {
                'name': 'employeeIds'
            },
            {
                'name': 'employeeNumbers'
            },
            {
                'name': 'employmentStatus'
            },
            {
                'name': 'inProbation'
            },
            {
                'name': 'inNoticePeriod'
            },
            {
                'name': 'lastModified'
            },
            {
                'name': 'pageNumber'
            },
            {
                'name': 'pageSize'
            },
        ]
    },
    '/hris/employees/updatefields-GET': {
        'parameters': [
            {
                'name': 'pageNumber'
            },
            {
                'name': 'pageSize'
            },
        ]
    },
    '/hris/employees/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/hris/employees/{id}/jobdetails-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'employeeNumber'
            },
            {
                'name': 'location'
            },
            {
                'name': 'businessUnit'
            },
            {
                'name': 'department'
            },
            {
                'name': 'jobTitle'
            },
            {
                'name': 'reportingManager'
            },
            {
                'name': 'attendanceNumber'
            },
            {
                'name': 'timeType'
            },
            {
                'name': 'attendanceCaptureScheme'
            },
            {
                'name': 'expensePolicy'
            },
            {
                'name': 'noticePeriod'
            },
            {
                'name': 'holidayList'
            },
            {
                'name': 'costCenter'
            },
            {
                'name': 'payBand'
            },
            {
                'name': 'payGrade'
            },
            {
                'name': 'customFields'
            },
        ]
    },
    '/hris/employees/{id}/personaldetails-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'displayName'
            },
            {
                'name': 'firstName'
            },
            {
                'name': 'middleName'
            },
            {
                'name': 'lastName'
            },
            {
                'name': 'gender'
            },
            {
                'name': 'dateOfBirth'
            },
            {
                'name': 'workPhone'
            },
            {
                'name': 'homePhone'
            },
            {
                'name': 'personalEmail'
            },
            {
                'name': 'skypeId'
            },
            {
                'name': 'maritalStatus'
            },
            {
                'name': 'marriageDate'
            },
            {
                'name': 'relations'
            },
            {
                'name': 'bloodGroup'
            },
            {
                'name': 'currentAddress'
            },
            {
                'name': 'permanentAddress'
            },
            {
                'name': 'professionalSummary'
            },
            {
                'name': 'customFields'
            },
        ]
    },
    '/expense/claims-GET': {
        'parameters': [
            {
                'name': 'pageNumber'
            },
            {
                'name': 'pageSize'
            },
        ]
    },
    '/expense/categories-GET': {
        'parameters': [
            {
                'name': 'expenseCategoryIds'
            },
            {
                'name': 'pageNumber'
            },
            {
                'name': 'pageSize'
            },
        ]
    },
    '/expensepolicies-GET': {
        'parameters': [
            {
                'name': 'expensepolicyIds'
            },
            {
                'name': 'pageNumber'
            },
            {
                'name': 'pageSize'
            },
        ]
    },
    '/pms/goals-GET': {
        'parameters': [
            {
                'name': 'goalIds'
            },
            {
                'name': 'timeFrameIds'
            },
            {
                'name': 'employeeIds'
            },
            {
                'name': 'from'
            },
            {
                'name': 'to'
            },
            {
                'name': 'pageNumber'
            },
            {
                'name': 'pageSize'
            },
        ]
    },
    '/pms/goals/{goalId}/progress-PUT': {
        'parameters': [
            {
                'name': 'currentValue'
            },
            {
                'name': 'status'
            },
            {
                'name': 'updatedBy'
            },
            {
                'name': 'goalId'
            },
            {
                'name': 'note'
            },
        ]
    },
    '/hris/groups-GET': {
        'parameters': [
            {
                'name': 'groupTypeIds'
            },
            {
                'name': 'systemGroupTypes'
            },
            {
                'name': 'lastModified'
            },
            {
                'name': 'pageNumber'
            },
            {
                'name': 'pageSize'
            },
        ]
    },
    '/hris/grouptypes-GET': {
        'parameters': [
            {
                'name': 'pageNumber'
            },
            {
                'name': 'pageSize'
            },
        ]
    },
    '/time/holidayscalendar-GET': {
        'parameters': [
            {
                'name': 'holidaysCalendarIds'
            },
            {
                'name': 'pageNumber'
            },
            {
                'name': 'pageSize'
            },
        ]
    },
    '/hris/jobtitles-GET': {
        'parameters': [
            {
                'name': 'lastModified'
            },
            {
                'name': 'pageNumber'
            },
            {
                'name': 'pageSize'
            },
        ]
    },
    '/v1/hire/jobs/{jobId}/candidate/{candidateId}/notes-POST': {
        'parameters': [
            {
                'name': 'candidateId'
            },
            {
                'name': 'jobId'
            },
            {
                'name': 'tags'
            },
            {
                'name': 'comments'
            },
        ]
    },
    '/v1/hire/jobs-GET': {
        'parameters': [
            {
                'name': 'lastModified'
            },
            {
                'name': 'JobStatus'
            },
            {
                'name': 'pageNumber'
            },
            {
                'name': 'pageSize'
            },
        ]
    },
    '/v1/hire/jobs/{jobId}/applicationfields-GET': {
        'parameters': [
            {
                'name': 'jobId'
            },
        ]
    },
    '/v1/hire/jobs/{jobId}/candidate/{candidateId}/interviews-GET': {
        'parameters': [
            {
                'name': 'candidateId'
            },
            {
                'name': 'jobId'
            },
            {
                'name': 'pageNumber'
            },
            {
                'name': 'pageSize'
            },
        ]
    },
    '/v1/hire/jobs/{jobId}/candidate/{candidateId}/scorecards-GET': {
        'parameters': [
            {
                'name': 'candidateId'
            },
            {
                'name': 'jobId'
            },
            {
                'name': 'pageNumber'
            },
            {
                'name': 'pageSize'
            },
        ]
    },
    '/v1/hire/jobs/{jobId}/candidates-GET': {
        'parameters': [
            {
                'name': 'jobId'
            },
            {
                'name': 'isArchived'
            },
            {
                'name': 'lastModified'
            },
            {
                'name': 'pageNumber'
            },
            {
                'name': 'pageSize'
            },
        ]
    },
    '/v1/hire/jobs/{jobId}/candidate-POST': {
        'parameters': [
            {
                'name': 'jobId'
            },
        ]
    },
    '/v1/hire/jobs/{jobId}/candidate/{candidateId}-PUT': {
        'parameters': [
            {
                'name': 'candidateId'
            },
            {
                'name': 'jobId'
            },
        ]
    },
    '/time/leavebalance-GET': {
        'parameters': [
            {
                'name': 'employeeIds'
            },
            {
                'name': 'leaveTypeIds'
            },
            {
                'name': 'pageNumber'
            },
            {
                'name': 'pageSize'
            },
        ]
    },
    '/time/leaverequests-POST': {
        'parameters': [
            {
                'name': 'employeeId'
            },
            {
                'name': 'requestedBy'
            },
            {
                'name': 'fromDate'
            },
            {
                'name': 'toDate'
            },
            {
                'name': 'leaveTypeId'
            },
            {
                'name': 'reason'
            },
            {
                'name': 'fromSession'
            },
            {
                'name': 'toSession'
            },
            {
                'name': 'note'
            },
        ]
    },
    '/time/leaverequests-GET': {
        'parameters': [
            {
                'name': 'employeeIds'
            },
            {
                'name': 'from'
            },
            {
                'name': 'to'
            },
            {
                'name': 'pageNumber'
            },
            {
                'name': 'pageSize'
            },
        ]
    },
    '/time/leavetypes-GET': {
        'parameters': [
            {
                'name': 'leaveTypeIds'
            },
            {
                'name': 'pageNumber'
            },
            {
                'name': 'pageSize'
            },
        ]
    },
    '/hris/locations-GET': {
        'parameters': [
            {
                'name': 'lastModified'
            },
            {
                'name': 'pageNumber'
            },
            {
                'name': 'pageSize'
            },
        ]
    },
    '/hris/noticeperiods-GET': {
        'parameters': [
            {
                'name': 'noticePeriodIds'
            },
            {
                'name': 'pageNumber'
            },
            {
                'name': 'pageSize'
            },
        ]
    },
    '/payroll/paybands-GET': {
        'parameters': [
            {
                'name': 'payBandIds'
            },
            {
                'name': 'pageNumber'
            },
            {
                'name': 'pageSize'
            },
        ]
    },
    '/payroll/paygroups/{payGroupId}/paycycles-GET': {
        'parameters': [
            {
                'name': 'payGroupId'
            },
            {
                'name': 'runStatus'
            },
            {
                'name': 'pageNumber'
            },
            {
                'name': 'pageSize'
            },
        ]
    },
    '/payroll/paygroups/{payGroupId}/paycycles/{payCycleId}/paybatches/{payBatchId}/payments-GET': {
        'parameters': [
            {
                'name': 'payGroupId'
            },
            {
                'name': 'payCycleId'
            },
            {
                'name': 'payBatchId'
            },
            {
                'name': 'status'
            },
            {
                'name': 'pageNumber'
            },
            {
                'name': 'pageSize'
            },
        ]
    },
    '/payroll/paygroups/{payGroupId}/paycycles/{payCycleId}/paybatches-GET': {
        'parameters': [
            {
                'name': 'payGroupId'
            },
            {
                'name': 'payCycleId'
            },
            {
                'name': 'status'
            },
            {
                'name': 'pageNumber'
            },
            {
                'name': 'pageSize'
            },
        ]
    },
    '/payroll/paygroups/{payGroupId}/paycycles/{payCycleId}/payregister-GET': {
        'parameters': [
            {
                'name': 'payGroupId'
            },
            {
                'name': 'payCycleId'
            },
            {
                'name': 'pageNumber'
            },
            {
                'name': 'pageSize'
            },
        ]
    },
    '/payroll/paygroups/{payGroupId}/paycycles/{payCycleId}/paybatches/{payBatchId}/payments-PUT': {
        'parameters': [
            {
                'name': 'payGroupId'
            },
            {
                'name': 'payCycleId'
            },
            {
                'name': 'payBatchId'
            },
        ]
    },
    '/payroll/paygrades-GET': {
        'parameters': [
            {
                'name': 'payGradeIds'
            },
            {
                'name': 'pageNumber'
            },
            {
                'name': 'pageSize'
            },
        ]
    },
    '/payroll/paygroups-GET': {
        'parameters': [
            {
                'name': 'pageNumber'
            },
            {
                'name': 'pageSize'
            },
        ]
    },
    '/pms/praise-POST': {
        'parameters': [
            {
                'name': 'employeeIds'
            },
            {
                'name': 'feedback'
            },
            {
                'name': 'badgeId'
            },
            {
                'name': 'givenBy'
            },
        ]
    },
    '/pms/praise-GET': {
        'parameters': [
            {
                'name': 'praiseIds'
            },
            {
                'name': 'from'
            },
            {
                'name': 'to'
            },
            {
                'name': 'pageNumber'
            },
            {
                'name': 'pageSize'
            },
        ]
    },
    '/psa/projects/{projectId}/phases-POST': {
        'parameters': [
            {
                'name': 'projectId'
            },
            {
                'name': 'phaseName'
            },
        ]
    },
    '/psa/projects/{projectId}/phases-GET': {
        'parameters': [
            {
                'name': 'projectId'
            },
            {
                'name': 'lastModified'
            },
            {
                'name': 'pageNumber'
            },
            {
                'name': 'pageSize'
            },
        ]
    },
    '/psa/projects-POST': {
        'parameters': [
            {
                'name': 'clientId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'code'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'endDate'
            },
            {
                'name': 'description'
            },
            {
                'name': 'status'
            },
            {
                'name': 'isBillable'
            },
        ]
    },
    '/psa/projects-GET': {
        'parameters': [
            {
                'name': 'clientIds'
            },
            {
                'name': 'lastModified'
            },
            {
                'name': 'pageNumber'
            },
            {
                'name': 'pageSize'
            },
        ]
    },
    '/psa/projects/{id}/allocations-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'lastModified'
            },
            {
                'name': 'pageNumber'
            },
            {
                'name': 'pageSize'
            },
        ]
    },
    '/psa/projects/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/psa/projects/{id}/timeentries-GET': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'from'
            },
            {
                'name': 'to'
            },
            {
                'name': 'employeeIds'
            },
            {
                'name': 'pageNumber'
            },
            {
                'name': 'pageSize'
            },
        ]
    },
    '/psa/projects/{id}-PUT': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'description'
            },
            {
                'name': 'name'
            },
            {
                'name': 'code'
            },
            {
                'name': 'status'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'endDate'
            },
            {
                'name': 'isBillable'
            },
        ]
    },
    '/requisition/requests-GET': {
        'parameters': [
            {
                'name': 'requisitionRequestIds'
            },
            {
                'name': 'status'
            },
            {
                'name': 'lastModified'
            },
            {
                'name': 'pageNumber'
            },
            {
                'name': 'pageSize'
            },
        ]
    },
    '/payroll/salarycomponents-GET': {
        'parameters': [
        ]
    },
    '/v1/hire/talentpool/{talentPoolId}/candidate-POST': {
        'parameters': [
            {
                'name': 'talentPoolId'
            },
        ]
    },
    '/v1/hire/talentpool-GET': {
        'parameters': [
            {
                'name': 'lastModified'
            },
            {
                'name': 'pageNumber'
            },
            {
                'name': 'pageSize'
            },
        ]
    },
    '/v1/hire/talentpool/{talentPoolId}/applicationfields-GET': {
        'parameters': [
            {
                'name': 'talentPoolId'
            },
        ]
    },
    '/v1/hire/talentpool/{talentPoolId}/candidates-GET': {
        'parameters': [
            {
                'name': 'talentPoolId'
            },
            {
                'name': 'lastModified'
            },
            {
                'name': 'pageNumber'
            },
            {
                'name': 'pageSize'
            },
        ]
    },
    '/psa/projects/{projectId}/tasks-POST': {
        'parameters': [
            {
                'name': 'projectId'
            },
            {
                'name': 'name'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'endDate'
            },
            {
                'name': 'projectId'
            },
            {
                'name': 'description'
            },
            {
                'name': 'taskBillingType'
            },
            {
                'name': 'assignedTo'
            },
            {
                'name': 'estimatedHours'
            },
            {
                'name': 'phaseId'
            },
        ]
    },
    '/psa/projects/{projectId}/tasks-GET': {
        'parameters': [
            {
                'name': 'projectId'
            },
            {
                'name': 'lastModified'
            },
            {
                'name': 'pageNumber'
            },
            {
                'name': 'pageSize'
            },
        ]
    },
    '/psa/projects/{projectId}/tasks/{taskId}/timeentries-GET': {
        'parameters': [
            {
                'name': 'projectId'
            },
            {
                'name': 'taskId'
            },
            {
                'name': 'from'
            },
            {
                'name': 'to'
            },
            {
                'name': 'employeeIds'
            },
            {
                'name': 'pageNumber'
            },
            {
                'name': 'pageSize'
            },
        ]
    },
    '/psa/projects/{projectId}/tasks/{taskId}-PUT': {
        'parameters': [
            {
                'name': 'projectId'
            },
            {
                'name': 'taskId'
            },
            {
                'name': 'description'
            },
            {
                'name': 'name'
            },
            {
                'name': 'taskBillingType'
            },
            {
                'name': 'assignedTo'
            },
            {
                'name': 'startDate'
            },
            {
                'name': 'endDate'
            },
            {
                'name': 'estimatedHours'
            },
            {
                'name': 'phaseId'
            },
        ]
    },
    '/pms/timeframes-GET': {
        'parameters': [
            {
                'name': 'timeFrameIds'
            },
            {
                'name': 'pageNumber'
            },
            {
                'name': 'pageSize'
            },
        ]
    },
    '/psa/timeentries-GET': {
        'parameters': [
            {
                'name': 'from'
            },
            {
                'name': 'to'
            },
            {
                'name': 'employeeIds'
            },
            {
                'name': 'projectIds'
            },
            {
                'name': 'taskIds'
            },
            {
                'name': 'pageNumber'
            },
            {
                'name': 'pageSize'
            },
        ]
    },
};