%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SQIpro
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Comprehensive Soil Quality Index Computation and Visualization

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-glmnet >= 4.1.0
BuildRequires:    R-CRAN-ggplot2 >= 3.3.0
BuildRequires:    R-CRAN-car >= 3.0.0
BuildRequires:    R-CRAN-FactoMineR >= 2.4
BuildRequires:    R-CRAN-tidyr >= 1.1.0
BuildRequires:    R-CRAN-factoextra >= 1.0.7
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-matrixStats >= 0.61.0
BuildRequires:    R-CRAN-rlang >= 0.4.0
BuildRequires:    R-stats 
BuildRequires:    R-methods 
Requires:         R-CRAN-glmnet >= 4.1.0
Requires:         R-CRAN-ggplot2 >= 3.3.0
Requires:         R-CRAN-car >= 3.0.0
Requires:         R-CRAN-FactoMineR >= 2.4
Requires:         R-CRAN-tidyr >= 1.1.0
Requires:         R-CRAN-factoextra >= 1.0.7
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-matrixStats >= 0.61.0
Requires:         R-CRAN-rlang >= 0.4.0
Requires:         R-stats 
Requires:         R-methods 

%description
Provides a comprehensive, modular framework for computing the Soil Quality
Index (SQI) using six established methods: Linear Scoring (Doran and
Parkin, 1994, <doi:10.2136/sssaspecpub35.c1>), Regression-based (Masto et
al., 2008, <doi:10.1007/s10661-007-9697-z>), Principal Component
Analysis-based (Andrews et al., 2004, <doi:10.2136/sssaj2004.1945>), Fuzzy
Logic, Entropy Weighting (Shannon, 1948,
<doi:10.1002/j.1538-7305.1948.tb01338.x>), and TOPSIS (Hwang and Yoon,
1981, <doi:10.1007/978-3-642-48318-9>). Implements four variable scoring
functions: more-is-better, less-is-better, optimum-value, and trapezoidal,
following Karlen and Stott (1994, <doi:10.2136/sssaspecpub35.c4>).
Includes automated Minimum Data Set selection via Principal Component
Analysis with Variance Inflation Factor filtering (Kaiser, 1960,
<doi:10.1177/001316446002000116>), one-way ANOVA with Tukey HSD post-hoc
tests, leave-one-out sensitivity analysis, and publication-quality
visualization using 'ggplot2'.

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
