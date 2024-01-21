%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  procs
%global packver   1.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Recreates Some 'SAS®' Procedures in 'R'

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-sasLM >= 0.9.9
BuildRequires:    R-CRAN-common 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-fmtr 
BuildRequires:    R-CRAN-reporter 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-sasLM >= 0.9.9
Requires:         R-CRAN-common 
Requires:         R-utils 
Requires:         R-CRAN-fmtr 
Requires:         R-CRAN-reporter 
Requires:         R-stats 
Requires:         R-CRAN-tibble 

%description
Contains functions to simulate the most commonly used 'SAS®' procedures.
Specifically, the package aims to simulate the functionality of 'proc
freq', 'proc means', 'proc ttest', 'proc transpose', 'proc sort', and
'proc print'. The simulation will include recreating all statistics with
the highest fidelity possible.

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
