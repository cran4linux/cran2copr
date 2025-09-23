%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  NetworkDistance
%global packver   0.3.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.6
Release:          1%{?dist}%{?buildtag}
Summary:          Distance Measures for Networks

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-RSpectra 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-graphon 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-network 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-RSpectra 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-graphon 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-network 
Requires:         R-CRAN-pracma 
Requires:         R-utils 

%description
Network is a prevalent form of data structure in many fields. As an object
of analysis, many distance or metric measures have been proposed to define
the concept of similarity between two networks. We provide a number of
distance measures for networks. See Jurman et al (2011)
<doi:10.3233/978-1-60750-692-8-227> for an overview on spectral class of
inter-graph distance measures.

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
