%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  nflfastR
%global packver   4.6.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.6.1
Release:          1%{?dist}%{?buildtag}
Summary:          Functions to Efficiently Access NFL Play by Play Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.0.0
BuildRequires:    R-CRAN-tibble >= 3.0
BuildRequires:    R-CRAN-stringr >= 1.3.0
BuildRequires:    R-CRAN-nflreadr >= 1.2.0
BuildRequires:    R-CRAN-data.table >= 1.14.0
BuildRequires:    R-CRAN-tidyselect >= 1.1.0
BuildRequires:    R-CRAN-xgboost >= 1.1
BuildRequires:    R-CRAN-fastrmodels >= 1.0.1
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-tidyr >= 1.0.0
BuildRequires:    R-CRAN-progressr >= 0.6.0
BuildRequires:    R-CRAN-rlang >= 0.4.7
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-furrr 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-janitor 
BuildRequires:    R-CRAN-mgcv 
Requires:         R-CRAN-cli >= 3.0.0
Requires:         R-CRAN-tibble >= 3.0
Requires:         R-CRAN-stringr >= 1.3.0
Requires:         R-CRAN-nflreadr >= 1.2.0
Requires:         R-CRAN-data.table >= 1.14.0
Requires:         R-CRAN-tidyselect >= 1.1.0
Requires:         R-CRAN-xgboost >= 1.1
Requires:         R-CRAN-fastrmodels >= 1.0.1
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-tidyr >= 1.0.0
Requires:         R-CRAN-progressr >= 0.6.0
Requires:         R-CRAN-rlang >= 0.4.7
Requires:         R-CRAN-curl 
Requires:         R-CRAN-furrr 
Requires:         R-CRAN-future 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-janitor 
Requires:         R-CRAN-mgcv 

%description
A set of functions to access National Football League play-by-play data
from <https://www.nfl.com/>.

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
