%global __brp_check_rpaths %{nil}
%global packname  mvnimpute
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Simultaneously Impute the Missing and Censored Values

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-LaplacesDemon 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-truncnorm 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppDist 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-LaplacesDemon 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-truncnorm 

%description
Implementing a multiple imputation algorithm for multivariate data with
missing and censored values under a coarsening at random assumption
(Heitjan and Rubin, 1991<doi:10.1214/aos/1176348396>). The multiple
imputation algorithm is based on the data augmentation algorithm proposed
by Tanner and Wong (1987)<doi:10.1080/01621459.1987.10478458>. The Gibbs
sampling algorithm is adopted to to update the model parameters and draw
imputations of the coarse data.

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
