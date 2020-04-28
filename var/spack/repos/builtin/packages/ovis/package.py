# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Ovis(AutotoolsPackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://github.com/ovis-hpc/ovis/wiki"
    url      = "https://github.com/ovis-hpc/ovis/archive/OVIS-4.3.3.tar.gz"

    version('4.3.3',      sha256='88fa1258de70124ce91544a55ef8d2d38b20203631e158a9cdeac5e38e0780e8')
    version('4.3.2',      sha256='52c5d889667a785a90cb70ba820040018437d9aeda83077dd9caa9fa71b05f0f')
    version('4.2.3',      sha256='656ad737b86d9d8ea0b64392b3c02284dc21381dff3578bbaa60f0d54eeab3f0')
    version('4.2.2',      sha256='10ba567cbba762b298264ee6baaae24a9f5299bec137885643aa64ad3bf855d8')

    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool',  type='build')
    depends_on('m4',       type='build')
    depends_on('glib',     type='build')
    depends_on('readline', type='build')
    depends_on('openssl',  type='build')

    variant('ldms', default=False, description='LDMS Python Interface')
    variant('docs', default=False, description='Build docs')

    depends_on('python@2.7.18', type='build', when='+ldms')
    depends_on('swig', type='build', when='+ldms')
    depends_on('doxygen', type='build', when='+docs')

    #def autoreconf(self, spec, prefix):
    #    autoreconf('--install')

    def configure_args(self):
        args=['--prefix={0}'.format(self.spec.prefix)]

        return args
