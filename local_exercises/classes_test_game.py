class Character:
    def __init__(self, name, hp, power):
        self.name = name
        self.hp = hp
        self.power = power

    def attack(self, enemy):
        # Calculate Damage
        damage = self.power
        # Modify the Enemy's State (The Interaction)
        enemy.hp -= damage

        print(f"⚔️ {self.name} hits {enemy.name} for {damage} damage!")
        print(f"   {enemy.name} has {enemy.hp} HP left.")

    def is_alive(self):
        return self.hp > 0


# The Game
hero = Character("The Architect", hp=100, power=25)
boss = Character("Bugzilla", hp=80, power=15)
# simulation
print("--- FIGHT START ---")
while hero.is_alive() and boss.is_alive():
    hero.attack(boss)

    if boss.is_alive():
        boss.attack(hero)
    else:
        print(f"🏆 {boss.name} defeated! {hero.name} wins!")

print("********* GAME OVER *********")
