# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, you can obtain one at http://mozilla.org/MPL/2.0/.
from autorepr import autorepr, autostr
from django.db import models

from ..models import CreatedByModel, EditedAtModel, URLActionModel
from .utils import calculate_fingerprint


class SSHKey(CreatedByModel, EditedAtModel, URLActionModel):
    """
    A Django data model to store public SSH keys for logged-in users
    to be used in the :mod:`on-demand clusters <atmo.clusters>`.
    """
    #: The list of valid SSH key data prefixes, will be validated
    #: on save.
    VALID_PREFIXES = [
        'ssh-rsa',
        'ssh-dss',
        'ecdsa-sha2-nistp256',
        'ecdsa-sha2-nistp384',
        'ecdsa-sha2-nistp521',
    ]

    title = models.CharField(
        max_length=100,
        help_text='Name to give to this public key',
    )
    key = models.TextField(
        help_text='Should start with one of the following prefixes: %s' %
                  ', '.join(VALID_PREFIXES),
    )
    fingerprint = models.CharField(
        max_length=48,
        blank=True,
    )

    class Meta:
        permissions = [
            ('view_sshkey', 'Can view SSH key'),
        ]
        unique_together = (
            ('created_by', 'fingerprint')
        )

    __str__ = autostr('{self.title}')

    __repr__ = autorepr(['title', 'fingerprint'])

    url_prefix = 'keys'
    url_actions = ['detail', 'delete', 'raw']

    def get_absolute_url(self):
        return self.urls.detail

    @property
    def prefix(self):
        """
        The prefix of the key data,
        one of the :data:`~atmo.keys.models.SSHKey.VALID_PREFIXES`.
        """
        return self.key.strip().split()[0]

    def save(self, *args, **kwargs):
        self.fingerprint = calculate_fingerprint(self.key)
        super().save(*args, **kwargs)
