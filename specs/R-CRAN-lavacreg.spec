%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  lavacreg
%global packver   0.2-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Latent Variable Count Regression Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.5
BuildRequires:    R-CRAN-fastGHQuad 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-SparseGrid 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.5
Requires:         R-CRAN-fastGHQuad 
Requires:         R-CRAN-pracma 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-SparseGrid 

%description
Estimation of a multi-group count regression models (i.e., Poisson,
negative binomial) with latent covariates. This packages provides two
extensions compared to ordinary count regression models based on a
generalized linear model: First, measurement models for the predictors can
be specified allowing to account for measurement error. Second, the count
regression can be simultaneously estimated in multiple groups with
stochastic group weights. The marginal maximum likelihood estimation is
described in Kiefer & Mayer (2020) <doi:10.1080/00273171.2020.1751027>.

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
