%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  LorenzRegression
%global packver   2.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Lorenz and Penalized Lorenz Regressions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.1
Requires:         R-core >= 3.3.1
BuildRequires:    R-CRAN-Rcpp >= 0.11.0
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-parsnip 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-rsample 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-GA 
BuildRequires:    R-CRAN-Rearrangement 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.11.0
Requires:         R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-parsnip 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-rsample 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-GA 
Requires:         R-CRAN-Rearrangement 
Requires:         R-CRAN-progress 

%description
Inference for the Lorenz and penalized Lorenz regressions. More broadly,
the package proposes functions to assess inequality and graphically
represent it. The Lorenz Regression procedure is introduced in Heuchenne
and Jacquemain (2022) <doi:10.1016/j.csda.2021.107347> and in Jacquemain,
A., C. Heuchenne, and E. Pircalabelu (2024) <doi:10.1214/23-EJS2200>.

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
