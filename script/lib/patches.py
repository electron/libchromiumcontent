import os
import sys

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.join(PROJECT_ROOT, 'vendor', 'pyyaml', 'lib'))
import yaml

from git import apply as git_apply


class Patch:
  def __init__(self, file_path, repo_path):
    self.file_path = file_path
    self.repo_path = repo_path

  def apply(self, reverse=False):
    return git_apply(self.repo_path, self.file_path, reverse=reverse)

  def reverse(self):
    return self.apply(reverse=True)

  def get_file_path(self):
    return self.file_path


class PatchesList:
  def __init__(self, patches):
    self.patches = patches

  def __len__(self):
    return len(self.patches)

  def apply(self, reverse=False, stop_on_error=True):
    all_patches_applied = True
    failed_patches = []

    for patch in self.patches:
      applied_successfully = patch.apply(reverse=reverse)

      if not applied_successfully:
        all_patches_applied = False
        failed_patches.append(patch)

      should_stop_now = not applied_successfully and stop_on_error
      if should_stop_now:
        break

    return (all_patches_applied, failed_patches)

  def reverse(self, stop_on_error=True):
    return self.apply(reverse=True, stop_on_error=stop_on_error)


class PatchesConfig:
  @staticmethod
  def from_directory(dir_path, config_name='.patches.yaml'):
    config_path = os.path.join(dir_path, config_name)
    return PatchesConfig(config_path)

  def __init__(self, config_path):
    self.path = config_path

  def __parse(self):
    contents = None

    if os.path.isfile(self.path):
      with open(self.path, 'r') as stream:
        try:
          contents = yaml.load(stream)
        except yaml.YAMLError as e:
          print(e)

    return contents

  def __create_patch(self, raw_data, base_directory, repo_path):
    relative_file_path = raw_data['file']
    absolute_file_path = os.path.join(base_directory, relative_file_path)

    return Patch(absolute_file_path, repo_path)

  def get_patches_list(self):
    config_contents = self.__parse()
    if config_contents is None:
      return None

    repo_path = config_contents['repo']
    if sys.platform == 'win32':
      repo_path = repo_path.replace('/', '\\')

    patches_data = config_contents['patches']
    base_directory = os.path.dirname(self.path)

    patches = [self.__create_patch(data, base_directory, repo_path) for data in patches_data]
    patches_list = PatchesList(patches)

    return patches_list
