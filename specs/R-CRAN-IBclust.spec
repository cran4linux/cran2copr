%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  IBclust
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Information Bottleneck Methods for Clustering Mixed-Type Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-np 
BuildRequires:    R-CRAN-rje 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-RcppEigen 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-np 
Requires:         R-CRAN-rje 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-RcppEigen 

%description
Implements multiple variants of the Information Bottleneck ('IB') method
for clustering datasets containing continuous, categorical
(nominal/ordinal) and mixed-type variables. The package provides
deterministic, agglomerative, generalized, and standard 'IB' clustering
algorithms that preserve relevant information while forming interpretable
clusters. The Deterministic Information Bottleneck is described in Costa
et al. (2024) <doi:10.48550/arXiv.2407.03389>. The standard 'IB' method
originates from Tishby et al. (2000) <doi:10.48550/arXiv.physics/0004057>,
the agglomerative variant from Slonim and Tishby (1999)
<https://papers.nips.cc/paper/1651-agglomerative-information-bottleneck>,
and the generalized 'IB' from Strouse and Schwab (2017)
<doi:10.1162/NECO_a_00961>.

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
