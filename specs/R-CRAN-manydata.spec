%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  manydata
%global packver   0.9.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.3
Release:          1%{?dist}%{?buildtag}
Summary:          A Portal for Global Governance Data

License:          CC BY 4.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.4.0
BuildRequires:    R-CRAN-messydates >= 0.4.1
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-usethis 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-remotes 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-cli 
Requires:         R-CRAN-ggplot2 >= 3.4.0
Requires:         R-CRAN-messydates >= 0.4.1
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-usethis 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-remotes 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-cli 

%description
This is the core package for the many packages universe. It includes
functions to help researchers work with and contribute to event datasets
on global governance.

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
