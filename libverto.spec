Name:           libverto
Version:        0.3.1
Release:        6
Summary:        Main loop abstraction library
License:        MIT
URL:            https://github.com/latchset/libverto
Source0:        https://github.com/latchset/libverto/releases/download/%{version}/%{name}-%{version}.tar.gz

Patch6000:	backport-re-order-pkgconfig-for-expected-dependencies.patch
Patch6001:	backport-fix-use-after-free-in-verto_free.patch
Patch6002:	backport-fix-use-after-free-in-verto_reinitialize.patch
Patch6003:	backport-fix-bashisms-in-configure.ac.patch

BuildRequires:  autoconf automake libtool glib2-devel
BuildRequires:  libevent-devel libev-devel git

Obsoletes:      libverto-tevent < 0.3.0-2
Obsoletes:      libverto-tevent-devel < 0.3.0-2


Provides:  %{name}-glib
Obsoletes: %{name}-glib

Provides:  %{name}-module-base = %{version}-%{release}
Provides:  %{name}-libevent 
Obsoletes: %{name}-libevent

Provides:  %{name}-libev
Obsoletes: %{name}-libev

%description
libverto exists to solve an important problem: many applications and libraries
are unable to write asynchronous code because they are unable to pick an event
loop. This is particularly true of libraries who want to be useful to many
applications who use loops that do not integrate with one another or which
use home-grown loops. libverto provides a loop-neutral async api which allows
the library to expose asynchronous interfaces and offload the choice of the
main loop to the application.

%package   devel
Summary:   Development files for %{name}
Requires:  %{name} = %{version}-%{release}
Requires:  pkgconfig

Provides:  %{name}-glib-devel
Obsoletes: %{name}-glib-devel

Provides:  %{name}-libevent-devel
Obsoletes: %{name}-libevent-devel

Provides:  %{name}-libev-devel
Obsoletes: %{name}-libev-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n %{name}-%{version} -p1 -S git

%build
autoreconf -fiv
%configure --disable-static
%make_build

%install
rm -rf  %{buildroot}
%make_install
find  %{buildroot} -name '*.la' -exec rm -f {} ';'

%ldconfig_scriptlets

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/%{name}.so.*
%{_libdir}/%{name}-glib.so.*
%{_libdir}/%{name}-libevent.so.*
%{_libdir}/%{name}-libev.so.*

%files devel
%{_includedir}/verto.h
%{_includedir}/verto-module.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/verto-glib.h
%{_libdir}/%{name}-glib.so
%{_libdir}/pkgconfig/%{name}-glib.pc
%{_includedir}/verto-libevent.h
%{_libdir}/%{name}-libevent.so
%{_libdir}/pkgconfig/%{name}-libevent.pc
%{_includedir}/verto-libev.h
%{_libdir}/%{name}-libev.so
%{_libdir}/pkgconfig/%{name}-libev.pc

%changelog
* Tue Mar 08 2022 hanxinke <hanxinke@huawei.com> - 0.3.1-6
- fix bashisms in configure.ac

* Mon Mar 07 2022 hanxinke <hanxinke@huawei.com> - 0.3.1-5
- fix use after free in verto_reinitialize

* Fri Mar 04 2022 hanxinke <hanxinke@huawei.com> - 0.3.1-4
- fix use after free in verto_free

* Thu Mar 03 2022 hanxinke <hanxinke@huawei.com> - 0.3.1-3
- fix broken pkgconfig files

* Mon Oct 21 2019 shenyangyang <shenyangyang4@huawei.com> - 0.3.1-2
- Type:NA
- ID:NA
- SUG:NA
- DESC:remove libev.so* that should provided by libev

* Thu Sep 5 2019 openEuler Buildteam <buildteam@openeuler.org> - 0.3.1-1
- Package init
