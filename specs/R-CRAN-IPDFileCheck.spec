%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  IPDFileCheck
%global packver   0.8.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.1
Release:          1%{?dist}%{?buildtag}
Summary:          Basic Functions to Check Readability, Consistency, and Content of an Individual Participant Data File

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-testthat 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-eeptools 
BuildRequires:    R-CRAN-hash 
BuildRequires:    R-CRAN-kableExtra 
BuildRequires:    R-CRAN-gtsummary 
BuildRequires:    R-CRAN-effsize 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyselect 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-testthat 
Requires:         R-CRAN-lubridate 
Requires:         R-methods 
Requires:         R-CRAN-eeptools 
Requires:         R-CRAN-hash 
Requires:         R-CRAN-kableExtra 
Requires:         R-CRAN-gtsummary 
Requires:         R-CRAN-effsize 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyselect 

%description
Basic checks needed with an individual level participant data from
randomised controlled trial. This checks files for existence, read access
and individual columns for formats. The checks on format is currently
implemented for gender and age formats.

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
