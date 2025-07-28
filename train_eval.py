import os, torch
from stable_baselines3.dqn.dqn import DQN
from sumo_rl import SumoEnvironment

def make_env(use_gui=None, out_csv_name=None):
    env = SumoEnvironment(
            #net_file="../../ITS_ML/map.net.xml",
            #route_file="../../ITS_ML/map.rou.xml",
            net_file="../../map.net.xml",
            route_file="../../map.rou.xml",
            out_csv_name=out_csv_name,
            reward_fn=["diff-waiting-time", "average-speed"],
            reward_weights=[1.0, 0.1], # La recompensa total sería (diff_waiting_time * 1.0) + (average_speed * 0.1)
            single_agent=True,
            use_gui=use_gui,
            num_seconds=3600
        )
    return env

train_env = make_env(use_gui=False, out_csv_name="its_dqn")
device = "cuda" if torch.cuda.is_available() else "cpu"
log_path = os.path.join('logs')
model = DQN(env=train_env,
        policy="MlpPolicy",
        learning_rate=3e-4,
        learning_starts=0,
        train_freq=1,
        target_update_interval=500,
        exploration_initial_eps=0.5,
        exploration_final_eps=0.01,
        verbose=1,
        tensorboard_log=log_path,
        device=device
        )

print("Iniciando entrenamiento...")
model.learn(total_timesteps=1000000, tb_log_name="its_dqn", progress_bar=True)
print("Entrenamiento finalizado.")

ppo_path = os.path.join('models', 'its_dqn')
model.save(ppo_path)
print("Modelo guardado")
train_env.close()

print("\nCargando y probando el modelo entrenado...")
loaded_model = DQN.load(ppo_path)
eval_env = make_env(use_gui=True, out_csv_name="model")

obs, info = eval_env.reset()
done = False
truncated = False
total_reward = 0
step_count = 0

while not done and not truncated:
    action, _ = loaded_model.predict(obs, deterministic=True)
    obs, reward, done, truncated, info = eval_env.step(action)
    total_reward += reward
    step_count += 1
    if step_count % 100 == 0:
        print(f"Paso: {step_count}, Recompensa actual: {reward:.2f}, Recompensa acumulada: {total_reward:.2f}")

print(f"\nSimulación de prueba finalizada. Pasos: {step_count}, Recompensa total: {total_reward:.2f}")
eval_env.close()
