%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sasr
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          'SAS' Interface

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-reticulate 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-reticulate 

%description
Provides a 'SAS' interface, through
'SASPy'(<https://sassoftware.github.io/saspy/>) and
'reticulate'(<https://rstudio.github.io/reticulate/>).  This package helps
you create 'SAS' sessions, execute 'SAS' code in remote 'SAS' servers,
retrieve execution results and log, and exchange datasets between 'SAS'
and 'R'.  It also helps you to install 'SASPy' and create a configuration
file for the connection. Please review the 'SASPy' license file as
instructed so that you comply with its separate and independent license.

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
