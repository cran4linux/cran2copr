%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rbreak
%global packver   1.0.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.7
Release:          1%{?dist}%{?buildtag}
Summary:          Restricted Structural Change Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.3.0
Requires:         R-core >= 4.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-stats 
Requires:         R-CRAN-MASS 
Requires:         R-stats 

%description
Methods for detecting structural breaks and estimating break locations for
linear multiple regression models under general linear restrictions on the
coefficient vector. Restrictions can be within regimes, across regimes, or
both, and are supported in two forms: an affine parameterization (Form A:
delta = S*theta + s) and explicit linear constraints (Form B: R*delta =
r). Provides break date estimation with confidence intervals, a restricted
sup-F test for the null of no structural change, simulation of critical
values by Monte Carlo, and a bootstrap restart procedure to reduce the
risk of convergence to spurious local optima. Also implements a
generalized regression tree (linear model tree) procedure where each leaf
contains a linear regression model rather than a local average. Reference:
Perron, P., and Qu, Z. (2006). 'Estimating Restricted Structural Change
Models.' Journal of Econometrics, 134(2), 373-399.
<doi:10.1016/j.jeconom.2005.06.030>.

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
