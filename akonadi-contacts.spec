#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v18
# autospec commit: f35655a
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : akonadi-contacts
Version  : 24.08.0
Release  : 77
URL      : https://download.kde.org/stable/release-service/24.08.0/src/akonadi-contacts-24.08.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/24.08.0/src/akonadi-contacts-24.08.0.tar.xz
Source1  : https://download.kde.org/stable/release-service/24.08.0/src/akonadi-contacts-24.08.0.tar.xz.sig
Source2  : BB463350D6EF31EF.pkey
Summary  : Libraries and daemons to implement Contact Management in Akonadi
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GPL-2.0 LGPL-2.0
Requires: akonadi-contacts-data = %{version}-%{release}
Requires: akonadi-contacts-lib = %{version}-%{release}
Requires: akonadi-contacts-license = %{version}-%{release}
Requires: akonadi-contacts-locales = %{version}-%{release}
BuildRequires : akonadi-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : grantleetheme-dev
BuildRequires : kcontacts-dev
BuildRequires : kmime-dev
BuildRequires : prison-dev
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Akonadi Contacts #
Akonadi Contacts is a library that effectively bridges the type-agnostic API of
the Akonadi client libraries and the domain-specific KContacts library. It provides
jobs, models and other helpers to make working with contacts and addressbooks through
Akonadi easier.

%package data
Summary: data components for the akonadi-contacts package.
Group: Data

%description data
data components for the akonadi-contacts package.


%package dev
Summary: dev components for the akonadi-contacts package.
Group: Development
Requires: akonadi-contacts-lib = %{version}-%{release}
Requires: akonadi-contacts-data = %{version}-%{release}
Provides: akonadi-contacts-devel = %{version}-%{release}
Requires: akonadi-contacts = %{version}-%{release}

%description dev
dev components for the akonadi-contacts package.


%package lib
Summary: lib components for the akonadi-contacts package.
Group: Libraries
Requires: akonadi-contacts-data = %{version}-%{release}
Requires: akonadi-contacts-license = %{version}-%{release}

%description lib
lib components for the akonadi-contacts package.


%package license
Summary: license components for the akonadi-contacts package.
Group: Default

%description license
license components for the akonadi-contacts package.


%package locales
Summary: locales components for the akonadi-contacts package.
Group: Default

