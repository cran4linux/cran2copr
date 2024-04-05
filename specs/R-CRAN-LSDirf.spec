%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  LSDirf
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Impulse-Response Function Analysis for Agent-Based Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-partykit 
BuildRequires:    R-CRAN-randomForest 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-gplots 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-partykit 
Requires:         R-CRAN-randomForest 

%description
Performing impulse-response function (IRF) analysis of relevant variables
of agent-based simulation models, in particular for models described in
'LSD' format. Based on the data produced by the simulation model, it
performs both linear and state-dependent IRF analysis, providing the tools
required by the Counterfactual Monte Carlo (CMC) methodology (Amendola and
Pereira (2024) <doi:10.2139/ssrn.4740360>), including state identification
and sensitivity. CMC proposes retrieving the causal effect of shocks by
exploiting the opportunity to directly observe the counterfactual in a
fully controlled experimental setup. 'LSD' (Laboratory for Simulation
Development) is free software available at <https://www.labsimdev.org/>).

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
