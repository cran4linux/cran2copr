%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  chms
%global packver   7.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          7.1
Release:          1%{?dist}%{?buildtag}
Summary:          Accelerometer Processing Methods for Cycle 7 of the CHMS

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-CRAN-dbplyr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-hms 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-mirai 
BuildRequires:    R-CRAN-mori 
BuildRequires:    R-CRAN-parallelly 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-RSQLite 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-DBI 
Requires:         R-CRAN-dbplyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-hms 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-mirai 
Requires:         R-CRAN-mori 
Requires:         R-CRAN-parallelly 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-RSQLite 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyr 
Requires:         R-utils 
Requires:         R-CRAN-zoo 

%description
'ActiGraph wGT3X-BT' accelerometer processing methods using the
standardized workflow developed by Statistics Canada for cycle 7 of the
Canadian Health Measures Survey (CHMS). The package promotes transparent
and reproducible data processing while supporting the harmonization of
analytical approaches among researchers wishing to align with Statistics
Canada's methods. For general details about the processing methods, please
consult Clarke J, Gribbon A, St-Laurent M, Ferrao T, Barnes J, Kuzik N,
Colley R (2026) <doi: 10.25318/82-003-x202600200001-eng>.

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
