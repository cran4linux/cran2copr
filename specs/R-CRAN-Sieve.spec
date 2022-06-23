%global __brp_check_rpaths %{nil}
%global packname  Sieve
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Nonparametric Estimation by the Method of Sieves

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.7
BuildRequires:    R-CRAN-combinat 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.7
Requires:         R-CRAN-combinat 
Requires:         R-CRAN-glmnet 
Requires:         R-methods 

%description
Performs multivariate nonparametric regression/classification by the
method of sieves (or using orthogonal series). The method is suitable for
continuous/binary problems with multivariate or moderate high-dimensional
features (dimension < 100). The main estimator in this package, penalized
sieve estimator, is adaptive to the feature dimension with provable
theoretical guarantees. Moreover, such a method is computationally
tractable in the sense it typically has a polynomial dependence (rather
than an exponential one) on the feature dimension and an almost linear
dependence on the sample size. Details of the methods and model
assumptions can be found in: Tianyu Zhang, and Noah Simon (2022)
<arXiv:2206.02994>.

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
