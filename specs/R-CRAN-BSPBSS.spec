%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BSPBSS
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Spatial Blind Source Separation

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildRequires:    R-CRAN-movMF 
BuildRequires:    R-CRAN-rstiefel 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-ica 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-CRAN-BayesGPfit 
BuildRequires:    R-CRAN-svd 
BuildRequires:    R-CRAN-RandomFieldsUtils 
BuildRequires:    R-CRAN-neurobase 
BuildRequires:    R-CRAN-oro.nifti 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-movMF 
Requires:         R-CRAN-rstiefel 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-ica 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-gplots 
Requires:         R-CRAN-BayesGPfit 
Requires:         R-CRAN-svd 
Requires:         R-CRAN-RandomFieldsUtils 
Requires:         R-CRAN-neurobase 
Requires:         R-CRAN-oro.nifti 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gtools 

%description
Gibbs sampling for Bayesian spatial blind source separation (BSP-BSS).
BSP-BSS is designed for spatially dependent signals in high dimensional
and large-scale data, such as neuroimaging. The method assumes the
expectation of the observed images as a linear mixture of multiple sparse
and piece-wise smooth latent source signals, and constructs a Bayesian
nonparametric prior by thresholding Gaussian processes. Details can be
found in our paper: Wu et al. (2022+) "Bayesian Spatial Blind Source
Separation via the Thresholded Gaussian Process"
<doi:10.1080/01621459.2022.2123336>.

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
