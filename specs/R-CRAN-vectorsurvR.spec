%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  vectorsurvR
%global packver   1.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.1
Release:          1%{?dist}%{?buildtag}
Summary:          Data Access and Analytical Tools for 'VectorSurv' Users

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-kableExtra 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-httr2 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-DT 
BuildRequires:    R-CRAN-sf 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-kableExtra 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-httr2 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-DT 
Requires:         R-CRAN-sf 

%description
Allows registered 'VectorSurv' <https://vectorsurv.org/> users access to
data through the 'VectorSurv API' <https://api.vectorsurv.org/>.
Additionally provides functions for analysis and visualization.

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
