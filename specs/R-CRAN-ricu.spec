%global __brp_check_rpaths %{nil}
%global packname  ricu
%global packver   0.5.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.2
Release:          1%{?dist}%{?buildtag}
Summary:          Intensive Care Unit Data with R

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 2.1.0
BuildRequires:    R-CRAN-prt >= 0.1.2
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-fst 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-backports 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-vctrs 
BuildRequires:    R-CRAN-fansi 
BuildRequires:    R-CRAN-openssl 
BuildRequires:    R-utils 
Requires:         R-CRAN-cli >= 2.1.0
Requires:         R-CRAN-prt >= 0.1.2
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-fst 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-jsonlite 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-backports 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-vctrs 
Requires:         R-CRAN-fansi 
Requires:         R-CRAN-openssl 
Requires:         R-utils 

%description
Focused on (but not exclusive to) data sets hosted on PhysioNet
(<https://physionet.org>), 'ricu' provides utilities for download, setup
and access of intensive care unit (ICU) data sets. In addition to
functions for running arbitrary queries against available data sets, a
system for defining clinical concepts and encoding their representations
in tabular ICU data is presented.

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
