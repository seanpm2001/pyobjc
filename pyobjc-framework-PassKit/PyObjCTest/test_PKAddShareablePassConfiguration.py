from PyObjCTools.TestSupport import TestCase

import PassKit


class TestPKAddShareablePassConfiguration(TestCase):
    def test_constants(self):
        self.assertEqual(PassKit.PKAddShareablePassConfigurationPrimaryActionAdd, 0)
        self.assertEqual(PassKit.PKAddShareablePassConfigurationPrimaryActionShare, 1)

    def test_methods(self):
        self.assertArgIsBOOL(
            PassKit.PKShareablePassMetadata.initWithProvisioningCredentialIdentifier_sharingInstanceIdentifier_passThumbnailImage_ownerDisplayName_localizedDescription_accountHash_templateIdentifier_relyingPartyIdentifier_requiresUnifiedAccessCapableDevice_,  # noqa: B950
            8,
        )
        self.assertResultIsBOOL(
            PassKit.PKShareablePassMetadata.requiresUnifiedAccessCapableDevice
        )

        self.assertArgIsBlock(
            PassKit.PKAddShareablePassConfiguration.configurationForPassMetadata_provisioningPolicyIdentifier_primaryAction_completions_,  # noqa: B950
            3,
            b"v@@",
        )