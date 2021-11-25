# Global settings
%global major_version 5
%global minor_version 10
%global micro_version 3

Name:    crispy-doom
Version: %{major_version}.%{minor_version}.%{micro_version}
Release: 1%{?dist}
Summary: A limit-removing Doom source port based on Chocolate Doom.

License: GPLv2+
URL:     https://github.com/fabiangreffrath/crispy-doom
Source0: https://github.com/fabiangreffrath/%{name}/archive/refs/tags/%{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: make
BuildRequires: python3
BuildRequires: zlib-devel
BuildRequires: libpng-devel
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libsamplerate-devel
BuildRequires: SDL2-devel
BuildRequires: SDL2_mixer-devel
BuildRequires: SDL2_net-devel

Requires:      SDL_mixer
Requires:      SDL_net
Requires:      SDL2
Requires:      zlib
Requires:      libpng

%description
Crispy Doom is a limit-removing, enhanced-resolution Doom source port designed
based on Chocolate Doom. Its name means that internal 640x400 resolution looks
"crisp"

Crispy Doom is a friendly fork of Chocolate Doom that provides a higher display
resolution, removes the static limits of the Doom engine, and offers optional
visual, tactial, and physical enhancements while remaining entirely config file,
savegave, netplay, and demo compatible with the original.

%prep
%autosetup -p1 -n %{name}-%{name}-%{version}

# Unlike chocolate doom, we have to make things a difficult.
autoreconf -fi

%build
%configure
%make_build

%install
rm -rf %{buildroot}
%make_install DESTDIR=%{buildroot} \
  iconsdir="%{_datadir}/icons/hicolor/128x128/apps" \
  docdir="%{_pkgdocdir}"

mkdir -p %{buildroot}/%{_bindir}

# TODO: Split out into multiple rpms. To facilitate this, each file will be
#       named individually to make it easier later.
%files
# This needs to get split somehow
%doc %{_docdir}/crispy*
# Binaries
%{_bindir}/crispy-doom
%{_bindir}/crispy-doom-setup
%{_bindir}/crispy-server
%{_bindir}/crispy-heretic
%{_bindir}/crispy-heretic-setup
# Application desktop files
%{_datadir}/applications/io.github.fabiangreffrath.Setup.desktop
%{_datadir}/applications/io.github.fabiangreffrath.Doom.desktop
%{_datadir}/applications/io.github.fabiangreffrath.Heretic.desktop
%{_datadir}/applications/screensavers/io.github.fabiangreffrath.Doom_Screensaver.desktop
# icons
%{_datadir}/icons/hicolor/128x128/apps/crispy-doom.png
%{_datadir}/icons/hicolor/128x128/apps/crispy-setup.png
# metainfo
%{_datadir}/metainfo/io.github.fabiangreffrath.Doom.metainfo.xml
%{_datadir}/metainfo/io.github.fabiangreffrath.Heretic.metainfo.xml
# bash completion
%{_datadir}/bash-completion/completions/crispy-doom
%{_datadir}/bash-completion/completions/crispy-heretic
# man pages
%{_mandir}/man5/default.cfg.5.gz
%{_mandir}/man5/crispy-doom.cfg.5.gz
%{_mandir}/man5/heretic.cfg.5.gz
%{_mandir}/man5/crispy-heretic.cfg.5.gz
%{_mandir}/man6/crispy-doom.6.gz
%{_mandir}/man6/crispy-doom-setup.6.gz
%{_mandir}/man6/crispy-heretic.6.gz
%{_mandir}/man6/crispy-heretic-setup.6.gz

%changelog
* Wed Nov 24 2021 Louis Abel <tucklesepk@gmail.com> - 5.10.3-1
- Initial release for crispy doom
