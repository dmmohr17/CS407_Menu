import pygame

def checkCollision(projectile, players):
    for player in players:
        if projectile.rect.colliderect(player.rect) and projectile not in player.projectiles:
            if projectile.hasHit == False:
                player.health -= projectile.damage
                projectile.hasHit = True
            return True
    return False