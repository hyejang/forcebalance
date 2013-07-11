import unittest
import sys, os, re
import forcebalance
import abc
import numpy
from __init__ import ForceBalanceTestCase, TestValues
from test_target import TargetTests # general targets tests defined in test_target.py

class TestAbInitio_GMX(ForceBalanceTestCase, TargetTests):
    def setUp(self):
        self.options=TestValues.opts.copy()
        self.options.update({
                'root': os.getcwd() + '/test/files',
                'penalty_additive': 0.01,
                'jobtype': 'NEWTON',
                'forcefield': ['water.itp']})
        os.chdir(self.options['root'])
        self.ff = forcebalance.forcefield.FF(self.options)
        self.ffname = self.options['forcefield'][0][:-3]
        self.filetype = self.options['forcefield'][0][-3:]

        self.tgt_opt=TestValues.tgt_opt.copy()
        self.tgt_opt.update({'type':'ABINITIO_GMX',
            'name':'cluster-02'})

        self.target = forcebalance.gmxio.AbInitio_GMX(self.options, self.tgt_opt, self.ff)
        self.addCleanup(os.system, 'rm -rf temp')

    def shortDescription(self):
        """@override ForceBalanceTestCase.shortDescription()"""
        return super(TestAbInitio_GMX,self).shortDescription() + " (AbInitio_GMX)"