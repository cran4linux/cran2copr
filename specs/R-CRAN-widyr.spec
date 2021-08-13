%global __brp_check_rpaths %{nil}
%global packname  widyr
%global packver   0.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Widen, Process, then Re-Tidy Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-tidytext 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-gapminder 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-tidytext 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-gapminder 

%description
Encapsulates the pattern of untidying data into a wide matrix, performing
some processing, then turning it back into a tidy form. This is useful for
several operations such as co-occurrence counts, correlations, or
clustering that are mathematically convenient on wide matrices.

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
