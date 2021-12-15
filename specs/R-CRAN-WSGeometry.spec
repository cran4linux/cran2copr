%global __brp_check_rpaths %{nil}
%global packname  WSGeometry
%global packver   1.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Geometric Tools Based on Balanced/Unbalanced Optimal Transport

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-transport 
BuildRequires:    R-CRAN-RSpectra 
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-CRAN-plot3D 
BuildRequires:    R-CRAN-imager 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-lpSolve 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-transport 
Requires:         R-CRAN-RSpectra 
Requires:         R-CRAN-expm 
Requires:         R-CRAN-plot3D 
Requires:         R-CRAN-imager 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-lpSolve 
Requires:         R-CRAN-Matrix 

%description
Includes a variety of methods to compute objects related to the
'Wasserstein distance' (also known as 'Kantorovich distance' or
'Earth-Mover distance'). The main effort of this package is to allow for
computations of 'Wasserstein barycenter' using regularised, unregularised
and stochastic methods. It also provides convenient wrappers to call the
'transport' package with more general inputs. Handy visual tools are
provided to showcase, barycenters, animations of optimal transport
geodesics and animations of principal components in the 'Wasserstein
space'. It also includes tools to compute 'Kantorovich-Rubinstein'
distances and barycenters.

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
