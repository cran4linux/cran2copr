%global __brp_check_rpaths %{nil}
%global packname  povcalnetR
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Client for the 'Povcalnet' API

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-httr 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-js 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-naniar 
BuildRequires:    R-CRAN-memoise 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-httr 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-js 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-naniar 
Requires:         R-CRAN-memoise 

%description
Provides an interface to compute poverty and inequality indicators for
more than 160 countries and regions from the World Bank's database of
household surveys. It has the same functionality as the 'Povcalnet'
website (<http://iresearch.worldbank.org/PovcalNet/>). 'Povcalnet' is a
computational tool that allows users to estimate poverty rates for
regions, sets of countries or individual countries, over time and at any
poverty line. 'Povcalnet' is managed jointly by the data and research
group in the World Bank's development economics division. It draws heavily
upon a strong collaboration with the poverty and equity global practice,
which is responsible for the gathering and harmonization of the underlying
survey data.

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
