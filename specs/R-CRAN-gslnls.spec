%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gslnls
%global packver   1.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.0
Release:          1%{?dist}%{?buildtag}
Summary:          GSL Multi-Start Nonlinear Least-Squares Fitting

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    gsl-devel
BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Matrix 
Requires:         R-stats 
Requires:         R-CRAN-Matrix 

%description
An R interface to weighted nonlinear least-squares optimization with the
GNU Scientific Library (GSL), see M. Galassi et al. (2009,
ISBN:0954612078). The available trust region methods include the
Levenberg-Marquardt algorithm with and without geodesic acceleration, the
Steihaug-Toint conjugate gradient algorithm for large systems and several
variants of Powell's dogleg algorithm. Multi-start optimization based on
quasi-random samples is implemented using a modified version of the
algorithm in Hickernell and Yuan (1997, OR Transactions). Robust nonlinear
regression can be performed using various robust loss functions, in which
case the optimization problem is solved by iterative reweighted least
squares (IRLS). Bindings are provided to tune a number of parameters
affecting the low-level aspects of the trust region algorithms. The
interface mimics R's nls() function and returns model objects inheriting
from the same class.

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
