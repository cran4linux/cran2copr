%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  TidyDensity
%global packver   1.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Functions for Tidy Analysis and Generation of Random Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rlang >= 0.4.11
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-actuar 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-stringr 
Requires:         R-CRAN-rlang >= 0.4.11
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-actuar 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-nloptr 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-stringr 

%description
To make it easy to generate random numbers based upon the underlying stats
distribution functions. All data is returned in a tidy and structured
format making working with the data simple and straight forward. Given
that the data is returned in a tidy 'tibble' it lends itself to working
with the rest of the 'tidyverse'.

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
