%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  maotai
%global packver   0.2.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.7
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Matrix Algebra, Optimization and Inference

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-RSpectra 
BuildRequires:    R-CRAN-Rtsne 
BuildRequires:    R-CRAN-RANN 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-labdsv 
BuildRequires:    R-CRAN-shapes 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-fastcluster 
BuildRequires:    R-CRAN-dbscan 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-gsignal 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppDist 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-RSpectra 
Requires:         R-CRAN-Rtsne 
Requires:         R-CRAN-RANN 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-labdsv 
Requires:         R-CRAN-shapes 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-fastcluster 
Requires:         R-CRAN-dbscan 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-gsignal 

%description
Matrix is an universal and sometimes primary object/unit in applied
mathematics and statistics. We provide a number of algorithms for selected
problems in optimization and statistical inference. For general exposition
to the topic with focus on statistical context, see the book by Banerjee
and Roy (2014, ISBN:9781420095388).

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
