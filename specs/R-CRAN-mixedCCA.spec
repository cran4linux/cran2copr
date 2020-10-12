%global packname  mixedCCA
%global packver   1.4.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.3
Release:          1%{?dist}%{?buildtag}
Summary:          Sparse Canonical Correlation Analysis for High-Dimensional Mixed Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.1
Requires:         R-core >= 3.0.1
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-pcaPP 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-fMultivar 
BuildRequires:    R-CRAN-mnormt 
BuildRequires:    R-CRAN-irlba 
BuildRequires:    R-CRAN-chebpol 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-stats 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-pcaPP 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-fMultivar 
Requires:         R-CRAN-mnormt 
Requires:         R-CRAN-irlba 
Requires:         R-CRAN-chebpol 

%description
Semi-parametric approach for sparse canonical correlation analysis which
can handle mixed data types: continuous, binary and truncated continuous.
Bridge functions are provided to connect Kendall's tau to latent
correlation under the Gaussian copula model. The methods are described in
Yoon, Carroll and Gaynanova (2020) <doi:10.1093/biomet/asaa007> and Yoon,
Müller and Gaynanova (2020) <arXiv:2006.13875>.

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
