from datetime import datetime
import pandas as pd
import json
# ====== HELIOS IMPORTS =========================================
# ------ Train/Test Function Imports ----------------------------
from helios_rl import STANDARD_RL
from helios_rl import HELIOS_OPTIMIZE
# ------ Config Import ------------------------------------------
# Meta parameters
from helios_rl.config import TestingSetupConfig
# Local parameters
from helios_rl.config_local import ConfigSetup
# ====== LOCAL IMPORTS ==========================================
# ------ Local Environment --------------------------------------
from environment.env import Environment
# ------ Visual Analysis -----------------------------------------------
from helios_rl import combined_variance_analysis_graph

def main():
    # ------ Load Configs -----------------------------------------
    # Meta parameters
    ExperimentConfig = TestingSetupConfig("./config.json").state_configs
    # Local Parameters
    ProblemConfig = ConfigSetup("./config_local.json").state_configs

    # ---
    # Server Specific:
    # - We do not run search methodology (assume we cannot interface directly)
    # - Search has been completed and we call the results of this to then train the agents to sub-goal/goals
    task = ProblemConfig['env_select']
    version = '2.5.3'
    save_dir = './output/'+str(task)+'_'+version
    
    data = open(save_dir+'/Reinforced_Instr_Experiment/instruction_predictions.json','r')
    instruction_results = json.loads(data.read())

    # ----

    # Take Instruction path now defined with reinforced+unsupervised sub-goal locations and train to these
    # Init experiment setup with sub-goal defined
    reinforced_experiment = HELIOS_OPTIMIZE(Config=ExperimentConfig, LocalConfig=ProblemConfig, 
                    Environment=Environment,
                    save_dir=save_dir+'/Reinforced_Instr_Experiment', show_figures = 'No', window_size=0.1,
                    instruction_path=None, predicted_path=instruction_results, instruction_episode_ratio=0.2,
                    instruction_chain=True, instruction_chain_how='continuous')
    reinforced_experiment.train()
    reinforced_experiment.test()
    
    # --------------------------------------------------------------------
    # Flat Baselines
    flat = STANDARD_RL(Config=ExperimentConfig, LocalConfig=ProblemConfig, 
                Environment=Environment,
                save_dir=save_dir, show_figures = 'No', window_size=0.1)
    flat.train()  
    flat.test()
    # --------------------------------------------------------------------
    # Combined results visual analysis
    flat_results = pd.read_csv(save_dir+'/Standard_Experiment'+'/testing_variance_results.csv')
    reinforced_results = pd.read_csv(save_dir+'/Reinforced_Instr_Experiment'+'/testing_variance_results.csv')

    variance_results = {}
    variance_results['Flat_agent'] = {}
    variance_results['Flat_agent']['results'] = flat_results
    variance_results['Flat_agent']['env_name'] = flat_results['agent'].iloc[0]
    variance_results['Flat_agent']['num_repeats'] = flat_results['num_repeats'].iloc[0]

    variance_results['Reinforced_instructions'] = {}
    variance_results['Reinforced_instructions']['results'] = reinforced_results
    variance_results['Reinforced_instructions']['env_name'] = reinforced_results['agent'].iloc[0]
    variance_results['Reinforced_instructions']['num_repeats'] = reinforced_results['num_repeats'].iloc[0]

    combined_variance_analysis_graph(variance_results, save_dir, show_figures='N')

if __name__=='__main__':
    main()