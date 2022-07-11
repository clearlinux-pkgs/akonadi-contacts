#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : akonadi-contacts
Version  : 22.04.3
Release  : 43
URL      : https://download.kde.org/stable/release-service/22.04.3/src/akonadi-contacts-22.04.3.tar.xz
Source0  : https://download.kde.org/stable/release-service/22.04.3/src/akonadi-contacts-22.04.3.tar.xz
Source1  : https://download.kde.org/stable/release-service/22.04.3/src/akonadi-contacts-22.04.3.tar.xz.sig
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
BuildRequires : kcmutils-dev
BuildRequires : kcompletion-dev
BuildRequires : kconfig-dev
BuildRequires : kcontacts-dev
BuildRequires : kcoreaddons-dev
BuildRequires : ki18n-dev
BuildRequires : kiconthemes-dev
BuildRequires : kio-dev
BuildRequires : kmime-dev
BuildRequires : kservice-dev
BuildRequires : ktextwidgets-dev
BuildRequires : kwidgetsaddons-dev
BuildRequires : kxmlgui-dev
BuildRequires : prison-dev

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
%setup -q -n akonadi-contacts-22.04.3
cd %{_builddir}/akonadi-contacts-22.04.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1657582569
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1657582569
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/akonadi-contacts
cp %{_builddir}/akonadi-contacts-22.04.3/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/akonadi-contacts/c085897bc39e05746ffd2d889a6e84ff1b7ae2d9
cp %{_builddir}/akonadi-contacts-22.04.3/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/akonadi-contacts/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
cp %{_builddir}/akonadi-contacts-22.04.3/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/akonadi-contacts/8287b608d3fa40ef401339fd907ca1260c964123
cp %{_builddir}/akonadi-contacts-22.04.3/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/akonadi-contacts/e712eadfab0d2357c0f50f599ef35ee0d87534cb
cp %{_builddir}/akonadi-contacts-22.04.3/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/akonadi-contacts/20079e8f79713dce80ab09774505773c926afa2a
cp %{_builddir}/akonadi-contacts-22.04.3/README.md.license %{buildroot}/usr/share/package-licenses/akonadi-contacts/cadc9e08cb956c041f87922de84b9206d9bbffb2
cp %{_builddir}/akonadi-contacts-22.04.3/metainfo.yaml.license %{buildroot}/usr/share/package-licenses/akonadi-contacts/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
pushd clr-build
%make_install
popd
%find_lang akonadicontact5-serializer
%find_lang akonadicontact5
%find_lang kcm_akonadicontact_actions

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/akonadi/plugins/serializer/akonadi_serializer_addressee.desktop
/usr/share/akonadi/plugins/serializer/akonadi_serializer_contactgroup.desktop
/usr/share/kf5/akonadi/contact/data/zone.tab
/usr/share/kf5/akonadi/contact/pics/world.jpg
/usr/share/kservices5/akonadicontact_actions.desktop
/usr/share/qlogging-categories5/akonadi-contacts.categories
/usr/share/qlogging-categories5/akonadi-contacts.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/AkonadiContact/Akonadi/AbstractContactFormatter
/usr/include/KF5/AkonadiContact/Akonadi/AbstractContactGroupFormatter
/usr/include/KF5/AkonadiContact/Akonadi/AbstractEmailAddressSelectionDialog
/usr/include/KF5/AkonadiContact/Akonadi/AddContactJob
/usr/include/KF5/AkonadiContact/Akonadi/AddEmailAddressJob
/usr/include/KF5/AkonadiContact/Akonadi/AddEmailDisplayJob
/usr/include/KF5/AkonadiContact/Akonadi/ContactDefaultActions
/usr/include/KF5/AkonadiContact/Akonadi/ContactEditor
/usr/include/KF5/AkonadiContact/Akonadi/ContactEditorDialog
/usr/include/KF5/AkonadiContact/Akonadi/ContactGrantleeWrapper
/usr/include/KF5/AkonadiContact/Akonadi/ContactGroupEditor
/usr/include/KF5/AkonadiContact/Akonadi/ContactGroupEditorDialog
/usr/include/KF5/AkonadiContact/Akonadi/ContactGroupExpandJob
/usr/include/KF5/AkonadiContact/Akonadi/ContactGroupSearchJob
/usr/include/KF5/AkonadiContact/Akonadi/ContactGroupViewer
/usr/include/KF5/AkonadiContact/Akonadi/ContactParts
/usr/include/KF5/AkonadiContact/Akonadi/ContactSearchJob
/usr/include/KF5/AkonadiContact/Akonadi/ContactViewer
/usr/include/KF5/AkonadiContact/Akonadi/ContactViewerDialog
/usr/include/KF5/AkonadiContact/Akonadi/ContactsFilterProxyModel
/usr/include/KF5/AkonadiContact/Akonadi/ContactsTreeModel
/usr/include/KF5/AkonadiContact/Akonadi/EmailAddressRequester
/usr/include/KF5/AkonadiContact/Akonadi/EmailAddressSelection
/usr/include/KF5/AkonadiContact/Akonadi/EmailAddressSelectionDialog
/usr/include/KF5/AkonadiContact/Akonadi/EmailAddressSelectionModel
/usr/include/KF5/AkonadiContact/Akonadi/EmailAddressSelectionWidget
/usr/include/KF5/AkonadiContact/Akonadi/GrantleeContactFormatter
/usr/include/KF5/AkonadiContact/Akonadi/GrantleeContactGroupFormatter
/usr/include/KF5/AkonadiContact/Akonadi/GrantleeContactViewer
/usr/include/KF5/AkonadiContact/Akonadi/GrantleePrint
/usr/include/KF5/AkonadiContact/Akonadi/OpenEmailAddressJob
/usr/include/KF5/AkonadiContact/Akonadi/RecipientsEditorManager
/usr/include/KF5/AkonadiContact/Akonadi/RecipientsPickerWidget
/usr/include/KF5/AkonadiContact/Akonadi/SelectAddressBookDialog
/usr/include/KF5/AkonadiContact/Akonadi/StandardContactActionManager
/usr/include/KF5/AkonadiContact/Akonadi/StandardContactFormatter
/usr/include/KF5/AkonadiContact/Akonadi/StandardContactGroupFormatter
/usr/include/KF5/AkonadiContact/akonadi-contact_version.h
/usr/include/KF5/AkonadiContact/akonadi/abstractcontactformatter.h
/usr/include/KF5/AkonadiContact/akonadi/abstractcontactgroupformatter.h
/usr/include/KF5/AkonadiContact/akonadi/abstractemailaddressselectiondialog.h
/usr/include/KF5/AkonadiContact/akonadi/addcontactjob.h
/usr/include/KF5/AkonadiContact/akonadi/addemailaddressjob.h
/usr/include/KF5/AkonadiContact/akonadi/addemaildisplayjob.h
/usr/include/KF5/AkonadiContact/akonadi/akonadi-contact_export.h
/usr/include/KF5/AkonadiContact/akonadi/contactdefaultactions.h
/usr/include/KF5/AkonadiContact/akonadi/contacteditor.h
/usr/include/KF5/AkonadiContact/akonadi/contacteditordialog.h
/usr/include/KF5/AkonadiContact/akonadi/contactgrantleewrapper.h
/usr/include/KF5/AkonadiContact/akonadi/contactgroupeditor.h
/usr/include/KF5/AkonadiContact/akonadi/contactgroupeditordialog.h
/usr/include/KF5/AkonadiContact/akonadi/contactgroupexpandjob.h
/usr/include/KF5/AkonadiContact/akonadi/contactgroupsearchjob.h
/usr/include/KF5/AkonadiContact/akonadi/contactgroupviewer.h
/usr/include/KF5/AkonadiContact/akonadi/contactparts.h
/usr/include/KF5/AkonadiContact/akonadi/contactsearchjob.h
/usr/include/KF5/AkonadiContact/akonadi/contactsfilterproxymodel.h
/usr/include/KF5/AkonadiContact/akonadi/contactstreemodel.h
/usr/include/KF5/AkonadiContact/akonadi/contactviewer.h
/usr/include/KF5/AkonadiContact/akonadi/contactviewerdialog.h
/usr/include/KF5/AkonadiContact/akonadi/emailaddressrequester.h
/usr/include/KF5/AkonadiContact/akonadi/emailaddressselection.h
/usr/include/KF5/AkonadiContact/akonadi/emailaddressselectiondialog.h
/usr/include/KF5/AkonadiContact/akonadi/emailaddressselectionmodel.h
/usr/include/KF5/AkonadiContact/akonadi/emailaddressselectionwidget.h
/usr/include/KF5/AkonadiContact/akonadi/grantleecontactformatter.h
/usr/include/KF5/AkonadiContact/akonadi/grantleecontactgroupformatter.h
/usr/include/KF5/AkonadiContact/akonadi/grantleecontactviewer.h
/usr/include/KF5/AkonadiContact/akonadi/grantleeprint.h
/usr/include/KF5/AkonadiContact/akonadi/openemailaddressjob.h
/usr/include/KF5/AkonadiContact/akonadi/recipientseditormanager.h
/usr/include/KF5/AkonadiContact/akonadi/recipientspickerwidget.h
/usr/include/KF5/AkonadiContact/akonadi/selectaddressbookdialog.h
/usr/include/KF5/AkonadiContact/akonadi/standardcontactactionmanager.h
/usr/include/KF5/AkonadiContact/akonadi/standardcontactformatter.h
/usr/include/KF5/AkonadiContact/akonadi/standardcontactgroupformatter.h
/usr/include/KF5/AkonadiContactEditor/Akonadi/CategoriesEditAbstractWidget
/usr/include/KF5/AkonadiContactEditor/Akonadi/ContactEditorPagePlugin
/usr/include/KF5/AkonadiContactEditor/akonadi-contact-editor_version.h
/usr/include/KF5/AkonadiContactEditor/akonadi/categorieseditabstractwidget.h
/usr/include/KF5/AkonadiContactEditor/akonadi/contacteditor_export.h
/usr/include/KF5/AkonadiContactEditor/akonadi/contacteditorpageplugin.h
/usr/lib64/cmake/KF5AkonadiContact/KF5AkonadiContactConfig.cmake
/usr/lib64/cmake/KF5AkonadiContact/KF5AkonadiContactConfigVersion.cmake
/usr/lib64/cmake/KF5AkonadiContact/KF5AkonadiContactTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5AkonadiContact/KF5AkonadiContactTargets.cmake
/usr/lib64/cmake/KF5ContactEditor/KF5ContactEditorConfig.cmake
/usr/lib64/cmake/KF5ContactEditor/KF5ContactEditorConfigVersion.cmake
/usr/lib64/cmake/KF5ContactEditor/KF5ContactEditorTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5ContactEditor/KF5ContactEditorTargets.cmake
/usr/lib64/libKF5AkonadiContact.so
/usr/lib64/libKF5ContactEditor.so
/usr/lib64/qt5/mkspecs/modules/qt_AkonadiContact.pri
/usr/lib64/qt5/mkspecs/modules/qt_ContactEditor.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5AkonadiContact.so.5
/usr/lib64/libKF5AkonadiContact.so.5.20.3
/usr/lib64/libKF5ContactEditor.so.5
/usr/lib64/libKF5ContactEditor.so.5.20.3
/usr/lib64/qt5/plugins/akonadi/contacts/plugins/categorieseditwidgetplugin.so
/usr/lib64/qt5/plugins/akonadi_serializer_addressee.so
/usr/lib64/qt5/plugins/akonadi_serializer_contactgroup.so
/usr/lib64/qt5/plugins/pim/kcms/kaddressbook/kcm_akonadicontact_actions.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/akonadi-contacts/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/akonadi-contacts/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
/usr/share/package-licenses/akonadi-contacts/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/akonadi-contacts/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/akonadi-contacts/c085897bc39e05746ffd2d889a6e84ff1b7ae2d9
/usr/share/package-licenses/akonadi-contacts/cadc9e08cb956c041f87922de84b9206d9bbffb2
/usr/share/package-licenses/akonadi-contacts/e712eadfab0d2357c0f50f599ef35ee0d87534cb

%files locales -f akonadicontact5-serializer.lang -f akonadicontact5.lang -f kcm_akonadicontact_actions.lang
%defattr(-,root,root,-)

