%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BsplineQuantReg
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          'Constrained Quantile Regression with B-Splines'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-CVXR 
Requires:         R-CRAN-CVXR 

%description
Quantile regression with B-splines under shape constraints. The initial
version with cubic splines is now augmented with splines of degree 1 to 4.
Constraints for degrees 3 (monotone) and 4 (monotone and convex) use the
Karlin-Studden SOCP characterization for the sign of the polynomial, while
other constraints applied at the knots are added as linear problems. The
method for cubic splines is described in Abbes (2026)
<doi:10.5281/zenodo.17427913>. Other formulations are simple consequences
of the other given references. This R implementation is intended for
demonstration and prototyping. All B-spline and polynomial functions have
been rewritten for consistency. An equivalent Python package is available
at <https://pypi.org/project/BsplineQuantRegpy/>.

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
