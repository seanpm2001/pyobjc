# This file is generated by objective.metadata
#
# Last update: Fri Jan 26 15:23:36 2024
#
# flake8: noqa

import objc, sys
from typing import NewType

if sys.maxsize > 2**32:

    def sel32or64(a, b):
        return b

else:

    def sel32or64(a, b):
        return a


if objc.arch == "arm64":

    def selAorI(a, b):
        return a

else:

    def selAorI(a, b):
        return b


misc = {}
constants = """$MPErrorDomain$MPLanguageOptionCharacteristicContainsOnlyForcedSubtitles$MPLanguageOptionCharacteristicDescribesMusicAndSound$MPLanguageOptionCharacteristicDescribesVideo$MPLanguageOptionCharacteristicDubbedTranslation$MPLanguageOptionCharacteristicEasyToRead$MPLanguageOptionCharacteristicIsAuxiliaryContent$MPLanguageOptionCharacteristicIsMainProgramContent$MPLanguageOptionCharacteristicLanguageTranslation$MPLanguageOptionCharacteristicTranscribesSpokenDialog$MPLanguageOptionCharacteristicVoiceOverTranslation$MPMediaEntityPropertyPersistentID$MPMediaItemPropertyAlbumArtist$MPMediaItemPropertyAlbumArtistPersistentID$MPMediaItemPropertyAlbumPersistentID$MPMediaItemPropertyAlbumTitle$MPMediaItemPropertyAlbumTrackCount$MPMediaItemPropertyAlbumTrackNumber$MPMediaItemPropertyArtist$MPMediaItemPropertyArtistPersistentID$MPMediaItemPropertyArtwork$MPMediaItemPropertyAssetURL$MPMediaItemPropertyBeatsPerMinute$MPMediaItemPropertyBookmarkTime$MPMediaItemPropertyComments$MPMediaItemPropertyComposer$MPMediaItemPropertyComposerPersistentID$MPMediaItemPropertyDateAdded$MPMediaItemPropertyDiscCount$MPMediaItemPropertyDiscNumber$MPMediaItemPropertyGenre$MPMediaItemPropertyGenrePersistentID$MPMediaItemPropertyHasProtectedAsset$MPMediaItemPropertyIsCloudItem$MPMediaItemPropertyIsCompilation$MPMediaItemPropertyIsExplicit$MPMediaItemPropertyIsPreorder$MPMediaItemPropertyLastPlayedDate$MPMediaItemPropertyLyrics$MPMediaItemPropertyMediaType$MPMediaItemPropertyPersistentID$MPMediaItemPropertyPlayCount$MPMediaItemPropertyPlaybackDuration$MPMediaItemPropertyPlaybackStoreID$MPMediaItemPropertyPodcastPersistentID$MPMediaItemPropertyPodcastTitle$MPMediaItemPropertyRating$MPMediaItemPropertyReleaseDate$MPMediaItemPropertySkipCount$MPMediaItemPropertyTitle$MPMediaItemPropertyUserGrouping$MPMediaLibraryDidChangeNotification$MPMediaPlaybackIsPreparedToPlayDidChangeNotification$MPMediaPlaylistPropertyAuthorDisplayName$MPMediaPlaylistPropertyCloudGlobalID$MPMediaPlaylistPropertyDescriptionText$MPMediaPlaylistPropertyName$MPMediaPlaylistPropertyPersistentID$MPMediaPlaylistPropertyPlaylistAttributes$MPMediaPlaylistPropertySeedItems$MPMusicPlayerControllerNowPlayingItemDidChangeNotification$MPMusicPlayerControllerPlaybackStateDidChangeNotification$MPMusicPlayerControllerQueueDidChangeNotification$MPMusicPlayerControllerVolumeDidChangeNotification$MPNowPlayingInfoCollectionIdentifier$MPNowPlayingInfoPropertyAdTimeRanges$MPNowPlayingInfoPropertyAssetURL$MPNowPlayingInfoPropertyAvailableLanguageOptions$MPNowPlayingInfoPropertyChapterCount$MPNowPlayingInfoPropertyChapterNumber$MPNowPlayingInfoPropertyCreditsStartTime$MPNowPlayingInfoPropertyCurrentLanguageOptions$MPNowPlayingInfoPropertyCurrentPlaybackDate$MPNowPlayingInfoPropertyDefaultPlaybackRate$MPNowPlayingInfoPropertyElapsedPlaybackTime$MPNowPlayingInfoPropertyExternalContentIdentifier$MPNowPlayingInfoPropertyExternalUserProfileIdentifier$MPNowPlayingInfoPropertyIsLiveStream$MPNowPlayingInfoPropertyMediaType$MPNowPlayingInfoPropertyPlaybackProgress$MPNowPlayingInfoPropertyPlaybackQueueCount$MPNowPlayingInfoPropertyPlaybackQueueIndex$MPNowPlayingInfoPropertyPlaybackRate$MPNowPlayingInfoPropertyServiceIdentifier$MPNowPlayingInfoPropertyServiceIdentifier,$"""
enums = """$MPChangeLanguageOptionSettingNone@0$MPChangeLanguageOptionSettingNowPlayingItemOnly@1$MPChangeLanguageOptionSettingPermanent@2$MPErrorCancelled@6$MPErrorCloudServiceCapabilityMissing@2$MPErrorNetworkConnectionFailed@3$MPErrorNotFound@4$MPErrorNotSupported@5$MPErrorPermissionDenied@1$MPErrorRequestTimedOut@7$MPErrorUnknown@0$MPMediaGroupingAlbum@1$MPMediaGroupingAlbumArtist@3$MPMediaGroupingArtist@2$MPMediaGroupingComposer@4$MPMediaGroupingGenre@5$MPMediaGroupingPlaylist@6$MPMediaGroupingPodcastTitle@7$MPMediaGroupingTitle@0$MPMediaLibraryAuthorizationStatusAuthorized@3$MPMediaLibraryAuthorizationStatusDenied@1$MPMediaLibraryAuthorizationStatusNotDetermined@0$MPMediaLibraryAuthorizationStatusRestricted@2$MPMediaPlaylistAttributeGenius@4$MPMediaPlaylistAttributeNone@0$MPMediaPlaylistAttributeOnTheGo@1$MPMediaPlaylistAttributeSmart@2$MPMediaPredicateComparisonContains@1$MPMediaPredicateComparisonEqualTo@0$MPMediaTypeAny@18446744073709551615$MPMediaTypeAnyAudio@255$MPMediaTypeAnyVideo@65280$MPMediaTypeAudioBook@4$MPMediaTypeAudioITunesU@8$MPMediaTypeHomeVideo@8192$MPMediaTypeMovie@256$MPMediaTypeMusic@1$MPMediaTypeMusicVideo@2048$MPMediaTypePodcast@2$MPMediaTypeTVShow@512$MPMediaTypeVideoITunesU@4096$MPMediaTypeVideoPodcast@1024$MPMusicPlaybackStateInterrupted@3$MPMusicPlaybackStatePaused@2$MPMusicPlaybackStatePlaying@1$MPMusicPlaybackStateSeekingBackward@5$MPMusicPlaybackStateSeekingForward@4$MPMusicPlaybackStateStopped@0$MPMusicRepeatModeAll@3$MPMusicRepeatModeDefault@0$MPMusicRepeatModeNone@1$MPMusicRepeatModeOne@2$MPMusicShuffleModeAlbums@3$MPMusicShuffleModeDefault@0$MPMusicShuffleModeOff@1$MPMusicShuffleModeSongs@2$MPNowPlayingInfoLanguageOptionTypeAudible@0$MPNowPlayingInfoLanguageOptionTypeLegible@1$MPNowPlayingInfoMediaTypeAudio@1$MPNowPlayingInfoMediaTypeNone@0$MPNowPlayingInfoMediaTypeVideo@2$MPNowPlayingPlaybackStateInterrupted@4$MPNowPlayingPlaybackStatePaused@2$MPNowPlayingPlaybackStatePlaying@1$MPNowPlayingPlaybackStateStopped@3$MPNowPlayingPlaybackStateUnknown@0$MPRemoteCommandHandlerStatusCommandFailed@200$MPRemoteCommandHandlerStatusDeviceNotFound@120$MPRemoteCommandHandlerStatusNoActionableNowPlayingItem@110$MPRemoteCommandHandlerStatusNoSuchContent@100$MPRemoteCommandHandlerStatusSuccess@0$MPRepeatTypeAll@2$MPRepeatTypeOff@0$MPRepeatTypeOne@1$MPSeekCommandEventTypeBeginSeeking@0$MPSeekCommandEventTypeEndSeeking@1$MPShuffleTypeCollections@2$MPShuffleTypeItems@1$MPShuffleTypeOff@0$MPSleepTimerStopModeChapterEnd@2$MPSleepTimerStopModeItemEnd@3$MPSleepTimerStopModeOff@0$MPSleepTimerStopModeTime@1$"""
misc.update(
    {
        "MPRepeatType": NewType("MPRepeatType", int),
        "MPChangeLanguageOptionSetting": NewType("MPChangeLanguageOptionSetting", int),
        "MPSleepTimerStopMode": NewType("MPSleepTimerStopMode", int),
        "MPSeekCommandEventType": NewType("MPSeekCommandEventType", int),
        "MPMediaLibraryAuthorizationStatus": NewType(
            "MPMediaLibraryAuthorizationStatus", int
        ),
        "MPMediaGrouping": NewType("MPMediaGrouping", int),
        "MPMusicPlaybackState": NewType("MPMusicPlaybackState", int),
        "MPMusicRepeatMode": NewType("MPMusicRepeatMode", int),
        "MPMediaPredicateComparison": NewType("MPMediaPredicateComparison", int),
        "MPMediaType": NewType("MPMediaType", int),
        "MPErrorCode": NewType("MPErrorCode", int),
        "MPNowPlayingInfoLanguageOptionType": NewType(
            "MPNowPlayingInfoLanguageOptionType", int
        ),
        "MPShuffleType": NewType("MPShuffleType", int),
        "MPNowPlayingPlaybackState": NewType("MPNowPlayingPlaybackState", int),
        "MPNowPlayingInfoMediaType": NewType("MPNowPlayingInfoMediaType", int),
        "MPMusicShuffleMode": NewType("MPMusicShuffleMode", int),
        "MPMediaPlaylistAttribute": NewType("MPMediaPlaylistAttribute", int),
        "MPRemoteCommandHandlerStatus": NewType("MPRemoteCommandHandlerStatus", int),
    }
)
misc.update({})
misc.update({})
functions = {
    "MPVolumeSettingsAlertIsVisible": (b"Z",),
    "MPVolumeSettingsAlertHide": (b"v",),
    "MPVolumeSettingsAlertShow": (b"v",),
}
aliases = {
    "MP_DEPRECATED_WITH_REPLACEMENT_END": "__API_DEPRECATED_WITH_REPLACEMENT_END",
    "MP_DEPRECATED_BEGIN": "__API_DEPRECATED_BEGIN",
    "MP_UNAVAILABLE_END": "__API_UNAVAILABLE_END",
    "MP_API_END": "__API_AVAILABLE_END",
    "MP_API_BEGIN": "__API_AVAILABLE_BEGIN",
    "MP_DEPRECATED_END": "__API_DEPRECATED_END",
}
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(
        b"MPAdTimeRange",
        b"initWithTimeRange:",
        {"arguments": {2: {"type": b"{_CMTimeRange={_CMTime=qiIq}{_CMTime=qiIq}}"}}},
    )
    r(
        b"MPAdTimeRange",
        b"setTimeRange:",
        {"arguments": {2: {"type": b"{_CMTimeRange={_CMTime=qiIq}{_CMTime=qiIq}}"}}},
    )
    r(
        b"MPAdTimeRange",
        b"timeRange",
        {"retval": {"type": b"{_CMTimeRange={_CMTime=qiIq}{_CMTime=qiIq}}"}},
    )
    r(
        b"MPChangeRepeatModeCommandEvent",
        b"preservesRepeatMode",
        {"retval": {"type": "Z"}},
    )
    r(
        b"MPChangeRepeatModeCommandEvent",
        b"setPreservesRepeatMode:",
        {"arguments": {2: {"type": "Z"}}},
    )
    r(
        b"MPChangeShuffleModeCommandEvent",
        b"preservesShuffleMode",
        {"retval": {"type": "Z"}},
    )
    r(
        b"MPChangeShuffleModeCommandEvent",
        b"setPreservesShuffleMode:",
        {"arguments": {2: {"type": "Z"}}},
    )
    r(b"MPContentItem", b"isContainer", {"retval": {"type": "Z"}})
    r(b"MPContentItem", b"isExplicitContent", {"retval": {"type": "Z"}})
    r(b"MPContentItem", b"isPlayable", {"retval": {"type": "Z"}})
    r(b"MPContentItem", b"isStreamingContent", {"retval": {"type": "Z"}})
    r(b"MPContentItem", b"setContainer:", {"arguments": {2: {"type": "Z"}}})
    r(b"MPContentItem", b"setExplicitContent:", {"arguments": {2: {"type": "Z"}}})
    r(b"MPContentItem", b"setPlayable:", {"arguments": {2: {"type": "Z"}}})
    r(b"MPContentItem", b"setStreamingContent:", {"arguments": {2: {"type": "Z"}}})
    r(b"MPFeedbackCommand", b"isActive", {"retval": {"type": "Z"}})
    r(b"MPFeedbackCommand", b"setActive:", {"arguments": {2: {"type": "Z"}}})
    r(b"MPFeedbackCommandEvent", b"isNegative", {"retval": {"type": "Z"}})
    r(b"MPFeedbackCommandEvent", b"setNegative:", {"arguments": {2: {"type": "Z"}}})
    r(b"MPMediaEntity", b"canFilterByProperty:", {"retval": {"type": "Z"}})
    r(
        b"MPMediaEntity",
        b"enumerateValuesForProperties:usingBlock:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                            3: {"type": b"o^Z"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"MPMediaEntity",
        b"enumerateValuesForProperties:usingBlock::",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                            3: {"type": b"o^Z"},
                        },
                    }
                }
            }
        },
    )
    r(b"MPMediaItem", b"hasProtectedAsset", {"retval": {"type": "Z"}})
    r(b"MPMediaItem", b"isCloudItem", {"retval": {"type": "Z"}})
    r(b"MPMediaItem", b"isCompilation", {"retval": {"type": "Z"}})
    r(b"MPMediaItem", b"isExplicitItem", {"retval": {"type": "Z"}})
    r(b"MPMediaItem", b"isPreorder", {"retval": {"type": b"Z"}})
    r(b"MPMediaItem", b"setCloudItem:", {"arguments": {2: {"type": "Z"}}})
    r(b"MPMediaItem", b"setCompilation:", {"arguments": {2: {"type": "Z"}}})
    r(b"MPMediaItem", b"setExplicitItem:", {"arguments": {2: {"type": "Z"}}})
    r(b"MPMediaItem", b"setHasProtectedAsset:", {"arguments": {2: {"type": "Z"}}})
    r(
        b"MPMediaItemArtwork",
        b"initWithBoundsSize:requestHandler:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"@"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"{CGSize=dd}"}},
                    }
                }
            }
        },
    )
    r(
        b"MPMediaLibrary",
        b"addItemWithProductID:completionHandler:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"MPMediaLibrary",
        b"getPlaylistWithUUID:creationMetadata:completionHandler:",
        {
            "arguments": {
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"MPMediaLibrary",
        b"requestAuthorization:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"q"}},
                    }
                }
            }
        },
    )
    r(
        b"MPMediaPlaylist",
        b"addItemWithProductID:completionHandler:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                }
            }
        },
    )
    r(
        b"MPMediaPlaylist",
        b"addMediaItems:completionHandler:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                }
            }
        },
    )
    r(
        b"MPMusicPlayerApplicationController",
        b"performQueueTransaction:completionHandler:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                },
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                        },
                    }
                },
            }
        },
    )
    r(
        b"MPMusicPlayerController",
        b"prepareToPlayWithCompletionHandler:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                }
            }
        },
    )
    r(
        b"MPNowPlayingInfoLanguageOption",
        b"isAutomaticAudibleLanguageOption",
        {"retval": {"type": "Z"}},
    )
    r(
        b"MPNowPlayingInfoLanguageOption",
        b"isAutomaticLegibleLanguageOption",
        {"retval": {"type": "Z"}},
    )
    r(
        b"MPNowPlayingInfoLanguageOptionGroup",
        b"allowEmptySelection",
        {"retval": {"type": "Z"}},
    )
    r(
        b"MPNowPlayingInfoLanguageOptionGroup",
        b"initWithLanguageOptions:defaultLanguageOption:allowEmptySelection:",
        {"arguments": {4: {"type": "Z"}}},
    )
    r(
        b"MPNowPlayingInfoLanguageOptionGroup",
        b"setAllowEmptySelection:",
        {"arguments": {2: {"type": "Z"}}},
    )
    r(
        b"MPNowPlayingSession",
        b"automaticallyPublishNowPlayingInfo",
        {"retval": {"type": b"Z"}},
    )
    r(
        b"MPNowPlayingSession",
        b"automaticallyPublishesNowPlayingInfo",
        {"retval": {"type": b"Z"}},
    )
    r(
        b"MPNowPlayingSession",
        b"becomeActiveIfPossibleWithCompletion:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"Z"}},
                    }
                }
            }
        },
    )
    r(b"MPNowPlayingSession", b"canBecomeActive", {"retval": {"type": b"Z"}})
    r(b"MPNowPlayingSession", b"isActive", {"retval": {"type": b"Z"}})
    r(
        b"MPNowPlayingSession",
        b"setAutomaticallyPublishNowPlayingInfo:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(
        b"MPNowPlayingSession",
        b"setAutomaticallyPublishesNowPlayingInfo:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(
        b"MPPlayableContentManagerContext",
        b"contentLimitsEnabled",
        {"retval": {"type": "Z"}},
    )
    r(
        b"MPPlayableContentManagerContext",
        b"contentLimitsEnforced",
        {"retval": {"type": "Z"}},
    )
    r(
        b"MPPlayableContentManagerContext",
        b"endpointAvailable",
        {"retval": {"type": "Z"}},
    )
    r(
        b"MPPlayableContentManagerContext",
        b"setContentLimitsEnabled:",
        {"arguments": {2: {"type": "Z"}}},
    )
    r(
        b"MPPlayableContentManagerContext",
        b"setContentLimitsEnforced:",
        {"arguments": {2: {"type": "Z"}}},
    )
    r(
        b"MPPlayableContentManagerContext",
        b"setEndpointAvailable:",
        {"arguments": {2: {"type": "Z"}}},
    )
    r(
        b"MPRemoteCommand",
        b"addTargetWithHandler:",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"q"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    }
                }
            }
        },
    )
    r(b"MPRemoteCommand", b"isEnabled", {"retval": {"type": "Z"}})
    r(b"MPRemoteCommand", b"setEnabled:", {"arguments": {2: {"type": "Z"}}})
    r(
        b"NSObject",
        b"beginLoadingChildItemsAtIndexPath:completionHandler:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {
                2: {"type": b"@"},
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    },
                    "type": b"@?",
                },
            },
        },
    )
    r(
        b"NSObject",
        b"beginSeekingBackward",
        {"required": True, "retval": {"type": b"v"}},
    )
    r(b"NSObject", b"beginSeekingForward", {"required": True, "retval": {"type": b"v"}})
    r(
        b"NSObject",
        b"childItemsDisplayPlaybackProgressAtIndexPath:",
        {"required": False, "retval": {"type": b"Z"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"contentItemAtIndexPath:",
        {"required": True, "retval": {"type": b"@"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"contentItemForIdentifier:completionHandler:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {
                2: {"type": b"@"},
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                        },
                    },
                    "type": b"@?",
                },
            },
        },
    )
    r(b"NSObject", b"currentPlaybackRate", {"required": True, "retval": {"type": b"f"}})
    r(b"NSObject", b"currentPlaybackTime", {"required": True, "retval": {"type": b"d"}})
    r(b"NSObject", b"endSeeking", {"required": True, "retval": {"type": b"v"}})
    r(b"NSObject", b"isPreparedToPlay", {"required": True, "retval": {"type": b"Z"}})
    r(
        b"NSObject",
        b"nowPlayingSessionDidChangeActive:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"nowPlayingSessionDidChangeCanBecomeActive:",
        {"required": False, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"numberOfChildItemsAtIndexPath:",
        {"required": True, "retval": {"type": b"q"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"openToPlayQueueDescriptor:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(b"NSObject", b"pause", {"required": True, "retval": {"type": b"v"}})
    r(b"NSObject", b"play", {"required": True, "retval": {"type": b"v"}})
    r(
        b"NSObject",
        b"playableContentManager:didUpdateContext:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"playableContentManager:initializePlaybackQueueWithCompletionHandler:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {
                2: {"type": b"@"},
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    },
                    "type": b"@?",
                },
            },
        },
    )
    r(
        b"NSObject",
        b"playableContentManager:initializePlaybackQueueWithContentItems:completionHandler:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {
                2: {"type": b"@"},
                3: {"type": b"@"},
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    },
                    "type": b"@?",
                },
            },
        },
    )
    r(
        b"NSObject",
        b"playableContentManager:initiatePlaybackOfContentItemAtIndexPath:completionHandler:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {
                2: {"type": b"@"},
                3: {"type": b"@"},
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    },
                    "type": b"@?",
                },
            },
        },
    )
    r(b"NSObject", b"prepareToPlay", {"required": True, "retval": {"type": b"v"}})
    r(
        b"NSObject",
        b"setCurrentPlaybackRate:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"f"}}},
    )
    r(
        b"NSObject",
        b"setCurrentPlaybackTime:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"d"}}},
    )
    r(b"NSObject", b"stop", {"required": True, "retval": {"type": b"v"}})
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE
