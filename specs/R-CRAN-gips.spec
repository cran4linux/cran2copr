%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gips
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Gaussian Model Invariant by Permutation Symmetry

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-numbers 
BuildRequires:    R-CRAN-permutations 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-utils 
Requires:         R-CRAN-numbers 
Requires:         R-CRAN-permutations 
Requires:         R-CRAN-rlang 
Requires:         R-utils 

%description
Find the permutation symmetry group such that the covariance matrix of the
given data is invariant under it. Discovering such a permutation decreases
the number of observations needed to fit a Gaussian model, which is of
great use when it is smaller than the number of variables. Even if that is
not the case, the covariance matrix found with 'gips' approximates the
actual covariance with less statistical error. The methods implemented in
this package are described in Graczyk et al. (2022)
<doi:10.1214/22-AOS2174>.

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
