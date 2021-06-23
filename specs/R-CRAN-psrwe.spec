%global __brp_check_rpaths %{nil}
%global packname  psrwe
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          1%{?dist}%{?buildtag}
Summary:          PS-Integrated Methods for Incorporating RWE in Clinical Studies

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildRequires:    R-CRAN-randomForest >= 4.6.14
BuildRequires:    R-CRAN-ggplot2 >= 3.3.2
BuildRequires:    R-parallel >= 3.2
BuildRequires:    R-CRAN-StanHeaders >= 2.21.0.5
BuildRequires:    R-CRAN-rstan >= 2.19.3
BuildRequires:    R-CRAN-BH >= 1.72.0.3
BuildRequires:    R-CRAN-Rcpp >= 1.0.5
BuildRequires:    R-CRAN-cowplot >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 0.8.5
BuildRequires:    R-CRAN-RcppEigen >= 0.3.3.7.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rstantools
Requires:         R-CRAN-randomForest >= 4.6.14
Requires:         R-CRAN-ggplot2 >= 3.3.2
Requires:         R-parallel >= 3.2
Requires:         R-CRAN-rstan >= 2.19.3
Requires:         R-CRAN-Rcpp >= 1.0.5
Requires:         R-CRAN-cowplot >= 1.0.0
Requires:         R-CRAN-dplyr >= 0.8.5
Requires:         R-methods 
Requires:         R-CRAN-rstantools

%description
High-quality real-world data can be transformed into scientific real-world
evidence (RWE) for regulatory and healthcare decision-making using proven
analytical methods and techniques. For example, propensity score (PS)
methodology can be applied to pre-select a subset of real-world data
containing patients that are similar to those in the current clinical
study in terms of covariates, and to stratify the selected patients
together with those in the current study into more homogeneous strata.
Then, methods such as power prior approach or composite likelihood
approach can be applied in each stratum to draw inference for the
parameters of interest. This package provides functions that implement the
PS-integrated RWE analysis methods proposed in Wang et al. (2019)
<doi:10.1080/10543406.2019.1657133>, Wang et al. (2020)
<doi:10.1080/10543406.2019.1684309> and Chen et al. (2020)
<doi:10.1080/10543406.2020.1730877>.

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
