%global __brp_check_rpaths %{nil}
%global packname  loo
%global packver   2.5.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.5.1
Release:          1%{?dist}%{?buildtag}
Summary:          Efficient Leave-One-Out Cross-Validation and WAIC for Bayesian Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         pandoc
BuildRequires:    R-devel >= 3.1.2
Requires:         R-core >= 3.1.2
BuildArch:        noarch
BuildRequires:    R-CRAN-matrixStats >= 0.52
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
Requires:         R-CRAN-matrixStats >= 0.52
Requires:         R-CRAN-checkmate 
Requires:         R-parallel 
Requires:         R-stats 

%description
Efficient approximate leave-one-out cross-validation (LOO) for Bayesian
models fit using Markov chain Monte Carlo, as described in Vehtari,
Gelman, and Gabry (2017) <doi:10.1007/s11222-016-9696-4>. The
approximation uses Pareto smoothed importance sampling (PSIS), a new
procedure for regularizing importance weights. As a byproduct of the
calculations, we also obtain approximate standard errors for estimated
predictive errors and for the comparison of predictive errors between
models. The package also provides methods for using stacking and other
model weighting techniques to average Bayesian predictive distributions.

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
