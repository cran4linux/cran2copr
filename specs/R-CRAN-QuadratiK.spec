%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  QuadratiK
%global packver   1.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Collection of Methods Constructed using Kernel-Based Quadratic Distances

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppEigen 
BuildRequires:    R-CRAN-rlecuyer 
BuildRequires:    R-CRAN-sn 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-rrcov 
BuildRequires:    R-CRAN-scatterplot3d 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggpubr 
Requires:         R-methods 
Requires:         R-CRAN-moments 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-RcppEigen 
Requires:         R-CRAN-rlecuyer 
Requires:         R-CRAN-sn 
Requires:         R-stats 
Requires:         R-CRAN-rrcov 
Requires:         R-CRAN-scatterplot3d 

%description
It includes test for multivariate normality, test for uniformity on the
d-dimensional Sphere, non-parametric two- and k-sample tests, random
generation of points from the Poisson kernel-based density and clustering
algorithm for spherical data. For more information see Saraceno G.,
Markatou M., Mukhopadhyay R. and Golzy M. (2024)
<doi:10.48550/arXiv.2402.02290> Markatou, M. and Saraceno, G. (2024)
<doi:10.48550/arXiv.2407.16374>, Ding, Y., Markatou, M. and Saraceno, G.
(2023) <doi:10.5705/ss.202022.0347>, and Golzy, M. and Markatou, M. (2020)
<doi:10.1080/10618600.2020.1740713>.

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
