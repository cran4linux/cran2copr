%global packname  ubiquity
%global packver   1.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          PKPD, PBPK, and Systems Pharmacology Modeling Tools

License:          BSD_2_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-officer >= 0.3.7
BuildRequires:    R-CRAN-deSolve 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-flextable 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-optimx 
BuildRequires:    R-CRAN-PKNCA 
BuildRequires:    R-CRAN-pso 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-rhandsontable 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-shiny 
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-officer >= 0.3.7
Requires:         R-CRAN-deSolve 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-flextable 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-gridExtra 
Requires:         R-grid 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-optimx 
Requires:         R-CRAN-PKNCA 
Requires:         R-CRAN-pso 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-rhandsontable 
Requires:         R-CRAN-rstudioapi 
Requires:         R-CRAN-scales 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-shiny 

%description
Complete work flow for the analysis of pharmacokinetic pharmacodynamic
(PKPD), physiologically-based pharmacokinetic (PBPK) and systems
pharmacology models including: creation of ordinary differential
equation-based models, pooled parameter estimation, individual/population
based simulations, rule-based simulations for clinical trial design and
modeling assays, deployment with a customizable 'Shiny' app, and
non-compartmental analysis. System-specific analysis templates can be
generated and each element includes integrated reporting with 'PowerPoint'
and 'Word'.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
