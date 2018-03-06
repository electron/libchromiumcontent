# import yaml  # TODO: Use for PatchesConfig.

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
  def __init__(self, path):
    raise

    self.path = path
    self.contents = None
    self.is_parsed = False

  def __parse(self):
    with open(self.path, 'r') as stream:
      try:
        self.contents = yaml.load(stream)
      except yaml.YAMLError as exc:
        print(exc)

    self.is_parsed = True

  def __parse_if_needed(self):
    if not self.is_parsed:
      self.__parse()

  def __create_patch(self, repo_path, raw_data):
    file_path = raw_data['file']
    return Patch(file_path, repo_path)

  def get_patches_list(self):
    self.__parse_if_needed()
    if self.contents is None:
      return None

    repo_path = self.contents['repo']  # TODO: Make it absolute.
    raw_patches_data = self.contents['patches']
    patches = [self.__create_patch(repo_path, data) for data in raw_patches_data]

    return patches
