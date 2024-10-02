%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GeodRegr
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Geodesic Regression

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS >= 7.3.51.6
BuildRequires:    R-stats >= 4.0.1
BuildRequires:    R-CRAN-zipfR >= 0.6.66
Requires:         R-CRAN-MASS >= 7.3.51.6
Requires:         R-stats >= 4.0.1
Requires:         R-CRAN-zipfR >= 0.6.66

%description
Provides a gradient descent algorithm to find a geodesic relationship
between real-valued independent variables and a manifold-valued dependent
variable (i.e. geodesic regression). Available manifolds are Euclidean
space, the sphere, hyperbolic space, and Kendall's 2-dimensional shape
space. Besides the standard least-squares loss, the least absolute
deviations, Huber, and Tukey biweight loss functions can also be used to
perform robust geodesic regression. Functions to help choose appropriate
cutoff parameters to maintain high efficiency for the Huber and Tukey
biweight estimators are included, as are functions for generating random
tangent vectors from the Riemannian normal distributions on the sphere and
hyperbolic space. The n-sphere is a n-dimensional manifold: we represent
it as a sphere of radius 1 and center 0 embedded in (n+1)-dimensional
space. Using the hyperboloid model of hyperbolic space, n-dimensional
hyperbolic space is embedded in (n+1)-dimensional Minkowski space as the
upper sheet of a hyperboloid of two sheets. Kendall's 2D shape space with
K landmarks is of real dimension 2K-4; preshapes are represented as
complex K-vectors with mean 0 and magnitude 1. Details are described in
Shin, H.-Y. and Oh, H.-S. (2020) <arXiv:2007.04518>. Also see Fletcher, P.
T. (2013) <doi:10.1007/s11263-012-0591-y>.

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
