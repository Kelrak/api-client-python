This repository contains a client library for LaunchDarkly's REST API. This client was automatically
generated from our [OpenAPI specification](https://github.com/launchdarkly/ld-openapi).

This REST API is for custom integrations, data export, or automating your feature flag workflows. *DO NOT* use this client library to include feature flags in your web or mobile application. To integrate feature flags with your application, please see the [SDK documentation](https://docs.launchdarkly.com/v2.0/docs)

# launchdarkly-api
Build custom integrations with the LaunchDarkly REST API

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 2.0.22
- Package version: 2.0.22
- Build package: io.swagger.codegen.languages.PythonClientCodegen
For more information, please visit [https://support.launchdarkly.com](https://support.launchdarkly.com)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import launchdarkly_api 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import launchdarkly_api
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import launchdarkly_api
from launchdarkly_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
configuration = launchdarkly_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = launchdarkly_api.AuditLogApi(launchdarkly_api.ApiClient(configuration))
before = 789 # int | A timestamp filter, expressed as a Unix epoch time in milliseconds. All entries returned will have before this timestamp. (optional)
after = 789 # int | A timestamp filter, expressed as a Unix epoch time in milliseconds. All entries returned will have occured after this timestamp. (optional)
q = 'q_example' # str | Text to search for. You can search for the full or partial name of the resource involved or fullpartial email address of the member who made the change. (optional)
limit = 8.14 # float | A limit on the number of audit log entries to be returned, between 1 and 20. (optional)
spec = 'spec_example' # str | A resource specifier, allowing you to filter audit log listings by resource. (optional)

try:
    # Get a list of all audit log entries. The query parameters allow you to restrict the returned results by date ranges, resource specifiers, or a full-text search query.
    api_response = api_instance.get_audit_log_entries(before=before, after=after, q=q, limit=limit, spec=spec)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditLogApi->get_audit_log_entries: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://app.launchdarkly.com/api/v2*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuditLogApi* | [**get_audit_log_entries**](docs/AuditLogApi.md#get_audit_log_entries) | **GET** /auditlog | Get a list of all audit log entries. The query parameters allow you to restrict the returned results by date ranges, resource specifiers, or a full-text search query.
*AuditLogApi* | [**get_audit_log_entry**](docs/AuditLogApi.md#get_audit_log_entry) | **GET** /auditlog/{resourceId} | Use this endpoint to fetch a single audit log entry by its resouce ID.
*CustomRolesApi* | [**delete_custom_role**](docs/CustomRolesApi.md#delete_custom_role) | **DELETE** /roles/{customRoleKey} | Delete a custom role by key.
*CustomRolesApi* | [**get_custom_role**](docs/CustomRolesApi.md#get_custom_role) | **GET** /roles/{customRoleKey} | Get one custom role by key.
*CustomRolesApi* | [**get_custom_roles**](docs/CustomRolesApi.md#get_custom_roles) | **GET** /roles | Return a complete list of custom roles.
*CustomRolesApi* | [**patch_custom_role**](docs/CustomRolesApi.md#patch_custom_role) | **PATCH** /roles/{customRoleKey} | Modify a custom role by key.
*CustomRolesApi* | [**post_custom_role**](docs/CustomRolesApi.md#post_custom_role) | **POST** /roles | Create a new custom role.
*CustomerMetricsApi* | [**get_evaluations**](docs/CustomerMetricsApi.md#get_evaluations) | **GET** /usage/evaluations/{envId}/{flagKey} | Get events usage by event id and the feature flag key.
*CustomerMetricsApi* | [**get_event**](docs/CustomerMetricsApi.md#get_event) | **GET** /usage/events/{type} | Get events usage by event type.
*CustomerMetricsApi* | [**get_events**](docs/CustomerMetricsApi.md#get_events) | **GET** /usage/events | Get events usage endpoints.
*CustomerMetricsApi* | [**get_mau**](docs/CustomerMetricsApi.md#get_mau) | **GET** /usage/mau | Get monthly active user data.
*CustomerMetricsApi* | [**get_mau_by_category**](docs/CustomerMetricsApi.md#get_mau_by_category) | **GET** /usage/mau/bycategory | Get monthly active user data by category.
*CustomerMetricsApi* | [**get_stream**](docs/CustomerMetricsApi.md#get_stream) | **GET** /usage/streams/{source} | Get a stream endpoint and return timeseries data.
*CustomerMetricsApi* | [**get_stream_by_sdk**](docs/CustomerMetricsApi.md#get_stream_by_sdk) | **GET** /usage/streams/{source}/bysdkversion | Get a stream timeseries data by source show sdk version metadata.
*CustomerMetricsApi* | [**get_stream_sdk_version**](docs/CustomerMetricsApi.md#get_stream_sdk_version) | **GET** /usage/streams/{source}/sdkversions | Get a stream timeseries data by source and show all sdk version associated.
*CustomerMetricsApi* | [**get_streams**](docs/CustomerMetricsApi.md#get_streams) | **GET** /usage/streams | Returns a list of all streams.
*CustomerMetricsApi* | [**get_usage**](docs/CustomerMetricsApi.md#get_usage) | **GET** /usage | Returns of the usage endpoints available.
*DataExportDestinationsApi* | [**delete_destination**](docs/DataExportDestinationsApi.md#delete_destination) | **DELETE** /destinations/{projectKey}/{environmentKey}/{destinationId} | Get a single data export destination by ID
*DataExportDestinationsApi* | [**get_destination**](docs/DataExportDestinationsApi.md#get_destination) | **GET** /destinations/{projectKey}/{environmentKey}/{destinationId} | Get a single data export destination by ID
*DataExportDestinationsApi* | [**get_destinations**](docs/DataExportDestinationsApi.md#get_destinations) | **GET** /destinations | Returns a list of all data export destinations.
*DataExportDestinationsApi* | [**patch_destination**](docs/DataExportDestinationsApi.md#patch_destination) | **PATCH** /destinations/{projectKey}/{environmentKey}/{destinationId} | Perform a partial update to a data export destination.
*DataExportDestinationsApi* | [**post_destination**](docs/DataExportDestinationsApi.md#post_destination) | **POST** /destinations/{projectKey}/{environmentKey} | Create a new data export destination
*EnvironmentsApi* | [**delete_environment**](docs/EnvironmentsApi.md#delete_environment) | **DELETE** /projects/{projectKey}/environments/{environmentKey} | Delete an environment in a specific project.
*EnvironmentsApi* | [**get_environment**](docs/EnvironmentsApi.md#get_environment) | **GET** /projects/{projectKey}/environments/{environmentKey} | Get an environment given a project and key.
*EnvironmentsApi* | [**patch_environment**](docs/EnvironmentsApi.md#patch_environment) | **PATCH** /projects/{projectKey}/environments/{environmentKey} | Modify an environment by ID.
*EnvironmentsApi* | [**post_environment**](docs/EnvironmentsApi.md#post_environment) | **POST** /projects/{projectKey}/environments | Create a new environment in a specified project with a given name, key, and swatch color.
*FeatureFlagsApi* | [**copy_feature_flag**](docs/FeatureFlagsApi.md#copy_feature_flag) | **POST** /flags/{projectKey}/{featureFlagKey}/copy | Copies the feature flag configuration from one environment to the same feature flag in another environment.
*FeatureFlagsApi* | [**delete_feature_flag**](docs/FeatureFlagsApi.md#delete_feature_flag) | **DELETE** /flags/{projectKey}/{featureFlagKey} | Delete a feature flag in all environments. Be careful-- only delete feature flags that are no longer being used by your application.
*FeatureFlagsApi* | [**get_feature_flag**](docs/FeatureFlagsApi.md#get_feature_flag) | **GET** /flags/{projectKey}/{featureFlagKey} | Get a single feature flag by key.
*FeatureFlagsApi* | [**get_feature_flag_status**](docs/FeatureFlagsApi.md#get_feature_flag_status) | **GET** /flag-statuses/{projectKey}/{environmentKey}/{featureFlagKey} | Get the status for a particular feature flag.
*FeatureFlagsApi* | [**get_feature_flag_status_across_environments**](docs/FeatureFlagsApi.md#get_feature_flag_status_across_environments) | **GET** /flag-status/{projectKey}/{featureFlagKey} | Get the status for a particular feature flag across environments
*FeatureFlagsApi* | [**get_feature_flag_statuses**](docs/FeatureFlagsApi.md#get_feature_flag_statuses) | **GET** /flag-statuses/{projectKey}/{environmentKey} | Get a list of statuses for all feature flags. The status includes the last time the feature flag was requested, as well as the state of the flag.
*FeatureFlagsApi* | [**get_feature_flags**](docs/FeatureFlagsApi.md#get_feature_flags) | **GET** /flags/{projectKey} | Get a list of all features in the given project.
*FeatureFlagsApi* | [**patch_feature_flag**](docs/FeatureFlagsApi.md#patch_feature_flag) | **PATCH** /flags/{projectKey}/{featureFlagKey} | Perform a partial update to a feature.
*FeatureFlagsApi* | [**post_feature_flag**](docs/FeatureFlagsApi.md#post_feature_flag) | **POST** /flags/{projectKey} | Creates a new feature flag.
*ProjectsApi* | [**delete_project**](docs/ProjectsApi.md#delete_project) | **DELETE** /projects/{projectKey} | Delete a project by key. Caution-- deleting a project will delete all associated environments and feature flags. You cannot delete the last project in an account.
*ProjectsApi* | [**get_project**](docs/ProjectsApi.md#get_project) | **GET** /projects/{projectKey} | Fetch a single project by key.
*ProjectsApi* | [**get_projects**](docs/ProjectsApi.md#get_projects) | **GET** /projects | Returns a list of all projects in the account.
*ProjectsApi* | [**patch_project**](docs/ProjectsApi.md#patch_project) | **PATCH** /projects/{projectKey} | Modify a project by ID.
*ProjectsApi* | [**post_project**](docs/ProjectsApi.md#post_project) | **POST** /projects | Create a new project with the given key and name.
*RootApi* | [**get_root**](docs/RootApi.md#get_root) | **GET** / | 
*TeamMembersApi* | [**delete_member**](docs/TeamMembersApi.md#delete_member) | **DELETE** /members/{memberId} | Delete a team member by ID.
*TeamMembersApi* | [**get_member**](docs/TeamMembersApi.md#get_member) | **GET** /members/{memberId} | Get a single team member by ID.
*TeamMembersApi* | [**get_members**](docs/TeamMembersApi.md#get_members) | **GET** /members | Returns a list of all members in the account.
*TeamMembersApi* | [**patch_member**](docs/TeamMembersApi.md#patch_member) | **PATCH** /members/{memberId} | Modify a team member by ID.
*TeamMembersApi* | [**post_members**](docs/TeamMembersApi.md#post_members) | **POST** /members | Invite new members.
*UserSegmentsApi* | [**delete_user_segment**](docs/UserSegmentsApi.md#delete_user_segment) | **DELETE** /segments/{projectKey}/{environmentKey}/{userSegmentKey} | Delete a user segment.
*UserSegmentsApi* | [**get_user_segment**](docs/UserSegmentsApi.md#get_user_segment) | **GET** /segments/{projectKey}/{environmentKey}/{userSegmentKey} | Get a single user segment by key.
*UserSegmentsApi* | [**get_user_segments**](docs/UserSegmentsApi.md#get_user_segments) | **GET** /segments/{projectKey}/{environmentKey} | Get a list of all user segments in the given project.
*UserSegmentsApi* | [**patch_user_segment**](docs/UserSegmentsApi.md#patch_user_segment) | **PATCH** /segments/{projectKey}/{environmentKey}/{userSegmentKey} | Perform a partial update to a user segment.
*UserSegmentsApi* | [**post_user_segment**](docs/UserSegmentsApi.md#post_user_segment) | **POST** /segments/{projectKey}/{environmentKey} | Creates a new user segment.
*UserSettingsApi* | [**get_user_flag_setting**](docs/UserSettingsApi.md#get_user_flag_setting) | **GET** /users/{projectKey}/{environmentKey}/{userKey}/flags/{featureFlagKey} | Fetch a single flag setting for a user by key.
*UserSettingsApi* | [**get_user_flag_settings**](docs/UserSettingsApi.md#get_user_flag_settings) | **GET** /users/{projectKey}/{environmentKey}/{userKey}/flags | Fetch a single flag setting for a user by key.
*UserSettingsApi* | [**put_flag_setting**](docs/UserSettingsApi.md#put_flag_setting) | **PUT** /users/{projectKey}/{environmentKey}/{userKey}/flags/{featureFlagKey} | Specifically enable or disable a feature flag for a user based on their key.
*UsersApi* | [**delete_user**](docs/UsersApi.md#delete_user) | **DELETE** /users/{projectKey}/{environmentKey}/{userKey} | Delete a user by ID.
*UsersApi* | [**get_search_users**](docs/UsersApi.md#get_search_users) | **GET** /user-search/{projectKey}/{environmentKey} | Search users in LaunchDarkly based on their last active date, or a search query. It should not be used to enumerate all users in LaunchDarkly-- use the List users API resource.
*UsersApi* | [**get_user**](docs/UsersApi.md#get_user) | **GET** /users/{projectKey}/{environmentKey}/{userKey} | Get a user by key.
*UsersApi* | [**get_users**](docs/UsersApi.md#get_users) | **GET** /users/{projectKey}/{environmentKey} | List all users in the environment. Includes the total count of users. In each page, there will be up to &#39;limit&#39; users returned (default 20). This is useful for exporting all users in the system for further analysis. Paginated collections will include a next link containing a URL with the next set of elements in the collection.
*WebhooksApi* | [**delete_webhook**](docs/WebhooksApi.md#delete_webhook) | **DELETE** /webhooks/{resourceId} | Delete a webhook by ID.
*WebhooksApi* | [**get_webhook**](docs/WebhooksApi.md#get_webhook) | **GET** /webhooks/{resourceId} | Get a webhook by ID.
*WebhooksApi* | [**get_webhooks**](docs/WebhooksApi.md#get_webhooks) | **GET** /webhooks | Fetch a list of all webhooks.
*WebhooksApi* | [**patch_webhook**](docs/WebhooksApi.md#patch_webhook) | **PATCH** /webhooks/{resourceId} | Modify a webhook by ID.
*WebhooksApi* | [**post_webhook**](docs/WebhooksApi.md#post_webhook) | **POST** /webhooks | Create a webhook.


## Documentation For Models

 - [AuditLogEntries](docs/AuditLogEntries.md)
 - [AuditLogEntry](docs/AuditLogEntry.md)
 - [AuditLogEntryTarget](docs/AuditLogEntryTarget.md)
 - [Clause](docs/Clause.md)
 - [CopyActions](docs/CopyActions.md)
 - [CustomProperty](docs/CustomProperty.md)
 - [CustomPropertyValues](docs/CustomPropertyValues.md)
 - [CustomRole](docs/CustomRole.md)
 - [CustomRoleBody](docs/CustomRoleBody.md)
 - [CustomRoles](docs/CustomRoles.md)
 - [Destination](docs/Destination.md)
 - [DestinationAmazonKinesis](docs/DestinationAmazonKinesis.md)
 - [DestinationBody](docs/DestinationBody.md)
 - [DestinationGooglePubSub](docs/DestinationGooglePubSub.md)
 - [DestinationMParticle](docs/DestinationMParticle.md)
 - [DestinationSegment](docs/DestinationSegment.md)
 - [Destinations](docs/Destinations.md)
 - [Environment](docs/Environment.md)
 - [EnvironmentPost](docs/EnvironmentPost.md)
 - [EvaluationUsageError](docs/EvaluationUsageError.md)
 - [Events](docs/Events.md)
 - [Fallthrough](docs/Fallthrough.md)
 - [FeatureFlag](docs/FeatureFlag.md)
 - [FeatureFlagBody](docs/FeatureFlagBody.md)
 - [FeatureFlagConfig](docs/FeatureFlagConfig.md)
 - [FeatureFlagCopyBody](docs/FeatureFlagCopyBody.md)
 - [FeatureFlagCopyObject](docs/FeatureFlagCopyObject.md)
 - [FeatureFlagStatus](docs/FeatureFlagStatus.md)
 - [FeatureFlagStatusAcrossEnvironments](docs/FeatureFlagStatusAcrossEnvironments.md)
 - [FeatureFlagStatusForQueriedEnvironment](docs/FeatureFlagStatusForQueriedEnvironment.md)
 - [FeatureFlagStatuses](docs/FeatureFlagStatuses.md)
 - [FeatureFlags](docs/FeatureFlags.md)
 - [Id](docs/Id.md)
 - [Link](docs/Link.md)
 - [Links](docs/Links.md)
 - [MAU](docs/MAU.md)
 - [MAUMetadata](docs/MAUMetadata.md)
 - [MAUbyCategory](docs/MAUbyCategory.md)
 - [Member](docs/Member.md)
 - [Members](docs/Members.md)
 - [MembersBody](docs/MembersBody.md)
 - [PatchComment](docs/PatchComment.md)
 - [PatchOperation](docs/PatchOperation.md)
 - [Policy](docs/Policy.md)
 - [Prerequisite](docs/Prerequisite.md)
 - [Project](docs/Project.md)
 - [ProjectBody](docs/ProjectBody.md)
 - [Projects](docs/Projects.md)
 - [Role](docs/Role.md)
 - [Rollout](docs/Rollout.md)
 - [Rule](docs/Rule.md)
 - [Statement](docs/Statement.md)
 - [Statements](docs/Statements.md)
 - [Stream](docs/Stream.md)
 - [StreamBySDK](docs/StreamBySDK.md)
 - [StreamBySDKLinks](docs/StreamBySDKLinks.md)
 - [StreamBySDKLinksMetadata](docs/StreamBySDKLinksMetadata.md)
 - [StreamLinks](docs/StreamLinks.md)
 - [StreamSDKVersion](docs/StreamSDKVersion.md)
 - [StreamSDKVersionData](docs/StreamSDKVersionData.md)
 - [StreamUsageError](docs/StreamUsageError.md)
 - [StreamUsageLinks](docs/StreamUsageLinks.md)
 - [StreamUsageMetadata](docs/StreamUsageMetadata.md)
 - [StreamUsageSeries](docs/StreamUsageSeries.md)
 - [Streams](docs/Streams.md)
 - [Target](docs/Target.md)
 - [Usage](docs/Usage.md)
 - [UsageError](docs/UsageError.md)
 - [UsageLinks](docs/UsageLinks.md)
 - [User](docs/User.md)
 - [UserFlagSetting](docs/UserFlagSetting.md)
 - [UserFlagSettings](docs/UserFlagSettings.md)
 - [UserRecord](docs/UserRecord.md)
 - [UserSegment](docs/UserSegment.md)
 - [UserSegmentBody](docs/UserSegmentBody.md)
 - [UserSegmentRule](docs/UserSegmentRule.md)
 - [UserSegments](docs/UserSegments.md)
 - [UserSettingsBody](docs/UserSettingsBody.md)
 - [Users](docs/Users.md)
 - [Variation](docs/Variation.md)
 - [Webhook](docs/Webhook.md)
 - [WebhookBody](docs/WebhookBody.md)
 - [Webhooks](docs/Webhooks.md)
 - [WeightedVariation](docs/WeightedVariation.md)


## Documentation For Authorization


## Token

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author

support@launchdarkly.com

## Sample Code

```
from __future__ import print_function
import os
from pprint import pprint

import launchdarkly_api
import launchdarkly_api.models
from launchdarkly_api.rest import ApiException

configuration = launchdarkly_api.Configuration()
configuration.api_key['Authorization'] = os.getenv("LD_API_KEY")

client = launchdarkly_api.ApiClient(configuration)
api_instance = launchdarkly_api.FeatureFlagsApi(client)

project_key = "openapi"
flag_key = "test-python"

# Create a flag with json variations
feature_flag_body = launchdarkly_api.FeatureFlagBody(
    name=flag_key,
    key=flag_key,
    variations=[
        launchdarkly_api.models.Variation(value=[1, 2]),
        launchdarkly_api.models.Variation(value=[3, 4]),
        launchdarkly_api.models.Variation(value=[5])
    ])

try:
    api_response = api_instance.post_feature_flag(project_key, feature_flag_body)
    pprint(api_response)
except ApiException as e:
    print("Exception creating flag: %s\n" % e)

# Clean up the flag
try:
    api_response = api_instance.delete_feature_flag(project_key, flag_key)
    pprint(api_response)
except ApiException as e:
    print("Exception deleting flag: %s\n" % e)
```
