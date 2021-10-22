%global __brp_check_rpaths %{nil}
%global packname  GCPBayes
%global packver   3.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Meta-Analysis of Pleiotropic Effects Using Group Structure

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-arm 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-invgamma 
BuildRequires:    R-CRAN-gdata 
BuildRequires:    R-CRAN-truncnorm 
BuildRequires:    R-CRAN-postpack 
BuildRequires:    R-CRAN-wiqid 
BuildRequires:    R-CRAN-usethis 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-arm 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-invgamma 
Requires:         R-CRAN-gdata 
Requires:         R-CRAN-truncnorm 
Requires:         R-CRAN-postpack 
Requires:         R-CRAN-wiqid 
Requires:         R-CRAN-usethis 
Requires:         R-CRAN-Rcpp 

%description
Run a Gibbs sampler for a multivariate Bayesian sparse group selection
model with Dirac, continuous and hierarchical spike prior for detecting
pleiotropy on the traits. This package is designed for summary statistics
containing estimated regression coefficients and its estimated covariance
matrix. The methodology is available from: Baghfalaki, T., Sugier, P. E.,
Truong, T., Pettitt, A. N., Mengersen, K., & Liquet, B. (2021)
<doi:10.1002/sim.8855>.

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
