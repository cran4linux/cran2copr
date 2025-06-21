%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  wordvector
%global packver   0.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.1
Release:          1%{?dist}%{?buildtag}
Summary:          Word and Document Vector Models

License:          Apache License (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-quanteda >= 4.1.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-proxyC 
BuildRequires:    R-CRAN-RSpectra 
BuildRequires:    R-CRAN-irlba 
BuildRequires:    R-CRAN-rsvd 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-quanteda >= 4.1.0
Requires:         R-methods 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-proxyC 
Requires:         R-CRAN-RSpectra 
Requires:         R-CRAN-irlba 
Requires:         R-CRAN-rsvd 

%description
Create dense vector representation of words and documents using
'quanteda'. Currently implements Word2vec (Mikolov et al., 2013)
<doi:10.48550/arXiv.1310.4546> and Latent Semantic Analysis (Deerwester et
al., 1990)
<doi:10.1002/(SICI)1097-4571(199009)41:6%%3C391::AID-ASI1%%3E3.0.CO;2-9>.

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
