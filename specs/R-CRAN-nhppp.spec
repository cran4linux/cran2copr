%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  nhppp
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Simulating Nonhomogeneous Poisson Point Processes

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Rcpp >= 1.0.12
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-rstream 
Requires:         R-CRAN-Rcpp >= 1.0.12
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-rstream 

%description
Simulates events from one dimensional nonhomogeneous Poisson point
processes (NHPPPs) as per Trikalinos and Sereda (2024,
<doi:10.48550/arXiv.2402.00358> and 2024,
<doi:10.1371/journal.pone.0311311>). Functions are based on three
algorithms that provably sample from a target NHPPP: the
time-transformation of a homogeneous Poisson process (of intensity one)
via the inverse of the integrated intensity function (Cinlar E, "Theory of
stochastic processes" (1975, ISBN:0486497996)); the generation of a
Poisson number of order statistics from a fixed density function; and the
thinning of a majorizing NHPPP via an acceptance-rejection scheme (Lewis
PAW, Shedler, GS (1979) <doi:10.1002/nav.3800260304>).

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
