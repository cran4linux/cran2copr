%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  baygel
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Estimators for Gaussian Graphical Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.8
BuildRequires:    R-CRAN-RcppArmadillo >= 0.11.1.1.0
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-statmod 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RcppProgress 
Requires:         R-CRAN-Rcpp >= 1.0.8
Requires:         R-CRAN-RcppArmadillo >= 0.11.1.1.0
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-statmod 
Requires:         R-stats 

%description
This R package offers a Bayesian graphical ridge and a naïve Bayesian
adaptive graphical elastic net data-augmented block Gibbs sampler. These
samplers facilitate the simulation of the posterior distribution of
precision matrices for Gaussian distributed data. These samplers were
originally proposed in two separate studies, both detailing their
methodologies and applications: Smith, Arashi, and Bekker (2022)
<doi:10.48550/arXiv.2210.16290> and Smith, Bekker, and Arashi (2023)
<doi:10.48550/arXiv.2306.14199>.

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
