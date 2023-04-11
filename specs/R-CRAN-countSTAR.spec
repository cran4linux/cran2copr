%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  countSTAR
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Flexible Modeling of Count Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-dbarts 
BuildRequires:    R-CRAN-FastGP 
BuildRequires:    R-CRAN-gbm 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-spikeSlabGAM 
BuildRequires:    R-CRAN-splines2 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-TruncatedNormal 
BuildRequires:    R-CRAN-truncdist 
BuildRequires:    R-CRAN-KFAS 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-dbarts 
Requires:         R-CRAN-FastGP 
Requires:         R-CRAN-gbm 
Requires:         R-graphics 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-spikeSlabGAM 
Requires:         R-CRAN-splines2 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-TruncatedNormal 
Requires:         R-CRAN-truncdist 
Requires:         R-CRAN-KFAS 

%description
For Bayesian and classical inference and prediction with count-valued
data, Simultaneous Transformation and Rounding (STAR) Models provide a
flexible, interpretable, and easy-to-use approach. STAR models the
observed count data using a rounded continuous data model and incorporates
a transformation for greater flexibility. Implicitly, STAR formalizes the
commonly-applied yet incoherent procedure of (i) transforming count-valued
data and subsequently (ii) modeling the transformed data using Gaussian
models. STAR is well-defined for count-valued data, which is reflected in
predictive accuracy, and is designed to account for zero-inflation,
bounded or censored data, and over- or underdispersion. Importantly, STAR
is easy to combine with existing MCMC or point estimation methods for
continuous data, which allows seamless adaptation of continuous data
models (such as linear regressions, additive models, BART, random forests,
and gradient boosting machines) for count-valued data. The package also
includes several methods for modeling count time series data, namely via
warped Dynamic Linear Models. For more details and background on these
methodologies, see the works of Kowal and Canale (2020)
<doi:10.1214/20-EJS1707>, Kowal and Wu (2022) <doi:10.1111/biom.13617>,
King and Kowal (2022) <arXiv:2110.14790>, and Kowal and Wu (2023)
<arXiv:2110.12316>.

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
