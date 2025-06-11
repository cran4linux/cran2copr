%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  boinet
%global packver   1.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Conduct Simulation Study of Bayesian Optimal Interval Design with BOIN-ET Family

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Iso 
BuildRequires:    R-CRAN-mfp 
BuildRequires:    R-CRAN-copula 
BuildRequires:    R-CRAN-gt 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-Iso 
Requires:         R-CRAN-mfp 
Requires:         R-CRAN-copula 
Requires:         R-CRAN-gt 
Requires:         R-CRAN-tibble 

%description
Bayesian optimal interval based on both efficacy and toxicity outcomes
(BOIN-ET) design is a model-assisted oncology phase I/II trial design,
aiming to establish an optimal biological dose accounting for efficacy and
toxicity in the framework of dose-finding. Some extensions of BOIN-ET
design are also available to allow for time-to-event efficacy and toxicity
outcomes based on cumulative and pending data (time-to-event BOIN-ET:
TITE-BOIN-ET), ordinal graded efficacy and toxicity outcomes (generalized
BOIN-ET: gBOIN-ET), and their combination (TITE-gBOIN-ET). 'boinet' is a
package to implement the BOIN-ET design family and supports the conduct of
simulation studies to assess operating characteristics of BOIN-ET,
TITE-BOIN-ET, gBOIN-ET, and TITE-gBOIN-ET, where users can choose design
parameters in flexible and straightforward ways depending on their own
application.

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
