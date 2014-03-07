from __future__ import print_function, division
import unittest

import forest

import env
import robots

class TestMultiKin(unittest.TestCase):

    def test_init(self):

        def test_kin():
            """Test if KinematicArm2D instanciates properly"""
            check = True

            arm = robots.KinematicArm2D(dim = 6)
            self.assertEqual(arm.dim, 6)

            cfg = forest.Tree()
            cfg.dim = 1
            cfg.lengths = 1.0
            cfg.limits = (-1.0, 1.0)
            arm = robots.KinematicArm2D(cfg)
            self.assertEqual(arm.dim, 1)

            cfg.dim = 6
            arm = robots.KinematicArm2D(cfg)
            self.assertEqual(arm.m_feats, tuple(range(-6, 0)))
            self.assertEqual(arm.s_feats, (0, 1))
            self.assertEqual(arm.m_bounds, 6*((-1.0, 1.0),))
