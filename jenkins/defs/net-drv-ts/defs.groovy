// SPDX-License-Identifier: Apache-2.0
// Copyright (C) 2023 OKTET Labs Ltd. All rights reserved.
//
// Site-specific variables for net-drv-ts test suite.

def set_defs(ctx) {
    ctx.TS_GIT_URL = 'https://github.com/ts-factory/net-drv-ts.git'
    ctx.TS_DEF_BRANCH = 'main'

    // Variables required for publish-logs
    ctx.PUBLISH_LOGS_NODE = 'ts-logs'
    ctx.TS_LOGS_SUBPATH = 'net-drv-ts/'

    // Variables required for bublik-import
    ctx.PROJECT = 'ts-factory'
    ctx.TS_BUBLIK_URL = 'https://ts-factory.io/bublik/'
    ctx.TS_LOGS_URL_PREFIX = 'https://ts-factory.io/logs/'

    // Log listener used by Bublik
    ctx.TS_LOG_LISTENER_NAME = 'ts_factory'
}

return this
