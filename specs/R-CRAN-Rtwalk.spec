%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Rtwalk
%global packver   2.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          An MCMC Sampler Using the t-Walk Algorithm

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildRequires:    R-CRAN-codetools 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-codetools 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-coda 
Requires:         R-CRAN-Rcpp 

%description
Implements the t-walk algorithm, a general-purpose, self-adjusting Markov
Chain Monte Carlo (MCMC) sampler for continuous distributions as described
by Christen & Fox (2010) <doi:10.1214/10-BA603>. The t-walk requires no
tuning and is robust for a wide range of target distributions, including
high-dimensional and multimodal problems. The sampler is implemented in
C++ and validated against a pure R reference implementation of the
published algorithm. The package supports reproducible parallel chains,
continuation of runs, single transitions for hybrid samplers, and
convergence diagnostics following Vehtari et al. (2021)
<doi:10.1214/20-BA1221>.

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
