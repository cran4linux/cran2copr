%global __brp_check_rpaths %{nil}
%global packname  changepoints
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
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
algorithms for 1) univariate mean; 2) univariate polynomials; 3)
univariate and multivariate nonparametric settings; 4) high-dimensional
covariances; 5) high-dimensional networks with and without missing values;
6) high-dimensional linear regression models; 7) high-dimensional vector
autoregressive models; 8) high-dimensional self exciting point processes;
9) dependent dynamic nonparametric random dot product graphs; 10)
univariate mean against adversarial attacks. For more informations, see
<arXiv:1810.09498>; <arXiv:2006.03283>; <arXiv:2007.09910>;
<arXiv:1905.10019>; <arXiv:1910.13289>; <arXiv:1712.09912>;
<arXiv:1809.09602>; <arXiv:1911.07494>; <arXiv:2101.05477>;
<arXiv:2010.10410>; <arXiv:1909.06359>; <arXiv:2006.03572>;
<arXiv:2110.06450>; <arXiv:2105.10417>.

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
