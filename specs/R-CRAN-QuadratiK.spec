%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  QuadratiK
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Collection of Methods Constructed using Kernel-Based Quadratic Distances

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppEigen 
BuildRequires:    R-CRAN-sn 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-movMF 
BuildRequires:    R-CRAN-rlecuyer 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-Tinflex 
BuildRequires:    R-CRAN-ggpp 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-clusterRepro 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-rrcov 
BuildRequires:    R-CRAN-cluster 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-RcppEigen 
Requires:         R-CRAN-sn 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-moments 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-movMF 
Requires:         R-CRAN-rlecuyer 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-Tinflex 
Requires:         R-CRAN-ggpp 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-clusterRepro 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-rrcov 
Requires:         R-CRAN-cluster 

%description
It includes test for multivariate normality, test for uniformity on the
Sphere, non-parametric two- and k-sample tests, random generation of
points from the Poisson kernel-based density and clustering algorithm for
spherical data. For more information see Saraceno, G., Markatou, M.,
Mukhopadhyay, R., Golzy, M. (2024) <arxiv:2402.02290>, Ding, Y., Markatou,
M., Saraceno, G. (2023) <doi:10.5705/ss.202022.0347>, and Golzy, M.,
Markatou, M. (2020) <doi:10.1080/10618600.2020.1740713>.

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
