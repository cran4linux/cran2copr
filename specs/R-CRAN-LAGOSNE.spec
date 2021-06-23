%global __brp_check_rpaths %{nil}
%global packname  LAGOSNE
%global packver   2.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Interface to the Lake Multi-Scaled Geospatial and Temporal Database

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-curl >= 2.7
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-stringr >= 1.2.0
BuildRequires:    R-CRAN-dplyr >= 0.7.0
BuildRequires:    R-CRAN-rappdirs >= 0.3.1
BuildRequires:    R-CRAN-purrr >= 0.2.2.2
BuildRequires:    R-CRAN-lazyeval >= 0.2
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-qs 
Requires:         R-CRAN-curl >= 2.7
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-stringr >= 1.2.0
Requires:         R-CRAN-dplyr >= 0.7.0
Requires:         R-CRAN-rappdirs >= 0.3.1
Requires:         R-CRAN-purrr >= 0.2.2.2
Requires:         R-CRAN-lazyeval >= 0.2
Requires:         R-CRAN-sf 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-memoise 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-qs 

%description
Client for programmatic access to the Lake Multi-scaled Geospatial and
Temporal database <https://lagoslakes.org>, with functions for accessing
lake water quality and ecological context data for the US.

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
