%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  supportR
%global packver   1.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Support Functions for Wrangling and Visualization

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-data.tree 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gh 
BuildRequires:    R-CRAN-googledrive 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-vegan 
Requires:         R-CRAN-data.tree 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gh 
Requires:         R-CRAN-googledrive 
Requires:         R-graphics 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-magrittr 
Requires:         R-methods 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-vegan 

%description
Suite of helper functions for data wrangling and visualization. The only
theme for these functions is that they tend towards simple, short, and
narrowly-scoped. These functions are built for tasks that often recur but
are not large enough in scope to warrant an ecosystem of interdependent
functions.

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