%description locales
locales components for the akonadi-contacts package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) BB463350D6EF31EF' gpg.status
%setup -q -n akonadi-contacts-24.08.0
cd %{_builddir}/akonadi-contacts-24.08.0
pushd ..
cp -a akonadi-contacts-24.08.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1724651889
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake .. -DQT_MAJOR_VERSION=6  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake .. -DQT_MAJOR_VERSION=6  -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1724651889
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/akonadi-contacts
cp %{_builddir}/akonadi-contacts-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/akonadi-contacts/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/akonadi-contacts-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/akonadi-contacts/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/akonadi-contacts-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/akonadi-contacts/e712eadfab0d2357c0f50f599ef35ee0d87534cb || :
cp %{_builddir}/akonadi-contacts-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/akonadi-contacts/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/akonadi-contacts-%{version}/README.md.license %{buildroot}/usr/share/package-licenses/akonadi-contacts/cadc9e08cb956c041f87922de84b9206d9bbffb2 || :
cp %{_builddir}/akonadi-contacts-%{version}/metainfo.yaml.license %{buildroot}/usr/share/package-licenses/akonadi-contacts/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang akonadicontact6-serializer
%find_lang akonadicontact6
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/akonadi/plugins/serializer/akonadi_serializer_addressee.desktop
/usr/share/akonadi/plugins/serializer/akonadi_serializer_contactgroup.desktop
/usr/share/kf6/akonadi/contact/data/zone.tab
/usr/share/kf6/akonadi/contact/pics/world.jpg
/usr/share/qlogging-categories6/akonadi-contacts.categories
/usr/share/qlogging-categories6/akonadi-contacts.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KPim6/AkonadiContactCore/Akonadi/AbstractContactFormatter
/usr/include/KPim6/AkonadiContactCore/Akonadi/AbstractContactGroupFormatter
/usr/include/KPim6/AkonadiContactCore/Akonadi/ContactGrantleeWrapper
/usr/include/KPim6/AkonadiContactCore/Akonadi/ContactGroupExpandJob
/usr/include/KPim6/AkonadiContactCore/Akonadi/ContactGroupSearchJob
/usr/include/KPim6/AkonadiContactCore/Akonadi/ContactParts
/usr/include/KPim6/AkonadiContactCore/Akonadi/ContactSearchJob
/usr/include/KPim6/AkonadiContactCore/Akonadi/ContactsFilterProxyModel
/usr/include/KPim6/AkonadiContactCore/Akonadi/ContactsTreeModel
/usr/include/KPim6/AkonadiContactCore/Akonadi/EmailAddressSelection
/usr/include/KPim6/AkonadiContactCore/Akonadi/EmailAddressSelectionModel
/usr/include/KPim6/AkonadiContactCore/Akonadi/GrantleeContactFormatter
/usr/include/KPim6/AkonadiContactCore/Akonadi/GrantleeContactGroupFormatter
/usr/include/KPim6/AkonadiContactCore/Akonadi/GrantleePrint
/usr/include/KPim6/AkonadiContactCore/Akonadi/StandardContactFormatter
/usr/include/KPim6/AkonadiContactCore/Akonadi/StandardContactGroupFormatter
/usr/include/KPim6/AkonadiContactCore/akonadi-contact_core_version.h
/usr/include/KPim6/AkonadiContactCore/akonadi/abstractcontactformatter.h
/usr/include/KPim6/AkonadiContactCore/akonadi/abstractcontactgroupformatter.h
/usr/include/KPim6/AkonadiContactCore/akonadi/akonadi-contact-core_export.h
/usr/include/KPim6/AkonadiContactCore/akonadi/contactgrantleewrapper.h
/usr/include/KPim6/AkonadiContactCore/akonadi/contactgroupexpandjob.h
/usr/include/KPim6/AkonadiContactCore/akonadi/contactgroupsearchjob.h
/usr/include/KPim6/AkonadiContactCore/akonadi/contactparts.h
/usr/include/KPim6/AkonadiContactCore/akonadi/contactsearchjob.h
/usr/include/KPim6/AkonadiContactCore/akonadi/contactsfilterproxymodel.h
/usr/include/KPim6/AkonadiContactCore/akonadi/contactstreemodel.h
/usr/include/KPim6/AkonadiContactCore/akonadi/emailaddressselection.h
/usr/include/KPim6/AkonadiContactCore/akonadi/emailaddressselectionmodel.h
/usr/include/KPim6/AkonadiContactCore/akonadi/grantleecontactformatter.h
/usr/include/KPim6/AkonadiContactCore/akonadi/grantleecontactgroupformatter.h
/usr/include/KPim6/AkonadiContactCore/akonadi/grantleeprint.h
/usr/include/KPim6/AkonadiContactCore/akonadi/standardcontactformatter.h
/usr/include/KPim6/AkonadiContactCore/akonadi/standardcontactgroupformatter.h
/usr/include/KPim6/AkonadiContactWidgets/Akonadi/AbstractEmailAddressSelectionDialog
/usr/include/KPim6/AkonadiContactWidgets/Akonadi/AddContactJob
/usr/include/KPim6/AkonadiContactWidgets/Akonadi/AddEmailAddressJob
/usr/include/KPim6/AkonadiContactWidgets/Akonadi/AddEmailDisplayJob
/usr/include/KPim6/AkonadiContactWidgets/Akonadi/ContactEditor
/usr/include/KPim6/AkonadiContactWidgets/Akonadi/ContactEditorDialog
/usr/include/KPim6/AkonadiContactWidgets/Akonadi/ContactEditorPagePlugin
/usr/include/KPim6/AkonadiContactWidgets/Akonadi/ContactGroupEditor
/usr/include/KPim6/AkonadiContactWidgets/Akonadi/ContactGroupEditorDialog
/usr/include/KPim6/AkonadiContactWidgets/Akonadi/ContactGroupViewer
/usr/include/KPim6/AkonadiContactWidgets/Akonadi/ContactViewer
/usr/include/KPim6/AkonadiContactWidgets/Akonadi/ContactViewerDialog
/usr/include/KPim6/AkonadiContactWidgets/Akonadi/EmailAddressRequester
/usr/include/KPim6/AkonadiContactWidgets/Akonadi/EmailAddressSelectionDialog
/usr/include/KPim6/AkonadiContactWidgets/Akonadi/EmailAddressSelectionWidget
/usr/include/KPim6/AkonadiContactWidgets/Akonadi/GrantleeContactViewer
/usr/include/KPim6/AkonadiContactWidgets/Akonadi/OpenEmailAddressJob
/usr/include/KPim6/AkonadiContactWidgets/Akonadi/RecipientsEditorManager
/usr/include/KPim6/AkonadiContactWidgets/Akonadi/RecipientsPickerWidget
/usr/include/KPim6/AkonadiContactWidgets/Akonadi/SelectAddressBookDialog
/usr/include/KPim6/AkonadiContactWidgets/Akonadi/StandardContactActionManager
/usr/include/KPim6/AkonadiContactWidgets/akonadi-contacts-widgets_version.h
/usr/include/KPim6/AkonadiContactWidgets/akonadi/abstractemailaddressselectiondialog.h
/usr/include/KPim6/AkonadiContactWidgets/akonadi/addcontactjob.h
/usr/include/KPim6/AkonadiContactWidgets/akonadi/addemailaddressjob.h
/usr/include/KPim6/AkonadiContactWidgets/akonadi/addemaildisplayjob.h
/usr/include/KPim6/AkonadiContactWidgets/akonadi/akonadi-contact-widgets_export.h
/usr/include/KPim6/AkonadiContactWidgets/akonadi/contacteditor.h
/usr/include/KPim6/AkonadiContactWidgets/akonadi/contacteditordialog.h
/usr/include/KPim6/AkonadiContactWidgets/akonadi/contacteditorpageplugin.h
/usr/include/KPim6/AkonadiContactWidgets/akonadi/contactgroupeditor.h
/usr/include/KPim6/AkonadiContactWidgets/akonadi/contactgroupeditordialog.h
/usr/include/KPim6/AkonadiContactWidgets/akonadi/contactgroupviewer.h
/usr/include/KPim6/AkonadiContactWidgets/akonadi/contactviewer.h
/usr/include/KPim6/AkonadiContactWidgets/akonadi/contactviewerdialog.h
/usr/include/KPim6/AkonadiContactWidgets/akonadi/emailaddressrequester.h
/usr/include/KPim6/AkonadiContactWidgets/akonadi/emailaddressselectiondialog.h
/usr/include/KPim6/AkonadiContactWidgets/akonadi/emailaddressselectionwidget.h
/usr/include/KPim6/AkonadiContactWidgets/akonadi/grantleecontactviewer.h
/usr/include/KPim6/AkonadiContactWidgets/akonadi/openemailaddressjob.h
/usr/include/KPim6/AkonadiContactWidgets/akonadi/recipientseditormanager.h
/usr/include/KPim6/AkonadiContactWidgets/akonadi/recipientspickerwidget.h
/usr/include/KPim6/AkonadiContactWidgets/akonadi/selectaddressbookdialog.h
/usr/include/KPim6/AkonadiContactWidgets/akonadi/standardcontactactionmanager.h
/usr/lib64/cmake/KPim6AkonadiContactCore/KPim6AkonadiContactCoreConfig.cmake
/usr/lib64/cmake/KPim6AkonadiContactCore/KPim6AkonadiContactCoreConfigVersion.cmake
/usr/lib64/cmake/KPim6AkonadiContactCore/KPim6AkonadiContactCoreTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KPim6AkonadiContactCore/KPim6AkonadiContactCoreTargets.cmake
/usr/lib64/cmake/KPim6AkonadiContactWidgets/KPim6AkonadiContactWidgetsConfig.cmake
/usr/lib64/cmake/KPim6AkonadiContactWidgets/KPim6AkonadiContactWidgetsConfigVersion.cmake
/usr/lib64/cmake/KPim6AkonadiContactWidgets/KPim6AkonadiContactWidgetsTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KPim6AkonadiContactWidgets/KPim6AkonadiContactWidgetsTargets.cmake
/usr/lib64/libKPim6AkonadiContactCore.so
/usr/lib64/libKPim6AkonadiContactWidgets.so

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKPim6AkonadiContactCore.so.6.2.0
/V3/usr/lib64/libKPim6AkonadiContactWidgets.so.6.2.0
/V3/usr/lib64/qt6/plugins/akonadi_serializer_addressee.so
/V3/usr/lib64/qt6/plugins/akonadi_serializer_contactgroup.so
/usr/lib64/libKPim6AkonadiContactCore.so.6
/usr/lib64/libKPim6AkonadiContactCore.so.6.2.0
/usr/lib64/libKPim6AkonadiContactWidgets.so.6
/usr/lib64/libKPim6AkonadiContactWidgets.so.6.2.0
/usr/lib64/qt6/plugins/akonadi_serializer_addressee.so
/usr/lib64/qt6/plugins/akonadi_serializer_contactgroup.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/akonadi-contacts/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/akonadi-contacts/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
/usr/share/package-licenses/akonadi-contacts/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/akonadi-contacts/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/akonadi-contacts/cadc9e08cb956c041f87922de84b9206d9bbffb2
/usr/share/package-licenses/akonadi-contacts/e712eadfab0d2357c0f50f599ef35ee0d87534cb

%files locales -f akonadicontact6-serializer.lang -f akonadicontact6.lang
%defattr(-,root,root,-)

