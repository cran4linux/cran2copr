%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  genMCMCDiag
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Generalized Convergence Diagnostics for Difficult MCMC Algorithms

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.0.0
BuildRequires:    R-CRAN-knitr >= 1.30
BuildRequires:    R-CRAN-mcmcse >= 1.0.0
BuildRequires:    R-CRAN-coda >= 0.19.0
BuildRequires:    R-CRAN-lifecycle 
Requires:         R-CRAN-ggplot2 >= 3.0.0
Requires:         R-CRAN-knitr >= 1.30
Requires:         R-CRAN-mcmcse >= 1.0.0
Requires:         R-CRAN-coda >= 0.19.0
Requires:         R-CRAN-lifecycle 

%description
Trace plots and convergence diagnostics for Markov Chain Monte Carlo
(MCMC) algorithms on highly multivariate or unordered spaces. Methods
outlined in a forthcoming paper.

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
