%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CompositionalRF
%global packver   1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6
Release:          1%{?dist}%{?buildtag}
Summary:          Multivariate Random Forest with Compositional Responses

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildRequires:    R-CRAN-Compositional 
BuildRequires:    R-CRAN-RcppParallel 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-stats 
Requires:         R-CRAN-Compositional 
Requires:         R-CRAN-RcppParallel 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-Rfast 
Requires:         R-stats 

%description
Multivariate random forests with compositional responses and Euclidean
predictors is performed. The compositional data are first transformed
using the additive log-ratio transformation, or the alpha-transformation
of Tsagris, Preston and Wood (2011), <doi:10.48550/arXiv.1106.1451>, and
then the multivariate random forest of Rahman R., Otridge J. and Pal R.
(2017), <doi:10.1093/bioinformatics/btw765>, is applied.

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
