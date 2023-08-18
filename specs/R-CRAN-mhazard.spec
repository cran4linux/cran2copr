%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mhazard
%global packver   0.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Nonparametric and Semiparametric Methods for Multivariate Failure Time Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-plot3D 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-rootSolve 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-plot3D 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-rootSolve 

%description
Nonparametric survival function estimates and semiparametric regression
for the multivariate failure time data with right-censoring. For
nonparametric survival function estimates, the Volterra, Dabrowska, and
Prentice-Cai estimates for bivariate failure time data may be computed as
well as the Dabrowska estimate for the trivariate failure time data.
Bivariate marginal hazard rate regression can be fitted for the bivariate
failure time data. Functions are also provided to compute (bootstrap)
confidence intervals and plot the estimates of the bivariate survival
function. For details, see "The Statistical Analysis of Multivariate
Failure Time Data: A Marginal Modeling Approach", Prentice, R., Zhao, S.
(2019, ISBN: 978-1-4822-5657-4), CRC Press.

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
