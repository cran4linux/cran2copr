%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  normalblockr
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Gaussian Models with Latent Clustering of Variables

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-sbm 
BuildRequires:    R-CRAN-corrplot 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-sbm 
Requires:         R-CRAN-corrplot 
Requires:         R-CRAN-MASS 
Requires:         R-stats 
Requires:         R-CRAN-Rcpp 

%description
Implements two families of Gaussian models with a latent clustering of the
variables, for multivariate data whose variables co-vary, or respond to
covariates, in groups. In the Normal-Block-Var model, the clusters
structure the covariance through latent variables, and a network is
inferred between the clusters rather than between the variables, which
reduces its dimension and eases its interpretation (Tous and Chiquet
(2026) <doi:10.1016/j.csda.2026.108347>). In the Normal-Block-Mean model,
the variables of a cluster share the same regression profile, and a
network between the variables can be inferred from their residual
covariance. In both families, the clustering is either known or inferred,
the network can be sparse (graphical lasso), and zero-inflated variants
handle data with an excess of zeros. The parameters are estimated by
expectation-maximization or variational expectation-maximization
algorithms, accelerated by squared extrapolation, and a split and merge
procedure improves the fits of a collection of models. The number of
clusters, the sparsity of the network and the shape of the covariance are
chosen with penalized criteria, cross-validation or stability selection.

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
