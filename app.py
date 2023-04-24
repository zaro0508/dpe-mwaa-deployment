#
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
#

#!/usr/bin/env python3
import os
from aws_cdk import core
from mwaairflow.mwaairflow_stack import MWAAirflowStack
import helpers

app = core.App(context=helpers.get_deployment_context())
  
MWAAirflowStack(
    app,
    "MWAAirflowStack"
)

app.synth()
