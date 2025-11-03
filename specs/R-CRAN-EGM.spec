%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  EGM
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Intracardiac Electrograms

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildRequires:    R-CRAN-data.table >= 1.15.0
BuildRequires:    R-CRAN-vctrs >= 0.5.0
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-signal 
BuildRequires:    R-CRAN-cpp11 
Requires:         R-CRAN-data.table >= 1.15.0
Requires:         R-CRAN-vctrs >= 0.5.0
Requires:         R-stats 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rlang 
Requires:         R-utils 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-signal 

%description
A system for importing electrophysiological signal, based on the 'Waveform
Database (WFDB)' software package, written by Moody et al 2022
<doi:10.13026/gjvw-1m31>. A R-based system to utilize 'WFDB' functions for
reading and writing signal data, as well as functions for visualization
and analysis are provided. A stable and broadly compatible class for
working with signal data, supporting the reading in of cardiac
electrophysiological files such as intracardiac electrograms, is
introduced.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
