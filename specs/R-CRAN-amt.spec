%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  amt
%global packver   0.3.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Animal Movement Tools

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-tidyr >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 0.7.0
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-circular 
BuildRequires:    R-CRAN-ctmm 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-fitdistrplus 
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-KernSmooth 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-sfheaders 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-utils 
Requires:         R-CRAN-tidyr >= 1.0.0
Requires:         R-CRAN-dplyr >= 0.7.0
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-circular 
Requires:         R-CRAN-ctmm 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-fitdistrplus 
Requires:         R-CRAN-FNN 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-KernSmooth 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-MASS 
Requires:         R-methods 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-sfheaders 
Requires:         R-stats 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-tibble 
Requires:         R-utils 

%description
Manage and analyze animal movement data. The functionality of 'amt'
includes methods to calculate home ranges, track statistics (e.g. step
lengths, speed, or turning angles), prepare data for fitting habitat
selection analyses, and simulation of space-use from fitted step-selection
functions.

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
