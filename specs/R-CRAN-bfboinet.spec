%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  bfboinet
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Backfill Bayesian Optimal Interval Design Using Efficacy and Toxicity

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Iso 
BuildRequires:    R-CRAN-copula 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyselect 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-BOP2FE 
BuildRequires:    R-CRAN-boinet 
BuildRequires:    R-CRAN-BOIN 
Requires:         R-CRAN-Iso 
Requires:         R-CRAN-copula 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyselect 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-BOP2FE 
Requires:         R-CRAN-boinet 
Requires:         R-CRAN-BOIN 

%description
Implements the Backfill Bayesian Optimal Interval Design (BF-BOIN-ET), a
novel clinical trial methodology for dose optimization that simultaneously
consider both efficacy and toxicity outcome as described in (Takeda et al
(2025) <doi:10.1002/pst.2470>). The package has been extended to include a
seamless two-stage phase I/II trial design with backfill and joint
efficacy and toxicity monitoring as described in (Takeda et al (2026)
<doi:10.1002/pst.70092>).

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
