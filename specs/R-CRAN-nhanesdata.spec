%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  nhanesdata
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Harmonized Access to NHANES Survey Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-arrow 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-nhanesA 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-srvyr 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-arrow 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-nhanesA 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-srvyr 
Requires:         R-CRAN-tibble 

%description
Instant access to harmonized National Health and Nutrition Examination
Survey (NHANES) data spanning 1999-2023. Retrieve pre-processed datasets
from reliable cloud storage with automatic type reconciliation and
integrated search tools for variables and datasets. Simplifies NHANES data
workflows by handling cycle management and maintaining data consistency
across survey waves. Data is sourced from
<https://www.cdc.gov/nchs/nhanes/>.

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
