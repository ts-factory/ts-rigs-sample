// SPDX-License-Identifier: Apache-2.0
// Copyright (C) 2023 OKTET Labs Ltd. All rights reserved.
//
// Set common variables for Jenkins pipelines.

def set_defs(ctx) {
    env.TE_WORKSPACE_DIR = '/srv/tmp'

    ctx.TE_GIT_URL = 'https://github.com/ts-factory/test-environment.git'
    ctx.TSCONF_GIT_URL = 'https://github.com/ts-factory/ts-conf.git'
}

return this
