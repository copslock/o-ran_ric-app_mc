#!/usr/bin/env bash
# vim: ts=4 sw=4 noet:
#----------------------------------------------------------------------------------
#
#	Copyright (c) 2018-2020 AT&T Intellectual Property.
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#	   http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
#---------------------------------------------------------------------------------


# ----------------------------------------------------------------------
# Mnemonic:	container_start.sh
# Abstract: For some "pod" environments a single container is required.
#			This starts all of the related processes which normally would
#			be started in individual containers.
#
#			There are two environment variables which affect the operation
#			of this script:
#				USE_NNG -- if set to !0 then the NNG version of the listener
#							is started; undefined or when 0 then the SI95
#							version is used.
#
#				GSLITE_ROOT -- Assumed to be the root directory for the 
#							core MC xAPP. If not defined, /mc/gs-lite is
#							assumed.
#
# Date:		13 February 2019
# Author:	E. Scott Daniels
# ----------------------------------------------------------------------

set -e

FIFO_DIR="/tmp/mcl/fifos"

SIMULATOR_MODE=`python /mc/extract_params.py ${XAPP_DESCRIPTOR_PATH}/config-file.json simulator_mode`
RMR_PORT=`python /mc/extract_rmr_port.py ${XAPP_DESCRIPTOR_PATH}/config-file.json rmr-data`

mkdir -p $FIFO_DIR

if [ "$SIMULATOR_MODE" != "true" ]
then
# --- start "sidecars" first. They are expected to need /playpen as the working dir

(
	cd /playpen
	if [ "$RMR_PORT" != "" ]
	then
		bin/mc_listener -p $RMR_PORT
	else
		bin/mc_listener
	fi
) >/tmp/listener.std 2>&1 &

echo "listener was started" >&2

fi


# ---- finally, start the core MC application -----------------------------
cd ${GSLITE_ROOT:-/mc/gs-lite}/demo/queries
./runall


