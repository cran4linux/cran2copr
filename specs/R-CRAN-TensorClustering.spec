%global packname  TensorClustering
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Model-Based Tensor Clustering

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-tensr 
BuildRequires:    R-CRAN-rTensor 
BuildRequires:    R-CRAN-TRES 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-combinat 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-tensr 
Requires:         R-CRAN-rTensor 
Requires:         R-CRAN-TRES 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-combinat 
Requires:         R-CRAN-pracma 
Requires:         R-stats 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-Rcpp 

%description
Performs model-based tensor clustering methods including Tensor Gaussian
Mixture Model (TGMM) and Tensor Envelope Mixture Model (TEMM) by Deng and
Zhang (2021, tentatively accepted by Biometrics), Doubly-Enhanced EM
(DEEM) algorithm by Mai, Zhang, Pan and Deng (2021) <arXiv:2012.10032>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
