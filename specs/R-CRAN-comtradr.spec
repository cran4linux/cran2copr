%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  comtradr
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Interface with the United Nations Comtrade API

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-askpass 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-httr2 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-poorman 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-rappdirs 
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-CRAN-cachem 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-askpass 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-httr2 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-poorman 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-purrr 
Requires:         R-tools 
Requires:         R-CRAN-rappdirs 
Requires:         R-CRAN-memoise 
Requires:         R-CRAN-cachem 

%description
Interface with and extract data from the United Nations 'Comtrade' API
<https://comtradeplus.un.org/>. 'Comtrade' provides country level shipping
data for a variety of commodities, these functions allow for easy API
query and data returned as a tidy data frame.

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
