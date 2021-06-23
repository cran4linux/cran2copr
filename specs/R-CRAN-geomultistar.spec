%global __brp_check_rpaths %{nil}
%global packname  geomultistar
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Multidimensional Queries Enriched with Geographic Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-starschemar 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-snakecase 
BuildRequires:    R-CRAN-RSQLite 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-pander 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-starschemar 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-snakecase 
Requires:         R-CRAN-RSQLite 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-pander 

%description
Multidimensional systems allow complex queries to be carried out in an
easy way. The geographical dimension, together with the temporal
dimension, plays a fundamental role in multidimensional systems. Through
this package, vector layers can be associated to the attributes of
geographic dimensions, so that the results of multidimensional queries can
be obtained directly as vector layers. The multidimensional structures on
which we can define the queries can be created from a flat table or
imported directly using functions from this package.

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
