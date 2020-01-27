#!/bin/bash
cd /scratch/beta/nabm/beta_pred_v3_rev1_2chan_cases_2_4_fix.runs/Case2c_no-dep_476
export PATH="/prog/roxar/tempest/tempest-8.1.3/simulation/scripts:$PATH"
export ROXAR_DIR=/prog/roxar/tempest/tempest-8.1.3
echo "RUN RUNNING \"\$submit command\"" Starting
/prog/roxar/tempest/tempest-8.1.3/simulation/runtime/python/python-3.6.1.ssl-lin64-rhel6/bin/python3 /prog/roxar/tempest/config/v8.1.3/configML/../scripts/tempest_lsf_submit.py --queue-name mr --num-cores 1 --job-name Case2c_no-dep_476 --log-file temp/lsf_Case2c_no-dep_476.log --single-node true --script "/scratch/beta/nabm/beta_pred_v3_rev1_2chan_cases_2_4_fix.runs/Case2c_no-dep_476/temp/job.sh > /scratch/beta/nabm/beta_pred_v3_rev1_2chan_cases_2_4_fix.runs/Case2c_no-dep_476/temp/job.log"
ffm_exit_status=$?
echo "RUN RUNNING \"\$submit command\"" exit code: $ffm_exit_status
if [ $ffm_exit_status -ne 0 ] ; then
   echo "RUN FAILED \"\$submit command\""
   exit 1
fi
echo "RUN COMPLETED \"\$submit command\""

