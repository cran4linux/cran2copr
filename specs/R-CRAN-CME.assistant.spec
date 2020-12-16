%global packname  CME.assistant
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Reusable Assisting Functions for Child Mortality Estimation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.0.0
BuildRequires:    R-CRAN-data.table >= 1.12.0
BuildRequires:    R-CRAN-ggforce >= 0.2.1.9000
BuildRequires:    R-CRAN-here 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-xlsx 
BuildRequires:    R-CRAN-usethis 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-ggplot2 >= 3.0.0
Requires:         R-CRAN-data.table >= 1.12.0
Requires:         R-CRAN-ggforce >= 0.2.1.9000
Requires:         R-CRAN-here 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-xlsx 
Requires:         R-CRAN-usethis 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-stringr 

%description
Provide helper functions for UNICEF child mortality estimation.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
