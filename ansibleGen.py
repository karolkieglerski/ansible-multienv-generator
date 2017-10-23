#!/usr/bin/python
import os
from shutil import copyfile


class ProjectGenerator:
    project = 'application'
    conf = 'ansible.cfg'
    env_000 = '000_cross_env_vars.yml'
    tasks_file = ['tasks_pre.yml', 'tasks_post.yml']
    project_conf = ''
    tmp_conf = ''
    role_dir = ['defaults', 'files', 'tasks', 'templates']
    group_dir = []
    roles = []
    envs = []
    tasks = True

    def __init__(self):
        self.project = raw_input("Enter project name: ")

        self.tasks = self.str_to_bool(raw_input("Generate tasks directory? (yes/no): "))

        print "Enter role's names separated by coma: "
        self.roles = raw_input().split(',')

        print "Enter environments names separated by coma: "
        self.envs = raw_input().split(',')

        print "Enter group vars separated by coma: "
        self.group_dir = raw_input().split(',')
        self.group_dir.append('all')

        self.project_conf = self.split_path([self.project, self.conf])
        self.tmp_conf = self.split_path(['tmp', self.conf])

        self.generate_project()

    def str_to_bool(self, s):
        if s == 'yes':
            return True
        elif s == 'no':
            return False
        else:
            raise ValueError

    def split_path(self, paths_array):
        return os.path.join(*paths_array)

    def create_paths(self, paths_array):
        path = os.path.join(*paths_array)

        try:
            os.makedirs(path)
        except OSError:
            if not os.path.isdir(path):
                raise
        return path

    def generate_project(self):

        env_file_000 = self.split_path([self.project, 'environments', self.env_000])

        self.create_paths([self.project, 'environments'])
        copyfile(self.tmp_conf, self.project_conf)
        open(self.split_path([self.project, 'playbook.yml']), 'a').close()
        open(env_file_000, 'a').close()

        if self.tasks:
            self.create_paths([self.project, 'tasks'])
            for file in self.tasks_file:
                open(self.split_path([self.project, 'tasks', file]), 'a').close()

        if self.roles:
            for role in self.roles:
                for rdir in self.role_dir:
                    self.create_paths([self.project, 'roles', role, rdir])

        if self.envs:
            for env in self.envs:
                for gdir in self.group_dir:
                    self.create_paths([self.project, 'environments', env, 'group_vars', gdir])
                    open(self.split_path([self.project, 'environments', env, 'group_vars', gdir, 'vars.yml']),
                         'a').close()
                os.symlink(env_file_000,
                           self.split_path([self.project, 'environments', env, 'group_vars/all', self.env_000]))
                open(self.split_path([self.project, 'environments', env, 'hosts']), 'a').close()


ans = ProjectGenerator()
