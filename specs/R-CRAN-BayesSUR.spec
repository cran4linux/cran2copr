%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BayesSUR
%global packver   2.1-7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.7
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Seemingly Unrelated Regression

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-RcppArmadillo >= 0.9.000
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-tikzDevice 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-tikzDevice 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-grDevices 
Requires:         R-graphics 

%description
Bayesian seemingly unrelated regression with general variable selection
and dense/sparse covariance matrix. The sparse seemingly unrelated
regression is described in Bottolo et al. (2021) <doi:10.1111/rssc.12490>,
the software paper is in Zhao et al. (2021) <doi:10.18637/jss.v100.i11>,
and the model with random effects is described in Zhao et al. (2024)
<doi:10.1093/jrsssc/qlad102>.

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
