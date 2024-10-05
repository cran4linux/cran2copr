%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  theftdlc
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Analyse and Interpret Time Series Features

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-theft >= 0.6.1
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-broom 
BuildRequires:    R-CRAN-Rtsne 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-janitor 
BuildRequires:    R-CRAN-umap 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-normaliseR 
BuildRequires:    R-CRAN-correctR 
Requires:         R-CRAN-theft >= 0.6.1
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-broom 
Requires:         R-CRAN-Rtsne 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-janitor 
Requires:         R-CRAN-umap 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-normaliseR 
Requires:         R-CRAN-correctR 

%description
Provides a suite of functions for analysing, interpreting, and visualising
time-series features calculated from different feature sets from the
'theft' package. Implements statistical learning methodologies described
in Henderson, T., Bryant, A., and Fulcher, B. (2023)
<doi:10.48550/arXiv.2303.17809>.

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
