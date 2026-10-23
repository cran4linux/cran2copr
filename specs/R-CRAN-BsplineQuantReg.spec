%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BsplineQuantReg
%global packver   0.2.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.6
Release:          1%{?dist}%{?buildtag}
Summary:          'Constrained Quantile Regression with B-Splines'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.5.0
Requires:         R-core >= 4.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-CVXR 
BuildRequires:    R-CRAN-ECOSolveR 
BuildRequires:    R-utils 
Requires:         R-CRAN-CVXR 
Requires:         R-CRAN-ECOSolveR 
Requires:         R-utils 

%description
Quantile regression with B-splines under shape constraints. The initial
version with cubic splines, augmented with splines of degree 1 to 4, is
now able to handle all degrees (degree >= 6 without any constraint).
Constraints for degrees 3 (monotone), 4 (monotone and convex) and 5
(convex) use the Karlin-Studden SOCP characterization for the sign of the
polynomial (Karlin and Studden, 1966; Papp and Alizadeh, 2014), while
other constraints are added as linear problems. The method for monotone
constraints of cubic splines is described in Abbes (2025)
<doi:10.5281/zenodo.17427913>. For quartic splines, see other references
given in the README. All B-spline and polynomial functions have been
rewritten for consistency. This package provides a fully independent
original B-spline library for conversion between PP-form and B-spline
representation, evaluation, differentiation, callable and non-callable
objects, human-readable PP forms, and basis visualization, all based on De
Boor's theory. It also extends to multiple knots to capture singularities.
This feature is robust in the package, including for constrained
regression. This R implementation is intended for demonstration and
prototyping. An equivalent Python package is available at
<https://pypi.org/project/BsplineQuantRegpy/>.

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
