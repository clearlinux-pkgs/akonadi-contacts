#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v3
# autospec commit: c1050fe
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : akonadi-contacts
Version  : 23.08.3
Release  : 63
URL      : https://download.kde.org/stable/release-service/23.08.3/src/akonadi-contacts-23.08.3.tar.xz
Source0  : https://download.kde.org/stable/release-service/23.08.3/src/akonadi-contacts-23.08.3.tar.xz
Source1  : https://download.kde.org/stable/release-service/23.08.3/src/akonadi-contacts-23.08.3.tar.xz.sig
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
BuildRequires : grantlee-dev
BuildRequires : grantleetheme-dev
BuildRequires : kcontacts-dev
BuildRequires : kmime-dev
BuildRequires : prison-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
SPDX-License-Identifier: CC0-1.0

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
%setup -q -n akonadi-contacts-23.08.3
cd %{_builddir}/akonadi-contacts-23.08.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1701930994
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
%cmake ..
make  %{?_smp_mflags}
popd
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
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake ..
make  %{?_smp_mflags}
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
export SOURCE_DATE_EPOCH=1701930994
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/akonadi-contacts
cp %{_builddir}/akonadi-contacts-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/akonadi-contacts/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/akonadi-contacts-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/akonadi-contacts/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/akonadi-contacts-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/akonadi-contacts/e712eadfab0d2357c0f50f599ef35ee0d87534cb || :
cp %{_builddir}/akonadi-contacts-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/akonadi-contacts/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/akonadi-contacts-%{version}/README.md.license %{buildroot}/usr/share/package-licenses/akonadi-contacts/cadc9e08cb956c041f87922de84b9206d9bbffb2 || :
cp %{_builddir}/akonadi-contacts-%{version}/metainfo.yaml.license %{buildroot}/usr/share/package-licenses/akonadi-contacts/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4 || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
%find_lang akonadicontact5-serializer
%find_lang akonadicontact5
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/akonadi/plugins/serializer/akonadi_serializer_addressee.desktop
/usr/share/akonadi/plugins/serializer/akonadi_serializer_contactgroup.desktop
/usr/share/kf5/akonadi/contact/data/zone.tab
/usr/share/kf5/akonadi/contact/pics/world.jpg
/usr/share/qlogging-categories5/akonadi-contacts.categories
/usr/share/qlogging-categories5/akonadi-contacts.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KPim5/AkonadiContact/Akonadi/AbstractContactFormatter
/usr/include/KPim5/AkonadiContact/Akonadi/AbstractContactGroupFormatter
/usr/include/KPim5/AkonadiContact/Akonadi/AbstractEmailAddressSelectionDialog
/usr/include/KPim5/AkonadiContact/Akonadi/ContactGrantleeWrapper
/usr/include/KPim5/AkonadiContact/Akonadi/ContactGroupEditor
/usr/include/KPim5/AkonadiContact/Akonadi/ContactGroupEditorDialog
/usr/include/KPim5/AkonadiContact/Akonadi/ContactGroupExpandJob
/usr/include/KPim5/AkonadiContact/Akonadi/ContactGroupSearchJob
/usr/include/KPim5/AkonadiContact/Akonadi/ContactParts
/usr/include/KPim5/AkonadiContact/Akonadi/ContactSearchJob
/usr/include/KPim5/AkonadiContact/Akonadi/ContactsFilterProxyModel
/usr/include/KPim5/AkonadiContact/Akonadi/ContactsTreeModel
/usr/include/KPim5/AkonadiContact/Akonadi/EmailAddressRequester
/usr/include/KPim5/AkonadiContact/Akonadi/EmailAddressSelection
/usr/include/KPim5/AkonadiContact/Akonadi/EmailAddressSelectionDialog
/usr/include/KPim5/AkonadiContact/Akonadi/EmailAddressSelectionModel
/usr/include/KPim5/AkonadiContact/Akonadi/EmailAddressSelectionWidget
/usr/include/KPim5/AkonadiContact/Akonadi/GrantleeContactFormatter
/usr/include/KPim5/AkonadiContact/Akonadi/GrantleeContactGroupFormatter
/usr/include/KPim5/AkonadiContact/Akonadi/GrantleePrint
/usr/include/KPim5/AkonadiContact/Akonadi/RecipientsEditorManager
/usr/include/KPim5/AkonadiContact/Akonadi/RecipientsPickerWidget
/usr/include/KPim5/AkonadiContact/Akonadi/StandardContactFormatter
/usr/include/KPim5/AkonadiContact/Akonadi/StandardContactGroupFormatter
/usr/include/KPim5/AkonadiContact/akonadi-contact_version.h
/usr/include/KPim5/AkonadiContact/akonadi/abstractcontactformatter.h
/usr/include/KPim5/AkonadiContact/akonadi/abstractcontactgroupformatter.h
/usr/include/KPim5/AkonadiContact/akonadi/abstractemailaddressselectiondialog.h
/usr/include/KPim5/AkonadiContact/akonadi/akonadi-contact_export.h
/usr/include/KPim5/AkonadiContact/akonadi/contactgrantleewrapper.h
/usr/include/KPim5/AkonadiContact/akonadi/contactgroupeditor.h
/usr/include/KPim5/AkonadiContact/akonadi/contactgroupeditordialog.h
/usr/include/KPim5/AkonadiContact/akonadi/contactgroupexpandjob.h
/usr/include/KPim5/AkonadiContact/akonadi/contactgroupsearchjob.h
/usr/include/KPim5/AkonadiContact/akonadi/contactparts.h
/usr/include/KPim5/AkonadiContact/akonadi/contactsearchjob.h
/usr/include/KPim5/AkonadiContact/akonadi/contactsfilterproxymodel.h
/usr/include/KPim5/AkonadiContact/akonadi/contactstreemodel.h
/usr/include/KPim5/AkonadiContact/akonadi/emailaddressrequester.h
/usr/include/KPim5/AkonadiContact/akonadi/emailaddressselection.h
/usr/include/KPim5/AkonadiContact/akonadi/emailaddressselectiondialog.h
/usr/include/KPim5/AkonadiContact/akonadi/emailaddressselectionmodel.h
/usr/include/KPim5/AkonadiContact/akonadi/emailaddressselectionwidget.h
/usr/include/KPim5/AkonadiContact/akonadi/grantleecontactformatter.h
/usr/include/KPim5/AkonadiContact/akonadi/grantleecontactgroupformatter.h
/usr/include/KPim5/AkonadiContact/akonadi/grantleeprint.h
/usr/include/KPim5/AkonadiContact/akonadi/recipientseditormanager.h
/usr/include/KPim5/AkonadiContact/akonadi/recipientspickerwidget.h
/usr/include/KPim5/AkonadiContact/akonadi/standardcontactformatter.h
/usr/include/KPim5/AkonadiContact/akonadi/standardcontactgroupformatter.h
/usr/include/KPim5/AkonadiContactEditor/Akonadi/AddContactJob
/usr/include/KPim5/AkonadiContactEditor/Akonadi/AddEmailAddressJob
/usr/include/KPim5/AkonadiContactEditor/Akonadi/AddEmailDisplayJob
/usr/include/KPim5/AkonadiContactEditor/Akonadi/ContactEditor
/usr/include/KPim5/AkonadiContactEditor/Akonadi/ContactEditorDialog
/usr/include/KPim5/AkonadiContactEditor/Akonadi/ContactEditorPagePlugin
/usr/include/KPim5/AkonadiContactEditor/Akonadi/ContactGroupViewer
/usr/include/KPim5/AkonadiContactEditor/Akonadi/ContactViewer
/usr/include/KPim5/AkonadiContactEditor/Akonadi/ContactViewerDialog
/usr/include/KPim5/AkonadiContactEditor/Akonadi/GrantleeContactViewer
/usr/include/KPim5/AkonadiContactEditor/Akonadi/OpenEmailAddressJob
/usr/include/KPim5/AkonadiContactEditor/Akonadi/SelectAddressBookDialog
/usr/include/KPim5/AkonadiContactEditor/Akonadi/StandardContactActionManager
/usr/include/KPim5/AkonadiContactEditor/akonadi-contact-editor_version.h
/usr/include/KPim5/AkonadiContactEditor/akonadi/addcontactjob.h
/usr/include/KPim5/AkonadiContactEditor/akonadi/addemailaddressjob.h
/usr/include/KPim5/AkonadiContactEditor/akonadi/addemaildisplayjob.h
/usr/include/KPim5/AkonadiContactEditor/akonadi/contacteditor.h
/usr/include/KPim5/AkonadiContactEditor/akonadi/contacteditor_export.h
/usr/include/KPim5/AkonadiContactEditor/akonadi/contacteditordialog.h
/usr/include/KPim5/AkonadiContactEditor/akonadi/contacteditorpageplugin.h
/usr/include/KPim5/AkonadiContactEditor/akonadi/contactgroupviewer.h
/usr/include/KPim5/AkonadiContactEditor/akonadi/contactviewer.h
/usr/include/KPim5/AkonadiContactEditor/akonadi/contactviewerdialog.h
/usr/include/KPim5/AkonadiContactEditor/akonadi/grantleecontactviewer.h
/usr/include/KPim5/AkonadiContactEditor/akonadi/openemailaddressjob.h
/usr/include/KPim5/AkonadiContactEditor/akonadi/selectaddressbookdialog.h
/usr/include/KPim5/AkonadiContactEditor/akonadi/standardcontactactionmanager.h
/usr/lib64/cmake/KF5AkonadiContactEditor/KF5ContactEditorConfig.cmake
/usr/lib64/cmake/KF5AkonadiContactEditor/KF5ContactEditorConfigVersion.cmake
/usr/lib64/cmake/KPim5AkonadiContact/KPim5AkonadiContactConfig.cmake
/usr/lib64/cmake/KPim5AkonadiContact/KPim5AkonadiContactConfigVersion.cmake
/usr/lib64/cmake/KPim5AkonadiContact/KPim5AkonadiContactTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KPim5AkonadiContact/KPim5AkonadiContactTargets.cmake
/usr/lib64/cmake/KPim5ContactEditor/KPim5ContactEditorConfig.cmake
/usr/lib64/cmake/KPim5ContactEditor/KPim5ContactEditorConfigVersion.cmake
/usr/lib64/cmake/KPim5ContactEditor/KPim5ContactEditorTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KPim5ContactEditor/KPim5ContactEditorTargets.cmake
/usr/lib64/libKPim5AkonadiContact.so
/usr/lib64/libKPim5ContactEditor.so
/usr/lib64/qt5/mkspecs/modules/qt_AkonadiContact.pri
/usr/lib64/qt5/mkspecs/modules/qt_ContactEditor.pri

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKPim5AkonadiContact.so.5.24.3
/V3/usr/lib64/libKPim5ContactEditor.so.5.24.3
/V3/usr/lib64/qt5/plugins/akonadi_serializer_addressee.so
/V3/usr/lib64/qt5/plugins/akonadi_serializer_contactgroup.so
/usr/lib64/libKPim5AkonadiContact.so.5
/usr/lib64/libKPim5AkonadiContact.so.5.24.3
/usr/lib64/libKPim5ContactEditor.so.5
/usr/lib64/libKPim5ContactEditor.so.5.24.3
/usr/lib64/qt5/plugins/akonadi_serializer_addressee.so
/usr/lib64/qt5/plugins/akonadi_serializer_contactgroup.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/akonadi-contacts/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/akonadi-contacts/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
/usr/share/package-licenses/akonadi-contacts/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/akonadi-contacts/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/akonadi-contacts/cadc9e08cb956c041f87922de84b9206d9bbffb2
/usr/share/package-licenses/akonadi-contacts/e712eadfab0d2357c0f50f599ef35ee0d87534cb

%files locales -f akonadicontact5-serializer.lang -f akonadicontact5.lang
%defattr(-,root,root,-)

