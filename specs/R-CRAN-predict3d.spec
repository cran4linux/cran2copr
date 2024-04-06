%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  predict3d
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Draw Three Dimensional Predict Plot Using Package 'rgl'

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.1.0
BuildRequires:    R-CRAN-rgl >= 1.0.1
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggiraphExtra 
BuildRequires:    R-CRAN-modelr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-ggplot2 >= 3.1.0
Requires:         R-CRAN-rgl >= 1.0.1
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggiraphExtra 
Requires:         R-CRAN-modelr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-magrittr 
Requires:         R-stats 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-tidyr 

%description
Draw 2 dimensional and three dimensional plot for multiple regression
models using package 'ggplot2' and 'rgl'. Supports linear models (lm),
generalized linear models (glm) and local polynomial regression fittings
(loess).

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
