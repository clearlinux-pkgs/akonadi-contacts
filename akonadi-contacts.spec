#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : akonadi-contacts
Version  : 19.08.0
Release  : 12
URL      : https://download.kde.org/stable/applications/19.08.0/src/akonadi-contacts-19.08.0.tar.xz
Source0  : https://download.kde.org/stable/applications/19.08.0/src/akonadi-contacts-19.08.0.tar.xz
Source1 : https://download.kde.org/stable/applications/19.08.0/src/akonadi-contacts-19.08.0.tar.xz.sig
Summary  : Libraries and daemons to implement Contact Management in Akonadi
Group    : Development/Tools
License  : BSD-2-Clause GPL-2.0 LGPL-2.1
Requires: akonadi-contacts-data = %{version}-%{release}
Requires: akonadi-contacts-lib = %{version}-%{release}
Requires: akonadi-contacts-license = %{version}-%{release}
Requires: akonadi-contacts-locales = %{version}-%{release}
BuildRequires : akonadi-dev
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : kcontacts-dev
BuildRequires : kmime-dev
BuildRequires : prison-dev
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
%setup -q -n akonadi-contacts-19.08.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1565917865
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags} VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1565917865
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/akonadi-contacts
cp COPYING %{buildroot}/usr/share/package-licenses/akonadi-contacts/COPYING
cp COPYING.BSD %{buildroot}/usr/share/package-licenses/akonadi-contacts/COPYING.BSD
cp COPYING.LIB %{buildroot}/usr/share/package-licenses/akonadi-contacts/COPYING.LIB
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
/usr/include/KF5/Akonadi/Contact/ContactDefaultActions
/usr/include/KF5/Akonadi/Contact/ContactEditor
/usr/include/KF5/Akonadi/Contact/ContactEditorDialog
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
/usr/include/KF5/Akonadi/Contact/SelectAddressBookDialog
/usr/include/KF5/Akonadi/Contact/StandardContactActionManager
/usr/include/KF5/Akonadi/Contact/StandardContactFormatter
/usr/include/KF5/Akonadi/Contact/StandardContactGroupFormatter
/usr/include/KF5/ContactEditor/AbstractAddressLocationWidget
/usr/include/KF5/ContactEditor/CategoriesEditAbstractWidget
/usr/include/KF5/ContactEditor/ContactEditorPagePlugin
/usr/include/KF5/akonadi/contact/abstractcontactformatter.h
/usr/include/KF5/akonadi/contact/abstractcontactgroupformatter.h
/usr/include/KF5/akonadi/contact/akonadi-contact_export.h
/usr/include/KF5/akonadi/contact/contactdefaultactions.h
/usr/include/KF5/akonadi/contact/contacteditor.h
/usr/include/KF5/akonadi/contact/contacteditordialog.h
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
/usr/include/KF5/akonadi/contact/selectaddressbookdialog.h
/usr/include/KF5/akonadi/contact/standardcontactactionmanager.h
/usr/include/KF5/akonadi/contact/standardcontactformatter.h
/usr/include/KF5/akonadi/contact/standardcontactgroupformatter.h
/usr/include/KF5/contacteditor/abstractaddresslocationwidget.h
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
/usr/lib64/libKF5AkonadiContact.so.5.12.0
/usr/lib64/libKF5ContactEditor.so.5
/usr/lib64/libKF5ContactEditor.so.5.12.0
/usr/lib64/qt5/plugins/akonadi/contacts/plugins/categorieseditwidgetplugin.so
/usr/lib64/qt5/plugins/akonadi_serializer_addressee.so
/usr/lib64/qt5/plugins/akonadi_serializer_contactgroup.so
/usr/lib64/qt5/plugins/kcm_akonadicontact_actions.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/akonadi-contacts/COPYING
/usr/share/package-licenses/akonadi-contacts/COPYING.BSD
/usr/share/package-licenses/akonadi-contacts/COPYING.LIB

%files locales -f akonadicontact5-serializer.lang -f akonadicontact5.lang -f kcm_akonadicontact_actions.lang
%defattr(-,root,root,-)

