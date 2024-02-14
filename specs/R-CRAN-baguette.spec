%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  baguette
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Efficient Model Functions for Bagging

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6
Requires:         R-core >= 3.6
BuildArch:        noarch
BuildRequires:    R-CRAN-hardhat >= 1.1.0
BuildRequires:    R-CRAN-parsnip >= 1.0.0
BuildRequires:    R-CRAN-butcher 
BuildRequires:    R-CRAN-C50 
BuildRequires:    R-CRAN-dials 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-furrr 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-rpart 
BuildRequires:    R-CRAN-rsample 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-hardhat >= 1.1.0
Requires:         R-CRAN-parsnip >= 1.0.0
Requires:         R-CRAN-butcher 
Requires:         R-CRAN-C50 
Requires:         R-CRAN-dials 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-furrr 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-rpart 
Requires:         R-CRAN-rsample 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-utils 
Requires:         R-CRAN-withr 

%description
Tree- and rule-based models can be bagged (<doi:10.1007/BF00058655>) using
this package and their predictions equations are stored in an efficient
format to reduce the model objects size and speed.

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
