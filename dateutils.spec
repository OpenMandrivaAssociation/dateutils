Summary:	Command-line date and time calculation and conversion
Name:		dateutils
Version:	0.4.12
Release:	1
License:	BSD-3-Clause
Group:		File tools
URL:		http://www.fresse.org/dateutils/
Source0:	https://github.com/hroptatyr/dateutils/releases/download/v%{version}/%{name}-%{version}.tar.xz

BuildSystem:	autotools
BuildOption:	--disable-silent-rules
BuildOption:	--without-old-links

BuildRequires:	make
BuildRequires:	tzdata
Requires:	tzdata

# make install also drops LICENSE under %%{_docdir}; we ship it via %%license
%install -a
rm -f %{buildroot}%{_datadir}/doc/%{name}/LICENSE

%description
Tools for fiddling with dates and times on the command line, with a
strong focus on use cases that arise when dealing with large amounts
of financial data.

%files
%license LICENSE
%doc README.md
%{_bindir}/*
%{_mandir}/man1/*
%{_infodir}/%{name}*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.tzmcc
%{_datadir}/%{name}/locale
