%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CoFM
%global packver   1.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Copula Factor Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-copula 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-stats 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-copula 
Requires:         R-CRAN-matrixcalc 
Requires:         R-stats 

%description
Provides tools for factor analysis in high-dimensional settings under
copula-based factor models. It includes functions to simulate factor-model
data with copula-distributed idiosyncratic errors (e.g., Clayton, Gumbel,
Frank, Student t and Gaussian copulas) and to perform diagnostic tests
such as the Kaiser-Meyer-Olkin measure and Bartlett's test of sphericity.
Estimation routines include principal component based factor analysis,
projected principal component analysis, and principal orthogonal
complement thresholding for large covariance matrix estimation. The
philosophy of the package is described in Guo G. (2023)
<doi:10.1007/s00180-022-01270-z>.

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
