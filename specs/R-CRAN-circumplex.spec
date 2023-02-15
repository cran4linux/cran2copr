%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  circumplex
%global packver   0.3.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.9
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis and Visualization of Circular Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4
Requires:         R-core >= 3.4
BuildRequires:    R-CRAN-ggplot2 >= 3.3.0
BuildRequires:    R-CRAN-tibble >= 3.0.0
BuildRequires:    R-CRAN-magrittr >= 1.5
BuildRequires:    R-CRAN-boot >= 1.3.18
BuildRequires:    R-CRAN-htmlTable >= 1.13.3
BuildRequires:    R-CRAN-tidyr >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 0.8.5
BuildRequires:    R-CRAN-rlang >= 0.4.11
BuildRequires:    R-CRAN-purrr >= 0.3.4
BuildRequires:    R-CRAN-ggforce >= 0.3.0
BuildRequires:    R-CRAN-assertthat >= 0.2.1
BuildRequires:    R-CRAN-RcppArmadillo >= 0.11
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
Requires:         R-CRAN-ggplot2 >= 3.3.0
Requires:         R-CRAN-tibble >= 3.0.0
Requires:         R-CRAN-magrittr >= 1.5
Requires:         R-CRAN-boot >= 1.3.18
Requires:         R-CRAN-htmlTable >= 1.13.3
Requires:         R-CRAN-tidyr >= 1.0.0
Requires:         R-CRAN-dplyr >= 0.8.5
Requires:         R-CRAN-rlang >= 0.4.11
Requires:         R-CRAN-purrr >= 0.3.4
Requires:         R-CRAN-ggforce >= 0.3.0
Requires:         R-CRAN-assertthat >= 0.2.1
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 

%description
Circumplex models, which organize constructs in a circle around two
underlying dimensions, are popular for studying interpersonal functioning,
mood/affect, and vocational preferences/environments. This package
provides tools for analyzing and visualizing circular data, including
scoring functions for relevant instruments and a generalization of the
bootstrapped structural summary method from Zimmermann & Wright (2017)
<doi:10.1177/1073191115621795> and functions for creating
publication-ready tables and figures from the results.

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
