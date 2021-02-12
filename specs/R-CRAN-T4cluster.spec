%global packname  T4cluster
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Tools for Cluster Analysis

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp >= 1.0.5
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-Rdimtools 
BuildRequires:    R-CRAN-ADMM 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-fda 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-lpSolve 
BuildRequires:    R-CRAN-maotai 
BuildRequires:    R-CRAN-mclustcomp 
BuildRequires:    R-CRAN-rstiefel 
BuildRequires:    R-CRAN-scatterplot3d 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp >= 1.0.5
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-Rdimtools 
Requires:         R-CRAN-ADMM 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-fda 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-lpSolve 
Requires:         R-CRAN-maotai 
Requires:         R-CRAN-mclustcomp 
Requires:         R-CRAN-rstiefel 
Requires:         R-CRAN-scatterplot3d 
Requires:         R-stats 
Requires:         R-utils 

%description
Cluster analysis is one of the most fundamental problems in data science.
We provide a variety of algorithms from clustering to the learning on the
space of partitions. See Hennig, Meila, and Rocci (2016,
ISBN:9781466551886) for general exposition to cluster analysis.

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
