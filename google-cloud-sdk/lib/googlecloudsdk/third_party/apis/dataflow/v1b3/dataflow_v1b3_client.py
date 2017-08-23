"""Generated client library for dataflow version v1b3."""
# NOTE: This file is autogenerated and should not be edited by hand.
from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.dataflow.v1b3 import dataflow_v1b3_messages as messages


class DataflowV1b3(base_api.BaseApiClient):
  """Generated client library for service dataflow version v1b3."""

  MESSAGES_MODULE = messages
  BASE_URL = u'https://dataflow.googleapis.com/'

  _PACKAGE = u'dataflow'
  _SCOPES = [u'https://www.googleapis.com/auth/cloud-platform', u'https://www.googleapis.com/auth/compute', u'https://www.googleapis.com/auth/compute.readonly', u'https://www.googleapis.com/auth/userinfo.email']
  _VERSION = u'v1b3'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _CLIENT_CLASS_NAME = u'DataflowV1b3'
  _URL_VERSION = u'v1b3'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None):
    """Create a new dataflow handle."""
    url = url or self.BASE_URL
    super(DataflowV1b3, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers)
    self.projects_jobs_debug = self.ProjectsJobsDebugService(self)
    self.projects_jobs_messages = self.ProjectsJobsMessagesService(self)
    self.projects_jobs_workItems = self.ProjectsJobsWorkItemsService(self)
    self.projects_jobs = self.ProjectsJobsService(self)
    self.projects_locations_jobs_debug = self.ProjectsLocationsJobsDebugService(self)
    self.projects_locations_jobs_messages = self.ProjectsLocationsJobsMessagesService(self)
    self.projects_locations_jobs_workItems = self.ProjectsLocationsJobsWorkItemsService(self)
    self.projects_locations_jobs = self.ProjectsLocationsJobsService(self)
    self.projects_locations_templates = self.ProjectsLocationsTemplatesService(self)
    self.projects_locations = self.ProjectsLocationsService(self)
    self.projects_templates = self.ProjectsTemplatesService(self)
    self.projects = self.ProjectsService(self)

  class ProjectsJobsDebugService(base_api.BaseApiService):
    """Service class for the projects_jobs_debug resource."""

    _NAME = u'projects_jobs_debug'

    def __init__(self, client):
      super(DataflowV1b3.ProjectsJobsDebugService, self).__init__(client)
      self._upload_configs = {
          }

    def GetConfig(self, request, global_params=None):
      """Get encoded debug configuration for component. Not cacheable.

      Args:
        request: (DataflowProjectsJobsDebugGetConfigRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GetDebugConfigResponse) The response message.
      """
      config = self.GetMethodConfig('GetConfig')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetConfig.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'dataflow.projects.jobs.debug.getConfig',
        ordered_params=[u'projectId', u'jobId'],
        path_params=[u'jobId', u'projectId'],
        query_params=[],
        relative_path=u'v1b3/projects/{projectId}/jobs/{jobId}/debug/getConfig',
        request_field=u'getDebugConfigRequest',
        request_type_name=u'DataflowProjectsJobsDebugGetConfigRequest',
        response_type_name=u'GetDebugConfigResponse',
        supports_download=False,
    )

    def SendCapture(self, request, global_params=None):
      """Send encoded debug capture data for component.

      Args:
        request: (DataflowProjectsJobsDebugSendCaptureRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (SendDebugCaptureResponse) The response message.
      """
      config = self.GetMethodConfig('SendCapture')
      return self._RunMethod(
          config, request, global_params=global_params)

    SendCapture.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'dataflow.projects.jobs.debug.sendCapture',
        ordered_params=[u'projectId', u'jobId'],
        path_params=[u'jobId', u'projectId'],
        query_params=[],
        relative_path=u'v1b3/projects/{projectId}/jobs/{jobId}/debug/sendCapture',
        request_field=u'sendDebugCaptureRequest',
        request_type_name=u'DataflowProjectsJobsDebugSendCaptureRequest',
        response_type_name=u'SendDebugCaptureResponse',
        supports_download=False,
    )

  class ProjectsJobsMessagesService(base_api.BaseApiService):
    """Service class for the projects_jobs_messages resource."""

    _NAME = u'projects_jobs_messages'

    def __init__(self, client):
      super(DataflowV1b3.ProjectsJobsMessagesService, self).__init__(client)
      self._upload_configs = {
          }

    def List(self, request, global_params=None):
      """Request the job status.

      Args:
        request: (DataflowProjectsJobsMessagesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListJobMessagesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'dataflow.projects.jobs.messages.list',
        ordered_params=[u'projectId', u'jobId'],
        path_params=[u'jobId', u'projectId'],
        query_params=[u'endTime', u'location', u'minimumImportance', u'pageSize', u'pageToken', u'startTime'],
        relative_path=u'v1b3/projects/{projectId}/jobs/{jobId}/messages',
        request_field='',
        request_type_name=u'DataflowProjectsJobsMessagesListRequest',
        response_type_name=u'ListJobMessagesResponse',
        supports_download=False,
    )

  class ProjectsJobsWorkItemsService(base_api.BaseApiService):
    """Service class for the projects_jobs_workItems resource."""

    _NAME = u'projects_jobs_workItems'

    def __init__(self, client):
      super(DataflowV1b3.ProjectsJobsWorkItemsService, self).__init__(client)
      self._upload_configs = {
          }

    def Lease(self, request, global_params=None):
      """Leases a dataflow WorkItem to run.

      Args:
        request: (DataflowProjectsJobsWorkItemsLeaseRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (LeaseWorkItemResponse) The response message.
      """
      config = self.GetMethodConfig('Lease')
      return self._RunMethod(
          config, request, global_params=global_params)

    Lease.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'dataflow.projects.jobs.workItems.lease',
        ordered_params=[u'projectId', u'jobId'],
        path_params=[u'jobId', u'projectId'],
        query_params=[],
        relative_path=u'v1b3/projects/{projectId}/jobs/{jobId}/workItems:lease',
        request_field=u'leaseWorkItemRequest',
        request_type_name=u'DataflowProjectsJobsWorkItemsLeaseRequest',
        response_type_name=u'LeaseWorkItemResponse',
        supports_download=False,
    )

    def ReportStatus(self, request, global_params=None):
      """Reports the status of dataflow WorkItems leased by a worker.

      Args:
        request: (DataflowProjectsJobsWorkItemsReportStatusRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ReportWorkItemStatusResponse) The response message.
      """
      config = self.GetMethodConfig('ReportStatus')
      return self._RunMethod(
          config, request, global_params=global_params)

    ReportStatus.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'dataflow.projects.jobs.workItems.reportStatus',
        ordered_params=[u'projectId', u'jobId'],
        path_params=[u'jobId', u'projectId'],
        query_params=[],
        relative_path=u'v1b3/projects/{projectId}/jobs/{jobId}/workItems:reportStatus',
        request_field=u'reportWorkItemStatusRequest',
        request_type_name=u'DataflowProjectsJobsWorkItemsReportStatusRequest',
        response_type_name=u'ReportWorkItemStatusResponse',
        supports_download=False,
    )

  class ProjectsJobsService(base_api.BaseApiService):
    """Service class for the projects_jobs resource."""

    _NAME = u'projects_jobs'

    def __init__(self, client):
      super(DataflowV1b3.ProjectsJobsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      """Creates a Cloud Dataflow job.

      Args:
        request: (DataflowProjectsJobsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Job) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'dataflow.projects.jobs.create',
        ordered_params=[u'projectId'],
        path_params=[u'projectId'],
        query_params=[u'location', u'replaceJobId', u'view'],
        relative_path=u'v1b3/projects/{projectId}/jobs',
        request_field=u'job',
        request_type_name=u'DataflowProjectsJobsCreateRequest',
        response_type_name=u'Job',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      """Gets the state of the specified Cloud Dataflow job.

      Args:
        request: (DataflowProjectsJobsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Job) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'dataflow.projects.jobs.get',
        ordered_params=[u'projectId', u'jobId'],
        path_params=[u'jobId', u'projectId'],
        query_params=[u'location', u'view'],
        relative_path=u'v1b3/projects/{projectId}/jobs/{jobId}',
        request_field='',
        request_type_name=u'DataflowProjectsJobsGetRequest',
        response_type_name=u'Job',
        supports_download=False,
    )

    def GetMetrics(self, request, global_params=None):
      """Request the job status.

      Args:
        request: (DataflowProjectsJobsGetMetricsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (JobMetrics) The response message.
      """
      config = self.GetMethodConfig('GetMetrics')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetMetrics.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'dataflow.projects.jobs.getMetrics',
        ordered_params=[u'projectId', u'jobId'],
        path_params=[u'jobId', u'projectId'],
        query_params=[u'location', u'startTime'],
        relative_path=u'v1b3/projects/{projectId}/jobs/{jobId}/metrics',
        request_field='',
        request_type_name=u'DataflowProjectsJobsGetMetricsRequest',
        response_type_name=u'JobMetrics',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      """List the jobs of a project.

      Args:
        request: (DataflowProjectsJobsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListJobsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'dataflow.projects.jobs.list',
        ordered_params=[u'projectId'],
        path_params=[u'projectId'],
        query_params=[u'filter', u'location', u'pageSize', u'pageToken', u'view'],
        relative_path=u'v1b3/projects/{projectId}/jobs',
        request_field='',
        request_type_name=u'DataflowProjectsJobsListRequest',
        response_type_name=u'ListJobsResponse',
        supports_download=False,
    )

    def Update(self, request, global_params=None):
      """Updates the state of an existing Cloud Dataflow job.

      Args:
        request: (DataflowProjectsJobsUpdateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Job) The response message.
      """
      config = self.GetMethodConfig('Update')
      return self._RunMethod(
          config, request, global_params=global_params)

    Update.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'PUT',
        method_id=u'dataflow.projects.jobs.update',
        ordered_params=[u'projectId', u'jobId'],
        path_params=[u'jobId', u'projectId'],
        query_params=[u'location'],
        relative_path=u'v1b3/projects/{projectId}/jobs/{jobId}',
        request_field=u'job',
        request_type_name=u'DataflowProjectsJobsUpdateRequest',
        response_type_name=u'Job',
        supports_download=False,
    )

  class ProjectsLocationsJobsDebugService(base_api.BaseApiService):
    """Service class for the projects_locations_jobs_debug resource."""

    _NAME = u'projects_locations_jobs_debug'

    def __init__(self, client):
      super(DataflowV1b3.ProjectsLocationsJobsDebugService, self).__init__(client)
      self._upload_configs = {
          }

    def GetConfig(self, request, global_params=None):
      """Get encoded debug configuration for component. Not cacheable.

      Args:
        request: (DataflowProjectsLocationsJobsDebugGetConfigRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GetDebugConfigResponse) The response message.
      """
      config = self.GetMethodConfig('GetConfig')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetConfig.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'dataflow.projects.locations.jobs.debug.getConfig',
        ordered_params=[u'projectId', u'location', u'jobId'],
        path_params=[u'jobId', u'location', u'projectId'],
        query_params=[],
        relative_path=u'v1b3/projects/{projectId}/locations/{location}/jobs/{jobId}/debug/getConfig',
        request_field=u'getDebugConfigRequest',
        request_type_name=u'DataflowProjectsLocationsJobsDebugGetConfigRequest',
        response_type_name=u'GetDebugConfigResponse',
        supports_download=False,
    )

    def SendCapture(self, request, global_params=None):
      """Send encoded debug capture data for component.

      Args:
        request: (DataflowProjectsLocationsJobsDebugSendCaptureRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (SendDebugCaptureResponse) The response message.
      """
      config = self.GetMethodConfig('SendCapture')
      return self._RunMethod(
          config, request, global_params=global_params)

    SendCapture.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'dataflow.projects.locations.jobs.debug.sendCapture',
        ordered_params=[u'projectId', u'location', u'jobId'],
        path_params=[u'jobId', u'location', u'projectId'],
        query_params=[],
        relative_path=u'v1b3/projects/{projectId}/locations/{location}/jobs/{jobId}/debug/sendCapture',
        request_field=u'sendDebugCaptureRequest',
        request_type_name=u'DataflowProjectsLocationsJobsDebugSendCaptureRequest',
        response_type_name=u'SendDebugCaptureResponse',
        supports_download=False,
    )

  class ProjectsLocationsJobsMessagesService(base_api.BaseApiService):
    """Service class for the projects_locations_jobs_messages resource."""

    _NAME = u'projects_locations_jobs_messages'

    def __init__(self, client):
      super(DataflowV1b3.ProjectsLocationsJobsMessagesService, self).__init__(client)
      self._upload_configs = {
          }

    def List(self, request, global_params=None):
      """Request the job status.

      Args:
        request: (DataflowProjectsLocationsJobsMessagesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListJobMessagesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'dataflow.projects.locations.jobs.messages.list',
        ordered_params=[u'projectId', u'location', u'jobId'],
        path_params=[u'jobId', u'location', u'projectId'],
        query_params=[u'endTime', u'minimumImportance', u'pageSize', u'pageToken', u'startTime'],
        relative_path=u'v1b3/projects/{projectId}/locations/{location}/jobs/{jobId}/messages',
        request_field='',
        request_type_name=u'DataflowProjectsLocationsJobsMessagesListRequest',
        response_type_name=u'ListJobMessagesResponse',
        supports_download=False,
    )

  class ProjectsLocationsJobsWorkItemsService(base_api.BaseApiService):
    """Service class for the projects_locations_jobs_workItems resource."""

    _NAME = u'projects_locations_jobs_workItems'

    def __init__(self, client):
      super(DataflowV1b3.ProjectsLocationsJobsWorkItemsService, self).__init__(client)
      self._upload_configs = {
          }

    def Lease(self, request, global_params=None):
      """Leases a dataflow WorkItem to run.

      Args:
        request: (DataflowProjectsLocationsJobsWorkItemsLeaseRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (LeaseWorkItemResponse) The response message.
      """
      config = self.GetMethodConfig('Lease')
      return self._RunMethod(
          config, request, global_params=global_params)

    Lease.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'dataflow.projects.locations.jobs.workItems.lease',
        ordered_params=[u'projectId', u'location', u'jobId'],
        path_params=[u'jobId', u'location', u'projectId'],
        query_params=[],
        relative_path=u'v1b3/projects/{projectId}/locations/{location}/jobs/{jobId}/workItems:lease',
        request_field=u'leaseWorkItemRequest',
        request_type_name=u'DataflowProjectsLocationsJobsWorkItemsLeaseRequest',
        response_type_name=u'LeaseWorkItemResponse',
        supports_download=False,
    )

    def ReportStatus(self, request, global_params=None):
      """Reports the status of dataflow WorkItems leased by a worker.

      Args:
        request: (DataflowProjectsLocationsJobsWorkItemsReportStatusRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ReportWorkItemStatusResponse) The response message.
      """
      config = self.GetMethodConfig('ReportStatus')
      return self._RunMethod(
          config, request, global_params=global_params)

    ReportStatus.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'dataflow.projects.locations.jobs.workItems.reportStatus',
        ordered_params=[u'projectId', u'location', u'jobId'],
        path_params=[u'jobId', u'location', u'projectId'],
        query_params=[],
        relative_path=u'v1b3/projects/{projectId}/locations/{location}/jobs/{jobId}/workItems:reportStatus',
        request_field=u'reportWorkItemStatusRequest',
        request_type_name=u'DataflowProjectsLocationsJobsWorkItemsReportStatusRequest',
        response_type_name=u'ReportWorkItemStatusResponse',
        supports_download=False,
    )

  class ProjectsLocationsJobsService(base_api.BaseApiService):
    """Service class for the projects_locations_jobs resource."""

    _NAME = u'projects_locations_jobs'

    def __init__(self, client):
      super(DataflowV1b3.ProjectsLocationsJobsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      """Creates a Cloud Dataflow job.

      Args:
        request: (DataflowProjectsLocationsJobsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Job) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'dataflow.projects.locations.jobs.create',
        ordered_params=[u'projectId', u'location'],
        path_params=[u'location', u'projectId'],
        query_params=[u'replaceJobId', u'view'],
        relative_path=u'v1b3/projects/{projectId}/locations/{location}/jobs',
        request_field=u'job',
        request_type_name=u'DataflowProjectsLocationsJobsCreateRequest',
        response_type_name=u'Job',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      """Gets the state of the specified Cloud Dataflow job.

      Args:
        request: (DataflowProjectsLocationsJobsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Job) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'dataflow.projects.locations.jobs.get',
        ordered_params=[u'projectId', u'location', u'jobId'],
        path_params=[u'jobId', u'location', u'projectId'],
        query_params=[u'view'],
        relative_path=u'v1b3/projects/{projectId}/locations/{location}/jobs/{jobId}',
        request_field='',
        request_type_name=u'DataflowProjectsLocationsJobsGetRequest',
        response_type_name=u'Job',
        supports_download=False,
    )

    def GetMetrics(self, request, global_params=None):
      """Request the job status.

      Args:
        request: (DataflowProjectsLocationsJobsGetMetricsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (JobMetrics) The response message.
      """
      config = self.GetMethodConfig('GetMetrics')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetMetrics.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'dataflow.projects.locations.jobs.getMetrics',
        ordered_params=[u'projectId', u'location', u'jobId'],
        path_params=[u'jobId', u'location', u'projectId'],
        query_params=[u'startTime'],
        relative_path=u'v1b3/projects/{projectId}/locations/{location}/jobs/{jobId}/metrics',
        request_field='',
        request_type_name=u'DataflowProjectsLocationsJobsGetMetricsRequest',
        response_type_name=u'JobMetrics',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      """List the jobs of a project.

      Args:
        request: (DataflowProjectsLocationsJobsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListJobsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'dataflow.projects.locations.jobs.list',
        ordered_params=[u'projectId', u'location'],
        path_params=[u'location', u'projectId'],
        query_params=[u'filter', u'pageSize', u'pageToken', u'view'],
        relative_path=u'v1b3/projects/{projectId}/locations/{location}/jobs',
        request_field='',
        request_type_name=u'DataflowProjectsLocationsJobsListRequest',
        response_type_name=u'ListJobsResponse',
        supports_download=False,
    )

    def Update(self, request, global_params=None):
      """Updates the state of an existing Cloud Dataflow job.

      Args:
        request: (DataflowProjectsLocationsJobsUpdateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Job) The response message.
      """
      config = self.GetMethodConfig('Update')
      return self._RunMethod(
          config, request, global_params=global_params)

    Update.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'PUT',
        method_id=u'dataflow.projects.locations.jobs.update',
        ordered_params=[u'projectId', u'location', u'jobId'],
        path_params=[u'jobId', u'location', u'projectId'],
        query_params=[],
        relative_path=u'v1b3/projects/{projectId}/locations/{location}/jobs/{jobId}',
        request_field=u'job',
        request_type_name=u'DataflowProjectsLocationsJobsUpdateRequest',
        response_type_name=u'Job',
        supports_download=False,
    )

  class ProjectsLocationsTemplatesService(base_api.BaseApiService):
    """Service class for the projects_locations_templates resource."""

    _NAME = u'projects_locations_templates'

    def __init__(self, client):
      super(DataflowV1b3.ProjectsLocationsTemplatesService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      """Creates a Cloud Dataflow job from a template.

      Args:
        request: (DataflowProjectsLocationsTemplatesCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Job) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'dataflow.projects.locations.templates.create',
        ordered_params=[u'projectId', u'location'],
        path_params=[u'location', u'projectId'],
        query_params=[],
        relative_path=u'v1b3/projects/{projectId}/locations/{location}/templates',
        request_field=u'createJobFromTemplateRequest',
        request_type_name=u'DataflowProjectsLocationsTemplatesCreateRequest',
        response_type_name=u'Job',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      """Get the template associated with a template.

      Args:
        request: (DataflowProjectsLocationsTemplatesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GetTemplateResponse) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'dataflow.projects.locations.templates.get',
        ordered_params=[u'projectId', u'location'],
        path_params=[u'location', u'projectId'],
        query_params=[u'gcsPath', u'view'],
        relative_path=u'v1b3/projects/{projectId}/locations/{location}/templates:get',
        request_field='',
        request_type_name=u'DataflowProjectsLocationsTemplatesGetRequest',
        response_type_name=u'GetTemplateResponse',
        supports_download=False,
    )

    def Launch(self, request, global_params=None):
      """Launch a template.

      Args:
        request: (DataflowProjectsLocationsTemplatesLaunchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (LaunchTemplateResponse) The response message.
      """
      config = self.GetMethodConfig('Launch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Launch.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'dataflow.projects.locations.templates.launch',
        ordered_params=[u'projectId', u'location'],
        path_params=[u'location', u'projectId'],
        query_params=[u'gcsPath', u'validateOnly'],
        relative_path=u'v1b3/projects/{projectId}/locations/{location}/templates:launch',
        request_field=u'launchTemplateParameters',
        request_type_name=u'DataflowProjectsLocationsTemplatesLaunchRequest',
        response_type_name=u'LaunchTemplateResponse',
        supports_download=False,
    )

  class ProjectsLocationsService(base_api.BaseApiService):
    """Service class for the projects_locations resource."""

    _NAME = u'projects_locations'

    def __init__(self, client):
      super(DataflowV1b3.ProjectsLocationsService, self).__init__(client)
      self._upload_configs = {
          }

    def WorkerMessages(self, request, global_params=None):
      """Send a worker_message to the service.

      Args:
        request: (DataflowProjectsLocationsWorkerMessagesRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (SendWorkerMessagesResponse) The response message.
      """
      config = self.GetMethodConfig('WorkerMessages')
      return self._RunMethod(
          config, request, global_params=global_params)

    WorkerMessages.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'dataflow.projects.locations.workerMessages',
        ordered_params=[u'projectId', u'location'],
        path_params=[u'location', u'projectId'],
        query_params=[],
        relative_path=u'v1b3/projects/{projectId}/locations/{location}/WorkerMessages',
        request_field=u'sendWorkerMessagesRequest',
        request_type_name=u'DataflowProjectsLocationsWorkerMessagesRequest',
        response_type_name=u'SendWorkerMessagesResponse',
        supports_download=False,
    )

  class ProjectsTemplatesService(base_api.BaseApiService):
    """Service class for the projects_templates resource."""

    _NAME = u'projects_templates'

    def __init__(self, client):
      super(DataflowV1b3.ProjectsTemplatesService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      """Creates a Cloud Dataflow job from a template.

      Args:
        request: (DataflowProjectsTemplatesCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Job) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'dataflow.projects.templates.create',
        ordered_params=[u'projectId'],
        path_params=[u'projectId'],
        query_params=[],
        relative_path=u'v1b3/projects/{projectId}/templates',
        request_field=u'createJobFromTemplateRequest',
        request_type_name=u'DataflowProjectsTemplatesCreateRequest',
        response_type_name=u'Job',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      """Get the template associated with a template.

      Args:
        request: (DataflowProjectsTemplatesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GetTemplateResponse) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'dataflow.projects.templates.get',
        ordered_params=[u'projectId'],
        path_params=[u'projectId'],
        query_params=[u'gcsPath', u'location', u'view'],
        relative_path=u'v1b3/projects/{projectId}/templates:get',
        request_field='',
        request_type_name=u'DataflowProjectsTemplatesGetRequest',
        response_type_name=u'GetTemplateResponse',
        supports_download=False,
    )

    def Launch(self, request, global_params=None):
      """Launch a template.

      Args:
        request: (DataflowProjectsTemplatesLaunchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (LaunchTemplateResponse) The response message.
      """
      config = self.GetMethodConfig('Launch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Launch.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'dataflow.projects.templates.launch',
        ordered_params=[u'projectId'],
        path_params=[u'projectId'],
        query_params=[u'gcsPath', u'location', u'validateOnly'],
        relative_path=u'v1b3/projects/{projectId}/templates:launch',
        request_field=u'launchTemplateParameters',
        request_type_name=u'DataflowProjectsTemplatesLaunchRequest',
        response_type_name=u'LaunchTemplateResponse',
        supports_download=False,
    )

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = u'projects'

    def __init__(self, client):
      super(DataflowV1b3.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }

    def WorkerMessages(self, request, global_params=None):
      """Send a worker_message to the service.

      Args:
        request: (DataflowProjectsWorkerMessagesRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (SendWorkerMessagesResponse) The response message.
      """
      config = self.GetMethodConfig('WorkerMessages')
      return self._RunMethod(
          config, request, global_params=global_params)

    WorkerMessages.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'dataflow.projects.workerMessages',
        ordered_params=[u'projectId'],
        path_params=[u'projectId'],
        query_params=[],
        relative_path=u'v1b3/projects/{projectId}/WorkerMessages',
        request_field=u'sendWorkerMessagesRequest',
        request_type_name=u'DataflowProjectsWorkerMessagesRequest',
        response_type_name=u'SendWorkerMessagesResponse',
        supports_download=False,
    )
