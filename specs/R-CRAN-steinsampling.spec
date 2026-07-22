%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  steinsampling
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Kernel Stein Discrepancy Goodness-of-Fit and Stein Sampling Tools

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-mvtnorm 

%description
Provides Stein-discrepancy goodness-of-fit tests and Stein-method-based
sampling tools. The tests include kernel Stein discrepancy U- and
V-statistics following Liu et al. (2016) <doi:10.48550/arXiv.1602.03253>
and Chwialkowski et al. (2016) <doi:10.48550/arXiv.1602.02964>, plus the
finite set Stein discrepancy test of Jitkrittum et al. (2017)
<doi:10.48550/arXiv.1705.07673>. The sampling tools include Stein
thinning, Stein Points, Stein Point Markov chain Monte Carlo, and Stein
variational gradient descent following Riabiz et al. (2022)
<doi:10.48550/arXiv.2005.03952>, Chen et al. (2018)
<doi:10.48550/arXiv.1803.10161>, Chen et al. (2019)
<doi:10.48550/arXiv.1905.03673>, and Liu and Wang (2016)
<doi:10.48550/arXiv.1608.04471>. Gaussian mixture utilities are included
for simulation, likelihoods, posterior probabilities, scores, and plots.

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
