%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  noisysbmGGM
%global packver   0.1.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Noisy Stochastic Block Model for GGM Inference

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-ppcor 
BuildRequires:    R-CRAN-SILGGM 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-huge 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-RColorBrewer 
Requires:         R-parallel 
Requires:         R-CRAN-ppcor 
Requires:         R-CRAN-SILGGM 
Requires:         R-stats 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-huge 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-RcppArmadillo 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-RColorBrewer 

%description
Greedy Bayesian algorithm to fit the noisy stochastic block model to an
observed sparse graph. Moreover, a graph inference procedure to recover
Gaussian Graphical Model (GGM) from real data. This procedure comes with a
control of the false discovery rate. The method is described in the
article "Enhancing the Power of Gaussian Graphical Model Inference by
Modeling the Graph Structure" by Kilian, Rebafka, and Villers (2024)
<arXiv:2402.19021>.

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
