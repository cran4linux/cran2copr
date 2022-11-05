%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mixedLSR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Mixed, Low-Rank, and Sparse Multivariate Regression on High-Dimensional Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-grpreg 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-grpreg 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-MASS 
Requires:         R-stats 
Requires:         R-CRAN-ggplot2 

%description
Mixed, low-rank, and sparse multivariate regression ('mixedLSR') provides
tools for performing mixture regression when the coefficient matrix is
low-rank and sparse. 'mixedLSR' allows subgroup identification by
alternating optimization with simulated annealing to encourage global
optimum convergence. This method is data-adaptive, automatically
performing parameter selection to identify low-rank substructures in the
coefficient matrix.

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
