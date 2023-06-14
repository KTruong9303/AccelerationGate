from os import walk
import pygame

def import_folder(path):
    '''
    a function that helps loading asset
    ...
    Parameter:
        path: path to the folder contain picture of asset
    --------
    Return:
        a list contain images that loaded and converted to alpha.
    '''
    surface_list = []

    for _, __, img_files in walk(path):
        for image in img_files:
            full_path = path +'/'+ image
            image_surf = pygame.image.load(full_path).convert_alpha()
            image_surf = pygame.transform.scale(image_surf,(48,48))
            surface_list.append(image_surf)

    return surface_list


def import_folder2(path):
    surface_list = []

    for _, __, img_files in walk(path):
        for image in img_files:
            full_path = path +'/'+ image
            image_surf = pygame.image.load(full_path).convert_alpha()
            image_surf = pygame.transform.scale(image_surf, (150, 150))
            surface_list.append(image_surf)

    return surface_list