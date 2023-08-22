# SPDX-License-Identifier: Apache-2.0
# Copyright (C) 2023 OKTET Labs Ltd. All rights reserved.
#
# Per-project specific settings.
# Full description is available in Bublik sources: doc/wiki/per_project.md.

# Identifies project matching PROJECT meta in metadata.json.
#
PROJECT = 'ts-factory'

# List of emails to notify about importruns failures.
#
EMAIL_PROJECT_WATCHERS = ['arybchik@ts-factory.io']

# Default UI version.
#
UI_VERSION = 2

# Configures dashboard through defining columns.
# Keys are common to all dashboard settings, values - meta category names.
#
DASHBOARD_HEADER = {
    'ts_name'           : 'Test Suite',
    'configuration'     : 'Configuration',
    'status'            : 'Status',
    'total'             : 'Total',
    'unexpected'        : 'NOK',
    'progress'          : 'Executed',
    'notes'             : 'Notes'
}

# Sets link available by click on column values.
# Key defines column matching DASHBOARD_HEADER to apply action from value.
#
DASHBOARD_PAYLOAD = {
    'configuration'     : 'go_run',
    'total'             : 'go_tree',
    'unexpected'        : 'go_run_failed',
    'notes'             : 'go_bug',
}

# Points to dashboard date column where to show that run.
# Value represents meta name in meta_data.json.
#
DASHBOARD_DATE = 'CAMPAIGN_DATE'

# Default sorting order.
# Values represent DASHBOARD_HEADER keys, except 'start' which defines run start.
#
DASHBOARD_RUNS_SORT = ['start']

# Sets deafult mode for open dashboard. Works only for UI-V2.
# Values available: 'one_day_one_column', 'one_day_two_columns', 'two_days_two_columns'.
#
DASHBOARD_DEFAULT_MODE = 'two_days_two_columns'

# Defines extra data to show in Info block on run and log pages.
# Value represent meta category name.
#
SPECIAL_CATEGORIES = ['Configuration']

# Defines data to show in Metadata column on runs and history tables.
# Value represent meta category name.
#
METADATA_ON_PAGES = ['Test Suite', 'Configuration']

# Defines run status.
# Value represents meta name in meta_data.json.
#
RUN_STATUS_META = 'RUN_STATUS'

# Sets borders for defining run status by rate of unexpected results.
# Value represent 2 float numbers: left and right borders respectively.
#
RUN_STATUS_BY_NOK_BORDERS = (20.0, 80.0)

# Indicates that run testing was completed.
# Value represents file available via run source link.
#
RUN_COMPLETE_FILE = '.done'

# Allows Bublik to distinguish one run from another.
# Value represents meta name in meta_data.json.
#
RUN_KEY_METAS = ['START_TIMESTAMP', 'CFG']

# Domens which Bublik server trusts accepting requests coming from.
# More details: https://docs.djangoproject.com/en/3.0/ref/settings/#csrf-trusted-origins
#
CSRF_TRUSTED_ORIGINS = ['ts-factory.io']
