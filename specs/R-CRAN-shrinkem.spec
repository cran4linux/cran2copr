%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  shrinkem
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Approximate Bayesian Regularization for Parsimonious Estimates

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-extraDistr 
BuildRequires:    R-CRAN-brms 
BuildRequires:    R-CRAN-CholWishart 
BuildRequires:    R-CRAN-matrixcalc 
Requires:         R-stats 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-extraDistr 
Requires:         R-CRAN-brms 
Requires:         R-CRAN-CholWishart 
Requires:         R-CRAN-matrixcalc 

%description
Approximate Bayesian regularization using Gaussian approximations. The
input is a vector of estimates and a Gaussian error covariance matrix of
the key parameters. Bayesian shrinkage is then applied to obtain
parsimonious solutions. The method is described on Karimova, van Erp,
Leenders, and Mulder (2024) <DOI:10.31234/osf.io/2g8qm>. Gibbs samplers
are used for model fitting. The shrinkage priors that are supported are
Gaussian (ridge) priors, Laplace (lasso) priors (Park and Casella, 2008
<DOI:10.1198/016214508000000337>), and horseshoe priors (Carvalho, et al.,
2010; <DOI:10.1093/biomet/asq017>). These priors include an option for
grouped regularization of different subsets of parameters (Meier et al.,
2008; <DOI:10.1111/j.1467-9868.2007.00627.x>). F priors are used for the
penalty parameters lambda^2 (Mulder and Pericchi, 2018
<DOI:10.1214/17-BA1092>). This correspond to half-Cauchy priors on lambda
(Carvalho, Polson, Scott, 2010 <DOI:10.1093/biomet/asq017>).

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
