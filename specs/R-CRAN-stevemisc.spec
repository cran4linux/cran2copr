%global __brp_check_rpaths %{nil}
%global packname  stevemisc
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Steve's Miscellaneous Functions

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.0
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-broom.mixed 
BuildRequires:    R-CRAN-labelled 
BuildRequires:    R-CRAN-arm 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-forcats 
Requires:         R-CRAN-ggplot2 >= 3.3.0
Requires:         R-stats 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-broom.mixed 
Requires:         R-CRAN-labelled 
Requires:         R-CRAN-arm 
Requires:         R-parallel 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-dplyr 
Requires:         R-methods 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-forcats 

%description
These are miscellaneous functions that I find useful for my research and
teaching. The contents include themes for plots, functions for simulating
quantities of interest from regression models, functions for simulating
various forms of fake data for instructional/research purposes, and many
more. All told, the functions provided here are broadly useful for data
organization, data presentation, data recoding, and data simulation.

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
