%global __brp_check_rpaths %{nil}
%global packname  DSSAT
%global packver   0.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.6
Release:          1%{?dist}%{?buildtag}
Summary:          A Comprehensive R Interface for the DSSAT Cropping Systems Model

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-rlang 

%description
The purpose of this package is to provide a comprehensive R interface to
the Decision Support System for Agrotechnology Transfer Cropping Systems
Model (DSSAT-CSM; see <https://dssat.net> for more information). The
package provides cross-platform functions to read and write input files,
run DSSAT-CSM, and read output files.

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
