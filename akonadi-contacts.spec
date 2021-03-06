#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : akonadi-contacts
Version  : 21.04.2
Release  : 31
URL      : https://download.kde.org/stable/release-service/21.04.2/src/akonadi-contacts-21.04.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/21.04.2/src/akonadi-contacts-21.04.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/21.04.2/src/akonadi-contacts-21.04.2.tar.xz.sig
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
BuildRequires : gpgme-dev
BuildRequires : gpgme-extras
BuildRequires : grantlee-dev
BuildRequires : grantleetheme-dev
BuildRequires : kcompletion-dev
BuildRequires : kconfig-dev
BuildRequires : kcontacts-dev
BuildRequires : ki18n-dev
BuildRequires : kiconthemes-dev
BuildRequires : kio-dev
BuildRequires : kmime-dev
BuildRequires : kservice-dev
BuildRequires : ktextwidgets-dev
BuildRequires : kwidgetsaddons-dev
BuildRequires : kxmlgui-dev
BuildRequires : libkleo-dev
BuildRequires : prison-dev
BuildRequires : qtbase-dev
BuildRequires : qtbase-dev mesa-dev

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
%setup -q -n akonadi-contacts-21.04.2
cd %{_builddir}/akonadi-contacts-21.04.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1623352593
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1623352593
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/akonadi-contacts
cp %{_builddir}/akonadi-contacts-21.04.2/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/akonadi-contacts/29fb05b49e12a380545499938c4879440bd8851e
cp %{_builddir}/akonadi-contacts-21.04.2/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/akonadi-contacts/8287b608d3fa40ef401339fd907ca1260c964123
cp %{_builddir}/akonadi-contacts-21.04.2/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/akonadi-contacts/e712eadfab0d2357c0f50f599ef35ee0d87534cb
cp %{_builddir}/akonadi-contacts-21.04.2/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/akonadi-contacts/20079e8f79713dce80ab09774505773c926afa2a
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
/usr/include/KF5/Akonadi/Contact/AbstractContactFormatter
/usr/include/KF5/Akonadi/Contact/AbstractContactGroupFormatter
/usr/include/KF5/Akonadi/Contact/AbstractEmailAddressSelectionDialog
/usr/include/KF5/Akonadi/Contact/AddContactJob
/usr/include/KF5/Akonadi/Contact/AddEmailAddressJob
/usr/include/KF5/Akonadi/Contact/AddEmailDisplayJob
/usr/include/KF5/Akonadi/Contact/ContactDefaultActions
/usr/include/KF5/Akonadi/Contact/ContactEditor
/usr/include/KF5/Akonadi/Contact/ContactEditorDialog
/usr/include/KF5/Akonadi/Contact/ContactGrantleeWrapper
/usr/include/KF5/Akonadi/Contact/ContactGroupEditor
/usr/include/KF5/Akonadi/Contact/ContactGroupEditorDialog
/usr/include/KF5/Akonadi/Contact/ContactGroupExpandJob
/usr/include/KF5/Akonadi/Contact/ContactGroupSearchJob
/usr/include/KF5/Akonadi/Contact/ContactGroupViewer
/usr/include/KF5/Akonadi/Contact/ContactGroupViewerDialog
/usr/include/KF5/Akonadi/Contact/ContactParts
/usr/include/KF5/Akonadi/Contact/ContactSearchJob
/usr/include/KF5/Akonadi/Contact/ContactViewer
/usr/include/KF5/Akonadi/Contact/ContactViewerDialog
/usr/include/KF5/Akonadi/Contact/ContactsFilterProxyModel
/usr/include/KF5/Akonadi/Contact/ContactsTreeModel
/usr/include/KF5/Akonadi/Contact/EmailAddressRequester
/usr/include/KF5/Akonadi/Contact/EmailAddressSelection
/usr/include/KF5/Akonadi/Contact/EmailAddressSelectionDialog
/usr/include/KF5/Akonadi/Contact/EmailAddressSelectionModel
/usr/include/KF5/Akonadi/Contact/EmailAddressSelectionWidget
/usr/include/KF5/Akonadi/Contact/GrantleeContactFormatter
/usr/include/KF5/Akonadi/Contact/GrantleeContactGroupFormatter
/usr/include/KF5/Akonadi/Contact/GrantleeContactViewer
/usr/include/KF5/Akonadi/Contact/GrantleePrint
/usr/include/KF5/Akonadi/Contact/OpenEmailAddressJob
/usr/include/KF5/Akonadi/Contact/RecipientsEditorManager
/usr/include/KF5/Akonadi/Contact/RecipientsPickerWidget
/usr/include/KF5/Akonadi/Contact/SelectAddressBookDialog
/usr/include/KF5/Akonadi/Contact/StandardContactActionManager
/usr/include/KF5/Akonadi/Contact/StandardContactFormatter
/usr/include/KF5/Akonadi/Contact/StandardContactGroupFormatter
/usr/include/KF5/ContactEditor/CategoriesEditAbstractWidget
/usr/include/KF5/ContactEditor/ContactEditorPagePlugin
/usr/include/KF5/akonadi/contact/abstractcontactformatter.h
/usr/include/KF5/akonadi/contact/abstractcontactgroupformatter.h
/usr/include/KF5/akonadi/contact/abstractemailaddressselectiondialog.h
/usr/include/KF5/akonadi/contact/addcontactjob.h
/usr/include/KF5/akonadi/contact/addemailaddressjob.h
/usr/include/KF5/akonadi/contact/addemaildisplayjob.h
/usr/include/KF5/akonadi/contact/akonadi-contact_export.h
/usr/include/KF5/akonadi/contact/contactdefaultactions.h
/usr/include/KF5/akonadi/contact/contacteditor.h
/usr/include/KF5/akonadi/contact/contacteditordialog.h
/usr/include/KF5/akonadi/contact/contactgrantleewrapper.h
/usr/include/KF5/akonadi/contact/contactgroupeditor.h
/usr/include/KF5/akonadi/contact/contactgroupeditordialog.h
/usr/include/KF5/akonadi/contact/contactgroupexpandjob.h
/usr/include/KF5/akonadi/contact/contactgroupsearchjob.h
/usr/include/KF5/akonadi/contact/contactgroupviewer.h
/usr/include/KF5/akonadi/contact/contactgroupviewerdialog.h
/usr/include/KF5/akonadi/contact/contactparts.h
/usr/include/KF5/akonadi/contact/contactsearchjob.h
/usr/include/KF5/akonadi/contact/contactsfilterproxymodel.h
/usr/include/KF5/akonadi/contact/contactstreemodel.h
/usr/include/KF5/akonadi/contact/contactviewer.h
/usr/include/KF5/akonadi/contact/contactviewerdialog.h
/usr/include/KF5/akonadi/contact/emailaddressrequester.h
/usr/include/KF5/akonadi/contact/emailaddressselection.h
/usr/include/KF5/akonadi/contact/emailaddressselectiondialog.h
/usr/include/KF5/akonadi/contact/emailaddressselectionmodel.h
/usr/include/KF5/akonadi/contact/emailaddressselectionwidget.h
/usr/include/KF5/akonadi/contact/grantleecontactformatter.h
/usr/include/KF5/akonadi/contact/grantleecontactgroupformatter.h
/usr/include/KF5/akonadi/contact/grantleecontactviewer.h
/usr/include/KF5/akonadi/contact/grantleeprint.h
/usr/include/KF5/akonadi/contact/openemailaddressjob.h
/usr/include/KF5/akonadi/contact/recipientseditormanager.h
/usr/include/KF5/akonadi/contact/recipientspickerwidget.h
/usr/include/KF5/akonadi/contact/selectaddressbookdialog.h
/usr/include/KF5/akonadi/contact/standardcontactactionmanager.h
/usr/include/KF5/akonadi/contact/standardcontactformatter.h
/usr/include/KF5/akonadi/contact/standardcontactgroupformatter.h
/usr/include/KF5/contacteditor/categorieseditabstractwidget.h
/usr/include/KF5/contacteditor/contacteditor_export.h
/usr/include/KF5/contacteditor/contacteditorpageplugin.h
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
/usr/lib64/libKF5AkonadiContact.so.5.17.2
/usr/lib64/libKF5ContactEditor.so.5
/usr/lib64/libKF5ContactEditor.so.5.17.2
/usr/lib64/qt5/plugins/akonadi/contacts/plugins/categorieseditwidgetplugin.so
/usr/lib64/qt5/plugins/akonadi_serializer_addressee.so
/usr/lib64/qt5/plugins/akonadi_serializer_contactgroup.so
/usr/lib64/qt5/plugins/kcm_akonadicontact_actions.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/akonadi-contacts/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/akonadi-contacts/29fb05b49e12a380545499938c4879440bd8851e
/usr/share/package-licenses/akonadi-contacts/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/akonadi-contacts/e712eadfab0d2357c0f50f599ef35ee0d87534cb

%files locales -f akonadicontact5-serializer.lang -f akonadicontact5.lang -f kcm_akonadicontact_actions.lang
%defattr(-,root,root,-)

