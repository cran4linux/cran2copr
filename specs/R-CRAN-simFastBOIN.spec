%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  simFastBOIN
%global packver   1.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          Fast Bayesian Optimal Interval Design for Phase I Dose-Finding Trials

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-kableExtra 
BuildRequires:    R-CRAN-Iso 
BuildRequires:    R-stats 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-kableExtra 
Requires:         R-CRAN-Iso 
Requires:         R-stats 

%description
Conducting Bayesian Optimal Interval (BOIN) design for phase I
dose-finding trials. 'simFastBOIN' provides functions for pre-computing
decision tables, conducting trial simulations, and evaluating operating
characteristics. The package uses vectorized operations and the
Iso::pava() function for isotonic regression to achieve efficient
performance while maintaining full compatibility with BOIN methodology.
Version 1.3.2 adds p_saf and p_tox parameters for customizable safety and
toxicity thresholds. Version 1.3.1 fixes Date field. Version 1.2.1 adds
comprehensive 'roxygen2' documentation and enhanced print formatting with
flexible table output options. Version 1.2.0 integrated C-based PAVA for
isotonic regression. Version 1.1.0 introduced conservative MTD selection
(boundMTD) and flexible early stopping rules (n_earlystop_rule). Methods
are described in Liu and Yuan (2015) <doi:10.1111/rssc.12089>.

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
