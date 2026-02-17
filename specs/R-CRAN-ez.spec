%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ez
%global packver   4.5-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Easy Analysis and Visualization of Factorial Experiments

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS >= 7.3.45
BuildRequires:    R-CRAN-ggplot2 >= 3.0.0
BuildRequires:    R-CRAN-car >= 2.1.3
BuildRequires:    R-CRAN-plyr >= 1.8.4
BuildRequires:    R-CRAN-mgcv >= 1.8.12
BuildRequires:    R-CRAN-reshape2 >= 1.4.2
BuildRequires:    R-CRAN-Matrix >= 1.2.7.1
BuildRequires:    R-CRAN-lme4 >= 1.1.12
BuildRequires:    R-CRAN-stringr >= 1.1.0
BuildRequires:    R-CRAN-scales >= 0.4.0
BuildRequires:    R-CRAN-rlang >= 0.4.0
Requires:         R-CRAN-MASS >= 7.3.45
Requires:         R-CRAN-ggplot2 >= 3.0.0
Requires:         R-CRAN-car >= 2.1.3
Requires:         R-CRAN-plyr >= 1.8.4
Requires:         R-CRAN-mgcv >= 1.8.12
Requires:         R-CRAN-reshape2 >= 1.4.2
Requires:         R-CRAN-Matrix >= 1.2.7.1
Requires:         R-CRAN-lme4 >= 1.1.12
Requires:         R-CRAN-stringr >= 1.1.0
Requires:         R-CRAN-scales >= 0.4.0
Requires:         R-CRAN-rlang >= 0.4.0

%description
Facilitates easy analysis of factorial experiments, including purely
within-Ss designs (a.k.a. "repeated measures"), purely between-Ss designs,
and mixed within-and-between-Ss designs. The functions in this package aim
to provide simple, intuitive and consistent specification of data analysis
and visualization. Visualization functions also include design
visualization for pre-analysis data auditing, and correlation matrix
visualization. Finally, this package includes functions for non-parametric
analysis, including permutation tests and bootstrap resampling. The
bootstrap function obtains predictions either by cell means or by more
advanced/powerful mixed effects models, yielding predictions and
confidence intervals that may be easily visualized at any level of the
experiment's design.

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
