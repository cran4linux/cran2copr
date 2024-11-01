%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  scicomptools
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tools Developed by the NCEAS Scientific Computing Support Team

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-chromote 
BuildRequires:    R-CRAN-data.tree 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-gitcreds 
BuildRequires:    R-CRAN-googledrive 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggwordcloud 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-SemNetCleaner 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tidytext 
BuildRequires:    R-CRAN-tidyxl 
Requires:         R-CRAN-chromote 
Requires:         R-CRAN-data.tree 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-gitcreds 
Requires:         R-CRAN-googledrive 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggwordcloud 
Requires:         R-CRAN-magrittr 
Requires:         R-methods 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-SemNetCleaner 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tidytext 
Requires:         R-CRAN-tidyxl 

%description
Set of tools to import, summarize, wrangle, and visualize data. These
functions were originally written based on the needs of the various
synthesis working groups that were supported by the National Center for
Ecological Analysis and Synthesis (NCEAS). These tools are meant to be
useful inside and outside of the context for which they were designed.

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
