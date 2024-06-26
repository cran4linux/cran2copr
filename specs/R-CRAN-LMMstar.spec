%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  LMMstar
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Repeated Measurement Models for Discrete Times

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-copula 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-lava 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-multcomp 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-copula 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-ggplot2 
Requires:         R-grid 
Requires:         R-CRAN-lava 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-multcomp 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-numDeriv 
Requires:         R-parallel 
Requires:         R-CRAN-rlang 

%description
Companion R package for the course "Statistical analysis of correlated and
repeated measurements for health science researchers" taught by the
section of Biostatistics of the University of Copenhagen. It implements
linear mixed models where the model for the variance-covariance of the
residuals is specified via patterns (compound symmetry, toeplitz,
unstructured, ...). Statistical inference for mean, variance, and
correlation parameters is performed based on the observed information and
a Satterthwaite approximation of the degrees of freedom. Normalized
residuals are provided to assess model misspecification. Statistical
inference can be performed for arbitrary linear or non-linear
combination(s) of model coefficients. Predictions can be computed
conditional to covariates only or also to outcome values.

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
