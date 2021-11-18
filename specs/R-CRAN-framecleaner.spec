%global __brp_check_rpaths %{nil}
%global packname  framecleaner
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Clean Data Frames

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-janitor 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-bit64 
BuildRequires:    R-CRAN-rio 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-vroom 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-rlist 
BuildRequires:    R-CRAN-fastDummies 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-janitor 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-bit64 
Requires:         R-CRAN-rio 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-vroom 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-rlist 
Requires:         R-CRAN-fastDummies 

%description
Provides a friendly interface for modifying data frames with a sequence of
piped commands built upon the 'tidyverse' Wickham et al., (2019)
<doi:10.21105/joss.01686> . The majority of commands wrap 'dplyr' mutate
statements in a convenient way to concisely solve common issues that arise
when tidying small to medium data sets. Includes smart defaults and allows
flexible selection of columns via 'tidyselect'.

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
