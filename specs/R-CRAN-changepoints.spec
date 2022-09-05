%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  changepoints
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Collection of Change-Point Detection Methods

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-gglasso 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-ks 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-data.tree 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-stats 
Requires:         R-CRAN-gglasso 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-ks 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-data.tree 
Requires:         R-CRAN-Rcpp 

%description
Performs a series of offline and/or online change-point detection
algorithms for 1) univariate mean: <doi:10.1214/20-EJS1710>,
<arXiv:2006.03283>; 2) univariate polynomials: <doi:10.1214/21-EJS1963>;
3) univariate and multivariate nonparametric settings:
<doi:10.1214/21-EJS1809>, <doi:10.1109/TIT.2021.3130330>; 4)
high-dimensional covariances: <doi:10.3150/20-BEJ1249>; 5)
high-dimensional networks with and without missing values:
<doi:10.1214/20-AOS1953>, <arXiv:2101.05477>, <arXiv:2110.06450>; 6)
high-dimensional linear regression models: <arXiv:2010.10410>,
<arXiv:2207.12453>; 7) high-dimensional vector autoregressive models:
<arXiv:1909.06359>; 8) high-dimensional self exciting point processes:
<arXiv:2006.03572>; 9) dependent dynamic nonparametric random dot product
graphs: <arXiv:1911.07494>; 10) univariate mean against adversarial
attacks: <arXiv:2105.10417>.

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
