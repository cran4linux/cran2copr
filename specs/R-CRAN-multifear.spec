%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  multifear
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Multiverse Analyses for Conditioning Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.2.1
BuildRequires:    R-CRAN-nlme >= 3.1.144
BuildRequires:    R-CRAN-bootstrap >= 2019
BuildRequires:    R-CRAN-tibble >= 2.1.3
BuildRequires:    R-CRAN-reshape2 >= 1.4.3
BuildRequires:    R-CRAN-forestplot >= 1.10
BuildRequires:    R-CRAN-BayesFactor >= 0.9.12.4.2
BuildRequires:    R-CRAN-dplyr >= 0.8.4
BuildRequires:    R-CRAN-effsize >= 0.7.8
BuildRequires:    R-CRAN-broom >= 0.5.5
BuildRequires:    R-CRAN-esc >= 0.5.1
BuildRequires:    R-CRAN-effectsize >= 0.4.1
BuildRequires:    R-CRAN-purrr >= 0.3.3
BuildRequires:    R-CRAN-bayestestR >= 0.10.0
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-fastDummies 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-maditr 
BuildRequires:    R-CRAN-car 
Requires:         R-CRAN-ggplot2 >= 3.2.1
Requires:         R-CRAN-nlme >= 3.1.144
Requires:         R-CRAN-bootstrap >= 2019
Requires:         R-CRAN-tibble >= 2.1.3
Requires:         R-CRAN-reshape2 >= 1.4.3
Requires:         R-CRAN-forestplot >= 1.10
Requires:         R-CRAN-BayesFactor >= 0.9.12.4.2
Requires:         R-CRAN-dplyr >= 0.8.4
Requires:         R-CRAN-effsize >= 0.7.8
Requires:         R-CRAN-broom >= 0.5.5
Requires:         R-CRAN-esc >= 0.5.1
Requires:         R-CRAN-effectsize >= 0.4.1
Requires:         R-CRAN-purrr >= 0.3.3
Requires:         R-CRAN-bayestestR >= 0.10.0
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-fastDummies 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-maditr 
Requires:         R-CRAN-car 

%description
A suite of functions for performing analyses, based on a multiverse
approach, for conditioning data. Specifically, given the appropriate data,
the functions are able to perform t-tests, analyses of variance, and mixed
models for the provided data and return summary statistics and plots. The
function is also able to return for all those tests p-values, confidence
intervals, and Bayes factors. The methods are described in Lonsdorf,
Gerlicher, Klingelhofer-Jens, & Krypotos (2022)
<doi:10.1016/j.brat.2022.104072>. Since November 2025, this package
contains code from the 'ez' R package (Copyright (c) 2016-11-01, Michael
A. Lawrence <mike.lwrnc@gmail.com>), originally distributed under the
'GPL' (equal and above 2) license.

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
