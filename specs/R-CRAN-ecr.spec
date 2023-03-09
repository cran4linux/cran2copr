%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ecr
%global packver   2.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Evolutionary Computation in R

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-BBmisc >= 1.6
BuildRequires:    R-CRAN-reshape2 >= 1.4.1
BuildRequires:    R-CRAN-smoof >= 1.4
BuildRequires:    R-CRAN-parallelMap >= 1.3
BuildRequires:    R-CRAN-ParamHelpers >= 1.1
BuildRequires:    R-CRAN-checkmate >= 1.1
BuildRequires:    R-CRAN-ggplot2 >= 1.0.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.16
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-plot3D 
BuildRequires:    R-CRAN-plot3Drgl 
BuildRequires:    R-CRAN-scatterplot3d 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-kableExtra 
BuildRequires:    R-CRAN-lazyeval 
Requires:         R-CRAN-BBmisc >= 1.6
Requires:         R-CRAN-reshape2 >= 1.4.1
Requires:         R-CRAN-smoof >= 1.4
Requires:         R-CRAN-parallelMap >= 1.3
Requires:         R-CRAN-ParamHelpers >= 1.1
Requires:         R-CRAN-checkmate >= 1.1
Requires:         R-CRAN-ggplot2 >= 1.0.0
Requires:         R-CRAN-Rcpp >= 0.12.16
Requires:         R-CRAN-viridis 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-plot3D 
Requires:         R-CRAN-plot3Drgl 
Requires:         R-CRAN-scatterplot3d 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-kableExtra 
Requires:         R-CRAN-lazyeval 

%description
Framework for building evolutionary algorithms for both single- and
multi-objective continuous or discrete optimization problems. A set of
predefined evolutionary building blocks and operators is included.
Moreover, the user can easily set up custom objective functions,
operators, building blocks and representations sticking to few
conventions. The package allows both a black-box approach for standard
tasks (plug-and-play style) and a much more flexible white-box approach
where the evolutionary cycle is written by hand.

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
