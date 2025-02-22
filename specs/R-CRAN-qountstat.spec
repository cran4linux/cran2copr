%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  qountstat
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Statistical Analysis of Count Data and Quantal Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-multcomp 
Requires:         R-CRAN-multcomp 

%description
Methods for statistical analysis of count data and quantal data. For the
analysis of count data an implementation of the Closure Principle
Computational Approach Test ("CPCAT") is provided (Lehmann, R et al.
(2016) <doi:10.1007/s00477-015-1079-4>), as well as an implementation of a
"Dunnett GLM" approach using a Quasi-Poisson regression (Hothorn, L,
Kluxen, F (2020) <doi:10.1101/2020.01.15.907881>). For the analysis of
quantal data an implementation of the Closure Principle
Fisher–Freeman–Halton test ("CPFISH") is provided (Lehmann, R et al.
(2018) <doi:10.1007/s00477-017-1392-1>). P-values and no/lowest observed
(adverse) effect concentration values are calculated. All implemented
methods include further functions to evaluate the power and the minimum
detectable difference using a bootstrapping approach.

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
