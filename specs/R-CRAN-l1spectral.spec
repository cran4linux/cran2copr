%global __brp_check_rpaths %{nil}
%global packname  l1spectral
%global packver   0.99.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.99.6
Release:          1%{?dist}%{?buildtag}
Summary:          An L1-Version of the Spectral Clustering

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 0.12.5
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-aricode 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-cvTools 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 0.12.5
Requires:         R-stats 
Requires:         R-CRAN-dplyr 
Requires:         R-graphics 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-aricode 
Requires:         R-grDevices 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-cvTools 

%description
Provides an l1-version of the spectral clustering algorithm devoted to
robustly clustering highly perturbed graphs using l1-penalty. This
algorithm is described with more details in the preprint C. Champion, M.
Champion, M. Blazère, R. Burcelin and J.M. Loubes, "l1-spectral clustering
algorithm: a spectral clustering method using l1-regularization" (2022).

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
