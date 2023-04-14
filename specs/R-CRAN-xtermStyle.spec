%global __brp_check_rpaths %{nil}
%global packname  xtermStyle
%global packver   3.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.5
Release:          3%{?dist}%{?buildtag}
Summary:          Terminal Text Formatting Using Escape Sequences

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
Can be used for coloring output in terminals. It was developed for the
standard Ubuntu terminal but should be compatible with any terminal using
xterm or ANSI escape sequences. If run in windows, RStudio, or any other
platform not supporting such escape sequences it gracefully passes on any
output without modifying it.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
