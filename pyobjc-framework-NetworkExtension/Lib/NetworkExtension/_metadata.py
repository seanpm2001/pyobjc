# This file is generated by objective.metadata
#
# Last update: Thu Nov 12 22:02:13 2020
#
# flake8: noqa

import objc, sys

if sys.maxsize > 2 ** 32:
    def sel32or64(a, b): return b
else:
    def sel32or64(a, b): return a

misc = {
}
constants = '''$NEAppProxyErrorDomain$NEAppPushErrorDomain$NEDNSProxyConfigurationDidChangeNotification$NEDNSProxyErrorDomain$NEDNSSettingsConfigurationDidChangeNotification$NEDNSSettingsErrorDomain$NEFilterConfigurationDidChangeNotification$NEFilterErrorDomain$NEFilterProviderRemediationMapRemediationButtonTexts$NEFilterProviderRemediationMapRemediationURLs$NEHotspotConfigurationErrorDomain$NETunnelProviderErrorDomain$NEVPNConfigurationChangeNotification$NEVPNConnectionStartOptionPassword$NEVPNConnectionStartOptionUsername$NEVPNErrorDomain$NEVPNStatusDidChangeNotification$kNEHotspotHelperOptionDisplayName$'''
enums = '''$NEAppProxyFlowErrorAborted@5$NEAppProxyFlowErrorDatagramTooLarge@9$NEAppProxyFlowErrorHostUnreachable@3$NEAppProxyFlowErrorInternal@8$NEAppProxyFlowErrorInvalidArgument@4$NEAppProxyFlowErrorNotConnected@1$NEAppProxyFlowErrorPeerReset@2$NEAppProxyFlowErrorReadAlreadyPending@10$NEAppProxyFlowErrorRefused@6$NEAppProxyFlowErrorTimedOut@7$NEAppPushManagerErrorConfigurationInvalid@1$NEAppPushManagerErrorConfigurationNotLoaded@2$NEAppPushManagerErrorInactiveSession@4$NEAppPushManagerErrorInternalError@3$NEDNSProtocolCleartext@1$NEDNSProtocolHTTPS@3$NEDNSProtocolTLS@2$NEDNSProxyManagerErrorConfigurationCannotBeRemoved@4$NEDNSProxyManagerErrorConfigurationDisabled@2$NEDNSProxyManagerErrorConfigurationInvalid@1$NEDNSProxyManagerErrorConfigurationStale@3$NEDNSSettingsManagerErrorConfigurationCannotBeRemoved@4$NEDNSSettingsManagerErrorConfigurationDisabled@2$NEDNSSettingsManagerErrorConfigurationInvalid@1$NEDNSSettingsManagerErrorConfigurationStale@3$NEEvaluateConnectionRuleActionConnectIfNeeded@1$NEEvaluateConnectionRuleActionNeverConnect@2$NEFilterActionAllow@1$NEFilterActionDrop@2$NEFilterActionFilterData@4$NEFilterActionInvalid@0$NEFilterActionRemediate@3$NEFilterDataAttributeHasIPHeader@1$NEFilterFlowBytesMax@18446744073709551615$NEFilterManagerErrorConfigurationCannotBeRemoved@4$NEFilterManagerErrorConfigurationDisabled@2$NEFilterManagerErrorConfigurationInternalError@6$NEFilterManagerErrorConfigurationInvalid@1$NEFilterManagerErrorConfigurationPermissionDenied@5$NEFilterManagerErrorConfigurationStale@3$NEFilterManagerGradeFirewall@1$NEFilterManagerGradeInspector@2$NEFilterPacketProviderVerdictAllow@0$NEFilterPacketProviderVerdictDelay@2$NEFilterPacketProviderVerdictDrop@1$NEFilterReportEventDataDecision@2$NEFilterReportEventFlowClosed@3$NEFilterReportEventNewFlow@1$NEFilterReportEventStatistics@4$NEFilterReportFrequencyHigh@3$NEFilterReportFrequencyLow@1$NEFilterReportFrequencyMedium@2$NEFilterReportFrequencyNone@0$NEHotspotConfigurationEAPTLSVersion_1_0@0$NEHotspotConfigurationEAPTLSVersion_1_1@1$NEHotspotConfigurationEAPTLSVersion_1_2@2$NEHotspotConfigurationEAPTTLSInnerAuthenticationCHAP@1$NEHotspotConfigurationEAPTTLSInnerAuthenticationEAP@4$NEHotspotConfigurationEAPTTLSInnerAuthenticationMSCHAP@2$NEHotspotConfigurationEAPTTLSInnerAuthenticationMSCHAPv2@3$NEHotspotConfigurationEAPTTLSInnerAuthenticationPAP@0$NEHotspotConfigurationEAPTypeEAPFAST@43$NEHotspotConfigurationEAPTypeEAPPEAP@25$NEHotspotConfigurationEAPTypeEAPTLS@13$NEHotspotConfigurationEAPTypeEAPTTLS@21$NEHotspotConfigurationErrorAlreadyAssociated@13$NEHotspotConfigurationErrorApplicationIsNotInForeground@14$NEHotspotConfigurationErrorInternal@8$NEHotspotConfigurationErrorInvalid@0$NEHotspotConfigurationErrorInvalidEAPSettings@4$NEHotspotConfigurationErrorInvalidHS20DomainName@6$NEHotspotConfigurationErrorInvalidHS20Settings@5$NEHotspotConfigurationErrorInvalidSSID@1$NEHotspotConfigurationErrorInvalidSSIDPrefix@15$NEHotspotConfigurationErrorInvalidWEPPassphrase@3$NEHotspotConfigurationErrorInvalidWPAPassphrase@2$NEHotspotConfigurationErrorJoinOnceNotSupported@12$NEHotspotConfigurationErrorPending@9$NEHotspotConfigurationErrorSystemConfiguration@10$NEHotspotConfigurationErrorUnknown@11$NEHotspotConfigurationErrorUserDenied@7$NENetworkRuleProtocolAny@0$NENetworkRuleProtocolTCP@1$NENetworkRuleProtocolUDP@2$NEOnDemandRuleActionConnect@1$NEOnDemandRuleActionDisconnect@2$NEOnDemandRuleActionEvaluateConnection@3$NEOnDemandRuleActionIgnore@4$NEOnDemandRuleInterfaceTypeAny@0$NEOnDemandRuleInterfaceTypeCellular@3$NEOnDemandRuleInterfaceTypeEthernet@1$NEOnDemandRuleInterfaceTypeWiFi@2$NEProviderStopReasonAppUpdate@16$NEProviderStopReasonAuthenticationCanceled@6$NEProviderStopReasonConfigurationDisabled@9$NEProviderStopReasonConfigurationFailed@7$NEProviderStopReasonConfigurationRemoved@10$NEProviderStopReasonConnectionFailed@14$NEProviderStopReasonIdleTimeout@8$NEProviderStopReasonNoNetworkAvailable@3$NEProviderStopReasonNone@0$NEProviderStopReasonProviderDisabled@5$NEProviderStopReasonProviderFailed@2$NEProviderStopReasonSleep@15$NEProviderStopReasonSuperceded@11$NEProviderStopReasonUnrecoverableNetworkChange@4$NEProviderStopReasonUserInitiated@1$NEProviderStopReasonUserLogout@12$NEProviderStopReasonUserSwitch@13$NETrafficDirectionAny@0$NETrafficDirectionInbound@1$NETrafficDirectionOutbound@2$NETunnelProviderErrorNetworkSettingsCanceled@2$NETunnelProviderErrorNetworkSettingsFailed@3$NETunnelProviderErrorNetworkSettingsInvalid@1$NETunnelProviderRoutingMethodDestinationIP@1$NETunnelProviderRoutingMethodNetworkRule@3$NETunnelProviderRoutingMethodSourceApplication@2$NEVPNErrorConfigurationDisabled@2$NEVPNErrorConfigurationInvalid@1$NEVPNErrorConfigurationReadWriteFailed@5$NEVPNErrorConfigurationStale@4$NEVPNErrorConfigurationUnknown@6$NEVPNErrorConnectionFailed@3$NEVPNIKEAuthenticationMethodCertificate@1$NEVPNIKEAuthenticationMethodNone@0$NEVPNIKEAuthenticationMethodSharedSecret@2$NEVPNIKEv2CertificateTypeECDSA256@2$NEVPNIKEv2CertificateTypeECDSA384@3$NEVPNIKEv2CertificateTypeECDSA521@4$NEVPNIKEv2CertificateTypeEd25519@5$NEVPNIKEv2CertificateTypeRSA@1$NEVPNIKEv2DeadPeerDetectionRateHigh@3$NEVPNIKEv2DeadPeerDetectionRateLow@1$NEVPNIKEv2DeadPeerDetectionRateMedium@2$NEVPNIKEv2DeadPeerDetectionRateNone@0$NEVPNIKEv2DiffieHellmanGroup0@0$NEVPNIKEv2DiffieHellmanGroup1@1$NEVPNIKEv2DiffieHellmanGroup14@14$NEVPNIKEv2DiffieHellmanGroup15@15$NEVPNIKEv2DiffieHellmanGroup16@16$NEVPNIKEv2DiffieHellmanGroup17@17$NEVPNIKEv2DiffieHellmanGroup18@18$NEVPNIKEv2DiffieHellmanGroup19@19$NEVPNIKEv2DiffieHellmanGroup2@2$NEVPNIKEv2DiffieHellmanGroup20@20$NEVPNIKEv2DiffieHellmanGroup21@21$NEVPNIKEv2DiffieHellmanGroup31@31$NEVPNIKEv2DiffieHellmanGroup5@5$NEVPNIKEv2DiffieHellmanGroupInvalid@0$NEVPNIKEv2EncryptionAlgorithm3DES@2$NEVPNIKEv2EncryptionAlgorithmAES128@3$NEVPNIKEv2EncryptionAlgorithmAES128GCM@5$NEVPNIKEv2EncryptionAlgorithmAES256@4$NEVPNIKEv2EncryptionAlgorithmAES256GCM@6$NEVPNIKEv2EncryptionAlgorithmChaCha20Poly1305@7$NEVPNIKEv2EncryptionAlgorithmDES@1$NEVPNIKEv2IntegrityAlgorithmSHA160@2$NEVPNIKEv2IntegrityAlgorithmSHA256@3$NEVPNIKEv2IntegrityAlgorithmSHA384@4$NEVPNIKEv2IntegrityAlgorithmSHA512@5$NEVPNIKEv2IntegrityAlgorithmSHA96@1$NEVPNIKEv2TLSVersion1_0@1$NEVPNIKEv2TLSVersion1_1@2$NEVPNIKEv2TLSVersion1_2@3$NEVPNIKEv2TLSVersionDefault@0$NEVPNStatusConnected@3$NEVPNStatusConnecting@2$NEVPNStatusDisconnected@1$NEVPNStatusDisconnecting@5$NEVPNStatusInvalid@0$NEVPNStatusReasserting@4$NWPathStatusInvalid@0$NWPathStatusSatisfiable@3$NWPathStatusSatisfied@1$NWPathStatusUnsatisfied@2$NWTCPConnectionStateCancelled@5$NWTCPConnectionStateConnected@3$NWTCPConnectionStateConnecting@1$NWTCPConnectionStateDisconnected@4$NWTCPConnectionStateInvalid@0$NWTCPConnectionStateWaiting@2$NWUDPSessionStateCancelled@5$NWUDPSessionStateFailed@4$NWUDPSessionStateInvalid@0$NWUDPSessionStatePreparing@2$NWUDPSessionStateReady@3$NWUDPSessionStateWaiting@1$kNEHotspotHelperCommandTypeAuthenticate@3$kNEHotspotHelperCommandTypeEvaluate@2$kNEHotspotHelperCommandTypeFilterScanList@1$kNEHotspotHelperCommandTypeLogoff@6$kNEHotspotHelperCommandTypeMaintain@5$kNEHotspotHelperCommandTypeNone@0$kNEHotspotHelperCommandTypePresentUI@4$kNEHotspotHelperConfidenceHigh@2$kNEHotspotHelperConfidenceLow@1$kNEHotspotHelperConfidenceNone@0$kNEHotspotHelperResultAuthenticationRequired@4$kNEHotspotHelperResultCommandNotRecognized@3$kNEHotspotHelperResultFailure@1$kNEHotspotHelperResultSuccess@0$kNEHotspotHelperResultTemporaryFailure@6$kNEHotspotHelperResultUIRequired@2$kNEHotspotHelperResultUnsupportedNetwork@5$'''
misc.update({'NEFilterProviderRemediationURLFlowURL': 'NE_FLOW_URL', 'NEFilterProviderRemediationURLFlowURLHostname': 'NE_FLOW_HOSTNAME', 'NEFilterProviderRemediationURLUsername': 'NE_USERNAME', 'NEFilterProviderRemediationURLOrganization': 'NE_ORGANIZATION'})
aliases = {'NEFilterFlowBytesMax': 'UINT64_MAX'}
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(b'NEAppProxyFlow', b'openWithLocalEndpoint:completionHandler:', {'arguments': {3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}, 'type': '@?'}}})
    r(b'NEAppProxyProvider', b'handleNewFlow:', {'retval': {'type': 'Z'}})
    r(b'NEAppProxyProvider', b'handleNewUDPFlow:initialRemoteEndpoint:', {'retval': {'type': b'Z'}})
    r(b'NEAppProxyProvider', b'startProxyWithOptions:completionHandler:', {'arguments': {3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}, 'type': '@?'}}})
    r(b'NEAppProxyProvider', b'stopProxyWithReason:completionHandler:', {'arguments': {3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}}}, 'type': '@?'}}})
    r(b'NEAppProxyProviderManager', b'loadAllFromPreferencesWithCompletionHandler:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}, 'type': '@?'}}})
    r(b'NEAppProxyTCPFlow', b'readDataWithCompletionHandler:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}, 'type': '@?'}}})
    r(b'NEAppProxyTCPFlow', b'writeData:withCompletionHandler:', {'arguments': {3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}, 'type': '@?'}}})
    r(b'NEAppProxyUDPFlow', b'readDatagramsWithCompletionHandler:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}, 3: {'type': b'@'}}}, 'type': '@?'}}})
    r(b'NEAppProxyUDPFlow', b'writeDatagrams:sentByEndpoints:completionHandler:', {'arguments': {4: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}, 'type': '@?'}}})
    r(b'NEAppPushManager', b'isActive', {'retval': {'type': b'Z'}})
    r(b'NEAppPushManager', b'isEnabled', {'retval': {'type': b'Z'}})
    r(b'NEAppPushManager', b'loadAllFromPreferencesWithCompletionHandler:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}}}})
    r(b'NEAppPushManager', b'loadFromPreferencesWithCompletionHandler:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}}}})
    r(b'NEAppPushManager', b'removeFromPreferencesWithCompletionHandler:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}}}})
    r(b'NEAppPushManager', b'saveToPreferencesWithCompletionHandler:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}}}})
    r(b'NEAppPushManager', b'setEnabled:', {'arguments': {2: {'type': b'Z'}}})
    r(b'NEAppPushProvider', b'startWithCompletionHandler:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}}}})
    r(b'NEAppPushProvider', b'stopWithReason:completionHandler:', {'arguments': {3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}}}}}})
    r(b'NEDNSProxyManager', b'isEnabled', {'retval': {'type': b'Z'}})
    r(b'NEDNSProxyManager', b'loadFromPreferencesWithCompletionHandler:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}}}})
    r(b'NEDNSProxyManager', b'removeFromPreferencesWithCompletionHandler:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}}}})
    r(b'NEDNSProxyManager', b'saveToPreferencesWithCompletionHandler:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}}}})
    r(b'NEDNSProxyManager', b'setEnabled:', {'arguments': {2: {'type': b'Z'}}})
    r(b'NEDNSProxyProvider', b'handleNewFlow:', {'retval': {'type': b'Z'}})
    r(b'NEDNSProxyProvider', b'handleNewUDPFlow:initialRemoteEndpoint:', {'retval': {'type': b'Z'}})
    r(b'NEDNSProxyProvider', b'startProxyWithOptions:completionHandler:', {'arguments': {3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}}}})
    r(b'NEDNSProxyProvider', b'stopProxyWithReason:completionHandler:', {'arguments': {3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}}}}}})
    r(b'NEDNSSettings', b'matchDomainsNoSearch', {'retval': {'type': 'Z'}})
    r(b'NEDNSSettings', b'setMatchDomainsNoSearch:', {'arguments': {2: {'type': 'Z'}}})
    r(b'NEDNSSettingsManager', b'isEnabled', {'retval': {'type': b'Z'}})
    r(b'NEDNSSettingsManager', b'loadFromPreferencesWithCompletionHandler:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}}}})
    r(b'NEDNSSettingsManager', b'removeFromPreferencesWithCompletionHandler:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}}}})
    r(b'NEDNSSettingsManager', b'saveToPreferencesWithCompletionHandler:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}}}})
    r(b'NEFilterControlProvider', b'handleNewFlow:completionHandler:', {'arguments': {3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}, 'type': '@?'}}})
    r(b'NEFilterControlProvider', b'handleRemediationForFlow:completionHandler:', {'arguments': {3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}, 'type': '@?'}}})
    r(b'NEFilterControlVerdict', b'allowVerdictWithUpdateRules:', {'arguments': {2: {'type': b'Z'}}})
    r(b'NEFilterControlVerdict', b'dropVerdictWithUpdateRules:', {'arguments': {2: {'type': b'Z'}}})
    r(b'NEFilterDataProvider', b'applySettings:completionHandler:', {'arguments': {3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}}}})
    r(b'NEFilterManager', b'isEnabled', {'retval': {'type': 'Z'}})
    r(b'NEFilterManager', b'loadFromPreferencesWithCompletionHandler:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}, 'type': '@?'}}})
    r(b'NEFilterManager', b'removeFromPreferencesWithCompletionHandler:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}, 'type': '@?'}}})
    r(b'NEFilterManager', b'saveToPreferencesWithCompletionHandler:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}, 'type': '@?'}}})
    r(b'NEFilterManager', b'setEnabled:', {'arguments': {2: {'type': 'Z'}}})
    r(b'NEFilterNewFlowVerdict', b'filterDataVerdictWithFilterInbound:peekInboundBytes:filterOutbound:peekOutboundBytes:', {'arguments': {2: {'type': b'Z'}, 4: {'type': b'Z'}}})
    r(b'NEFilterPacketProvider', b'packetHandler', {'retval': {'callable': {'retval': {'type': b'q'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}, 3: {'type': b'q'}, 4: {'type': b'n^v'}, 5: {'type': b'l'}}}}})
    r(b'NEFilterPacketProvider', b'setPacketHandler:', {'arguments': {2: {'callable': {'retval': {'type': b'q'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}, 3: {'type': b'q'}, 4: {'type': b'n^v'}, 5: {'type': b'l'}}}}}})
    r(b'NEFilterProvider', b'startFilterWithCompletionHandler:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}}}})
    r(b'NEFilterProvider', b'stopFilterWithReason:completionHandler:', {'arguments': {3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}}}}}})
    r(b'NEFilterProviderConfiguration', b'filterBrowsers', {'retval': {'type': 'Z'}})
    r(b'NEFilterProviderConfiguration', b'filterPackets', {'retval': {'type': b'Z'}})
    r(b'NEFilterProviderConfiguration', b'filterSockets', {'retval': {'type': 'Z'}})
    r(b'NEFilterProviderConfiguration', b'setFilterBrowsers:', {'arguments': {2: {'type': 'Z'}}})
    r(b'NEFilterProviderConfiguration', b'setFilterPackets:', {'arguments': {2: {'type': b'Z'}}})
    r(b'NEFilterProviderConfiguration', b'setFilterSockets:', {'arguments': {2: {'type': 'Z'}}})
    r(b'NEFilterVerdict', b'setShouldReport:', {'arguments': {2: {'type': b'Z'}}})
    r(b'NEFilterVerdict', b'shouldReport', {'retval': {'type': b'Z'}})
    r(b'NEHotspotConfiguration', b'hidden', {'retval': {'type': b'Z'}})
    r(b'NEHotspotConfiguration', b'initWithSSID:passphrase:isWEP:', {'arguments': {4: {'type': b'Z'}}})
    r(b'NEHotspotConfiguration', b'initWithSSIDPrefix:passphrase:isWEP:', {'arguments': {4: {'type': b'Z'}}})
    r(b'NEHotspotConfiguration', b'joinOnce', {'retval': {'type': b'Z'}})
    r(b'NEHotspotConfiguration', b'setHidden:', {'arguments': {2: {'type': b'Z'}}})
    r(b'NEHotspotConfiguration', b'setJoinOnce:', {'arguments': {2: {'type': b'Z'}}})
    r(b'NEHotspotConfigurationManager', b'applyConfiguration:completionHandler:', {'arguments': {3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}}}})
    r(b'NEHotspotConfigurationManager', b'getConfiguredSSIDsWithCompletionHandler:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}}}})
    r(b'NEHotspotEAPSettings', b'isTLSClientCertificateRequired', {'retval': {'type': b'Z'}})
    r(b'NEHotspotEAPSettings', b'setIdentity:', {'retval': {'type': b'Z'}})
    r(b'NEHotspotEAPSettings', b'setTlsClientCertificateRequired:', {'arguments': {2: {'type': b'Z'}}})
    r(b'NEHotspotEAPSettings', b'setTrustedServerCertificates:', {'retval': {'type': b'Z'}})
    r(b'NEHotspotHS20Settings', b'initWithDomainName:roamingEnabled:', {'arguments': {3: {'type': b'Z'}}})
    r(b'NEHotspotHS20Settings', b'isRoamingEnabled', {'retval': {'type': b'Z'}})
    r(b'NEHotspotHS20Settings', b'setRoamingEnabled:', {'arguments': {2: {'type': b'Z'}}})
    r(b'NEHotspotHelper', b'logoff:', {'retval': {'type': b'Z'}})
    r(b'NEHotspotHelper', b'registerWithOptions:queue:handler:', {'retval': {'type': b'Z'}, 'arguments': {4: {'callable': {'retval': {'type': b'@?'}, 'arguments': {0: {'type': b'^v'}}}}}})
    r(b'NEHotspotNetwork', b'didAutoJoin', {'retval': {'type': b'Z'}})
    r(b'NEHotspotNetwork', b'didJustJoin', {'retval': {'type': b'Z'}})
    r(b'NEHotspotNetwork', b'fetchCurrentWithCompletionHandler:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}}}})
    r(b'NEHotspotNetwork', b'isChosenHelper', {'retval': {'type': b'Z'}})
    r(b'NEHotspotNetwork', b'isSecure', {'retval': {'type': b'Z'}})
    r(b'NEPacketTunnelFlow', b'readPacketObjectsWithCompletionHandler:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}, 'type': '@?'}}})
    r(b'NEPacketTunnelFlow', b'readPacketsWithCompletionHandler:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}, 'type': '@?'}}})
    r(b'NEPacketTunnelFlow', b'writePacketObjects:', {'retval': {'type': 'Z'}})
    r(b'NEPacketTunnelFlow', b'writePackets:withProtocols:', {'retval': {'type': 'Z'}})
    r(b'NEPacketTunnelProvider', b'createTCPConnectionThroughTunnelToEndpoint:enableTLS:TLSParameters:delegate:', {'arguments': {3: {'type': 'Z'}}})
    r(b'NEPacketTunnelProvider', b'startTunnelWithOptions:completionHandler:', {'arguments': {3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}, 'type': '@?'}}})
    r(b'NEPacketTunnelProvider', b'stopTunnelWithReason:completionHandler:', {'arguments': {3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}}}, 'type': '@?'}}})
    r(b'NEProvider', b'createTCPConnectionToEndpoint:enableTLS:TLSParameters:delegate:', {'arguments': {3: {'type': 'Z'}}})
    r(b'NEProvider', b'displayMessage:completionHandler:', {'arguments': {3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'Z'}}}}}})
    r(b'NEProvider', b'sleepWithCompletionHandler:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}}}, 'type': '@?'}}})
    r(b'NEProxyServer', b'authenticationRequired', {'retval': {'type': 'Z'}})
    r(b'NEProxyServer', b'setAuthenticationRequired:', {'arguments': {2: {'type': 'Z'}}})
    r(b'NEProxySettings', b'HTTPEnabled', {'retval': {'type': 'Z'}})
    r(b'NEProxySettings', b'HTTPSEnabled', {'retval': {'type': 'Z'}})
    r(b'NEProxySettings', b'autoProxyConfigurationEnabled', {'retval': {'type': 'Z'}})
    r(b'NEProxySettings', b'excludeSimpleHostnames', {'retval': {'type': 'Z'}})
    r(b'NEProxySettings', b'setAutoProxyConfigurationEnabled:', {'arguments': {2: {'type': 'Z'}}})
    r(b'NEProxySettings', b'setExcludeSimpleHostnames:', {'arguments': {2: {'type': 'Z'}}})
    r(b'NEProxySettings', b'setHTTPEnabled:', {'arguments': {2: {'type': 'Z'}}})
    r(b'NEProxySettings', b'setHTTPSEnabled:', {'arguments': {2: {'type': 'Z'}}})
    r(b'NETransparentProxyManager', b'loadAllFromPreferencesWithCompletionHandler:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}}}})
    r(b'NETunnelProvider', b'handleAppMessage:completionHandler:', {'arguments': {3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}, 'type': '@?'}}})
    r(b'NETunnelProvider', b'reasserting', {'retval': {'type': 'Z'}})
    r(b'NETunnelProvider', b'setReasserting:', {'arguments': {2: {'type': 'Z'}}})
    r(b'NETunnelProvider', b'setTunnelNetworkSettings:completionHandler:', {'arguments': {3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}, 'type': '@?'}}})
    r(b'NETunnelProviderManager', b'loadAllFromPreferencesWithCompletionHandler:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}, 'type': '@?'}}})
    r(b'NETunnelProviderSession', b'sendProviderMessage:returnError:responseHandler:', {'retval': {'type': 'Z'}, 'arguments': {3: {'type_modifier': b'o'}, 4: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}, 'type': '@?'}}})
    r(b'NETunnelProviderSession', b'startTunnelWithOptions:andReturnError:', {'retval': {'type': 'Z'}, 'arguments': {3: {'type_modifier': b'o'}}})
    r(b'NEVPNConnection', b'startVPNTunnelAndReturnError:', {'retval': {'type': 'Z'}, 'arguments': {2: {'type_modifier': b'o'}}})
    r(b'NEVPNConnection', b'startVPNTunnelWithOptions:andReturnError:', {'retval': {'type': 'Z'}, 'arguments': {3: {'type_modifier': b'o'}}})
    r(b'NEVPNManager', b'isEnabled', {'retval': {'type': 'Z'}})
    r(b'NEVPNManager', b'isOnDemandEnabled', {'retval': {'type': 'Z'}})
    r(b'NEVPNManager', b'loadFromPreferencesWithCompletionHandler:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}, 'type': '@?'}}})
    r(b'NEVPNManager', b'protocol', {'deprecated': 1011})
    r(b'NEVPNManager', b'removeFromPreferencesWithCompletionHandler:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}, 'type': '@?'}}})
    r(b'NEVPNManager', b'saveToPreferencesWithCompletionHandler:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}, 'type': '@?'}}})
    r(b'NEVPNManager', b'setEnabled:', {'arguments': {2: {'type': 'Z'}}})
    r(b'NEVPNManager', b'setOnDemandEnabled:', {'arguments': {2: {'type': 'Z'}}})
    r(b'NEVPNManager', b'setProtocol:', {'deprecated': 1011})
    r(b'NEVPNProtocol', b'disconnectOnSleep', {'retval': {'type': 'Z'}})
    r(b'NEVPNProtocol', b'enforceRoutes', {'retval': {'type': b'Z'}})
    r(b'NEVPNProtocol', b'excludeLocalNetworks', {'retval': {'type': b'Z'}})
    r(b'NEVPNProtocol', b'includeAllNetworks', {'retval': {'type': b'Z'}})
    r(b'NEVPNProtocol', b'setDisconnectOnSleep:', {'arguments': {2: {'type': 'Z'}}})
    r(b'NEVPNProtocol', b'setEnforceRoutes:', {'arguments': {2: {'type': b'Z'}}})
    r(b'NEVPNProtocol', b'setExcludeLocalNetworks:', {'arguments': {2: {'type': b'Z'}}})
    r(b'NEVPNProtocol', b'setIncludeAllNetworks:', {'arguments': {2: {'type': b'Z'}}})
    r(b'NEVPNProtocolIKEv2', b'disableMOBIKE', {'retval': {'type': 'Z'}})
    r(b'NEVPNProtocolIKEv2', b'disableRedirect', {'retval': {'type': 'Z'}})
    r(b'NEVPNProtocolIKEv2', b'enableFallback', {'retval': {'type': b'Z'}})
    r(b'NEVPNProtocolIKEv2', b'enablePFS', {'retval': {'type': 'Z'}})
    r(b'NEVPNProtocolIKEv2', b'enableRevocationCheck', {'retval': {'type': 'Z'}})
    r(b'NEVPNProtocolIKEv2', b'setDisableMOBIKE:', {'arguments': {2: {'type': 'Z'}}})
    r(b'NEVPNProtocolIKEv2', b'setDisableRedirect:', {'arguments': {2: {'type': 'Z'}}})
    r(b'NEVPNProtocolIKEv2', b'setEnableFallback:', {'arguments': {2: {'type': b'Z'}}})
    r(b'NEVPNProtocolIKEv2', b'setEnablePFS:', {'arguments': {2: {'type': 'Z'}}})
    r(b'NEVPNProtocolIKEv2', b'setEnableRevocationCheck:', {'arguments': {2: {'type': 'Z'}}})
    r(b'NEVPNProtocolIKEv2', b'setStrictRevocationCheck:', {'arguments': {2: {'type': 'Z'}}})
    r(b'NEVPNProtocolIKEv2', b'setUseConfigurationAttributeInternalIPSubnet:', {'arguments': {2: {'type': 'Z'}}})
    r(b'NEVPNProtocolIKEv2', b'strictRevocationCheck', {'retval': {'type': 'Z'}})
    r(b'NEVPNProtocolIKEv2', b'useConfigurationAttributeInternalIPSubnet', {'retval': {'type': 'Z'}})
    r(b'NEVPNProtocolIPSec', b'setUseExtendedAuthentication:', {'arguments': {2: {'type': 'Z'}}})
    r(b'NEVPNProtocolIPSec', b'useExtendedAuthentication', {'retval': {'type': 'Z'}})
    r(b'NSObject', b'appPushManager:didReceiveIncomingCallWithUserInfo:', {'required': True, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}}})
    r(b'NSObject', b'evaluateTrustForConnection:peerCertificateChain:completionHandler:', {'required': False, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'type': b'@'}, 4: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}, 'type': '@?'}}})
    r(b'NSObject', b'provideIdentityForConnection:completionHandler:', {'required': False, 'retval': {'type': b'v'}, 'arguments': {2: {'type': b'@'}, 3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}, 'type': '@?'}}})
    r(b'NSObject', b'shouldEvaluateTrustForConnection:', {'required': False, 'retval': {'type': 'Z'}, 'arguments': {2: {'type': b'@'}}})
    r(b'NSObject', b'shouldProvideIdentityForConnection:', {'required': False, 'retval': {'type': 'Z'}, 'arguments': {2: {'type': b'@'}}})
    r(b'NWPath', b'isConstrained', {'retval': {'type': b'Z'}})
    r(b'NWPath', b'isEqualToPath:', {'retval': {'type': 'Z'}})
    r(b'NWPath', b'isExpensive', {'retval': {'type': 'Z'}})
    r(b'NWTCPConnection', b'hasBetterPath', {'retval': {'type': 'Z'}})
    r(b'NWTCPConnection', b'isViable', {'retval': {'type': 'Z'}})
    r(b'NWTCPConnection', b'readLength:completionHandler:', {'arguments': {3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}}}})
    r(b'NWTCPConnection', b'readMinimumLength:maximumLength:completionHandler:', {'arguments': {4: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}}}})
    r(b'NWTCPConnection', b'write:completionHandler:', {'arguments': {3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}}}})
    r(b'NWUDPSession', b'hasBetterPath', {'retval': {'type': 'Z'}})
    r(b'NWUDPSession', b'isViable', {'retval': {'type': 'Z'}})
    r(b'NWUDPSession', b'setReadHandler:maxDatagrams:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}}}})
    r(b'NWUDPSession', b'writeDatagram:completionHandler:', {'arguments': {3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}}}})
    r(b'NWUDPSession', b'writeMultipleDatagrams:completionHandler:', {'arguments': {3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}}}}}})
    r(b'null', b'didAutoJoin', {'retval': {'type': b'Z'}})
    r(b'null', b'didJustJoin', {'retval': {'type': b'Z'}})
    r(b'null', b'isChosenHelper', {'retval': {'type': b'Z'}})
    r(b'null', b'isSecure', {'retval': {'type': b'Z'}})
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE
