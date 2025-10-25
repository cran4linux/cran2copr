%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DTEAssurance
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Assurance Methods for Clinical Trials with a Delayed Treatment Effect

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-SHELF 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-nleqslv 
BuildRequires:    R-CRAN-nph 
BuildRequires:    R-CRAN-nphRCT 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-rjags 
BuildRequires:    R-CRAN-rpact 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-future.apply 
Requires:         R-CRAN-SHELF 
Requires:         R-CRAN-shiny 
Requires:         R-stats 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-nleqslv 
Requires:         R-CRAN-nph 
Requires:         R-CRAN-nphRCT 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-rjags 
Requires:         R-CRAN-rpact 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-future.apply 

%description
Provides functions for planning clinical trials subject to a delayed
treatment effect using assurance-based methods. Includes two 'shiny'
applications for interactive exploration, simulation, and visualisation of
trial designs and outcomes. The methodology is described in: Salsbury JA,
Oakley JE, Julious SA, Hampson LV (2024) "Assurance methods for designing
a clinical trial with a delayed treatment effect" <doi:10.1002/sim.10136>,
Salsbury JA, Oakley JE, Julious SA, Hampson LV (2024) "Adaptive clinical
trial design with delayed treatment effects using elicited prior
distributions" <doi:10.48550/arXiv.2509.07602>.

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
