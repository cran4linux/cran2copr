%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BGGM
%global packver   2.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Gaussian Graphical Models

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildRequires:    R-CRAN-MASS >= 7.3.51.5
BuildRequires:    R-CRAN-ggplot2 >= 3.2.1
BuildRequires:    R-CRAN-sna >= 2.5
BuildRequires:    R-CRAN-GGally >= 1.4.0
BuildRequires:    R-CRAN-BFpack >= 1.2.3
BuildRequires:    R-CRAN-network >= 1.15
BuildRequires:    R-CRAN-Rcpp >= 1.0.4.6
BuildRequires:    R-CRAN-reshape >= 0.8.8
BuildRequires:    R-CRAN-ggridges >= 0.5.1
BuildRequires:    R-CRAN-mvnfast >= 0.2.5
BuildRequires:    R-CRAN-Rdpack >= 0.11
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppArmadillo 
BuildRequires:    R-CRAN-RcppDist 
BuildRequires:    R-CRAN-RcppProgress 
Requires:         R-CRAN-MASS >= 7.3.51.5
Requires:         R-CRAN-ggplot2 >= 3.2.1
Requires:         R-CRAN-sna >= 2.5
Requires:         R-CRAN-GGally >= 1.4.0
Requires:         R-CRAN-BFpack >= 1.2.3
Requires:         R-CRAN-network >= 1.15
Requires:         R-CRAN-Rcpp >= 1.0.4.6
Requires:         R-CRAN-reshape >= 0.8.8
Requires:         R-CRAN-ggridges >= 0.5.1
Requires:         R-CRAN-mvnfast >= 0.2.5
Requires:         R-CRAN-Rdpack >= 0.11
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 

%description
Fit Bayesian Gaussian graphical models. The methods are separated into two
Bayesian approaches for inference: hypothesis testing and estimation.
There are extensions for confirmatory hypothesis testing, comparing
Gaussian graphical models, and node wise predictability. These methods
were recently introduced in the Gaussian graphical model literature,
including Williams (2019) <doi:10.31234/osf.io/x8dpr>, Williams and Mulder
(2019) <doi:10.31234/osf.io/ypxd8>, Williams, Rast, Pericchi, and Mulder
(2019) <doi:10.31234/osf.io/yt386>.

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
