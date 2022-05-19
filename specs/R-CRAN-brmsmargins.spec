%global __brp_check_rpaths %{nil}
%global packname  brmsmargins
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Marginal Effects for 'brms' Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-data.table >= 1.12.0
BuildRequires:    R-CRAN-extraoperators >= 0.1.1
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-brms 
BuildRequires:    R-CRAN-bayestestR 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-posterior 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-data.table >= 1.12.0
Requires:         R-CRAN-extraoperators >= 0.1.1
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-brms 
Requires:         R-CRAN-bayestestR 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-posterior 

%description
Calculate Bayesian marginal effects, average marginal effects, and
marginal coefficients (also called population averaged coefficients) for
models fit using the 'brms' package including fixed effects, mixed
effects, and location scale models. These are based on marginal
predictions that integrate out random effects if necessary (see for
example <doi:10.1186/s12874-015-0046-6> and <doi:10.1111/biom.12707>).

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
