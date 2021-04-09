%global packname  rfishbase
%global packver   3.1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1.7
Release:          1%{?dist}%{?buildtag}
Summary:          R Interface to 'FishBase'

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-arkdb >= 0.0.12
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-gh 
BuildRequires:    R-CRAN-DBI 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-curl 
BuildRequires:    R-CRAN-dbplyr 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-RSQLite 
Requires:         R-CRAN-arkdb >= 0.0.12
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-purrr 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-CRAN-memoise 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-gh 
Requires:         R-CRAN-DBI 
Requires:         R-tools 
Requires:         R-CRAN-curl 
Requires:         R-CRAN-dbplyr 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-RSQLite 

%description
A programmatic interface to 'FishBase', re-written based on an
accompanying 'RESTful' API. Access tables describing over 30,000 species
of fish, their biology, ecology, morphology, and more. This package also
supports experimental access to 'SeaLifeBase' data, which contains nearly
200,000 species records for all types of aquatic life not covered by
'FishBase.'

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
