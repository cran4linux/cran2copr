%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DDAWASS
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Discrete Distribution Data Analysis with Wasserstein Distance

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-HistDAWass 
BuildRequires:    R-CRAN-FactoMineR 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-methods 
Requires:         R-CRAN-HistDAWass 
Requires:         R-CRAN-FactoMineR 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tibble 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-grDevices 

%description
S4 classes and methods for the analysis of data described by discrete
distributions with finite support (e.g. frequency distributions of
ratings, scores or counts observed on groups of individuals), using the L2
Wasserstein metric between quantile functions. It is the discrete
counterpart of 'HistDAWass' and provides exact Wasserstein distances (in
C++), barycenters, Wasserstein variance, covariance and correlation,
k-means and hierarchical clustering, quantile-based principal component
and multiple factor analysis, two-component linear regression and
reliability (Cronbach's alpha) indices. See Crocetta, Irpino, Antonucci
and Marin (2025) <doi:10.1007/s11135-024-01956-0>.

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
