%global packname  ubiquity
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          PKPD, PBPK, and Systems Pharmacology Modeling Tools

License:          BSD_2_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-officer >= 0.3.5
BuildRequires:    R-CRAN-deSolve 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-doRNG 
BuildRequires:    R-CRAN-flextable 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gdata 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-optimx 
BuildRequires:    R-CRAN-PKNCA 
BuildRequires:    R-CRAN-pso 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-rhandsontable 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-shiny 
Requires:         R-CRAN-officer >= 0.3.5
Requires:         R-CRAN-deSolve 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-doRNG 
Requires:         R-CRAN-flextable 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-gridExtra 
Requires:         R-grid 
Requires:         R-CRAN-gdata 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-knitr 
Requires:         R-MASS 
Requires:         R-CRAN-optimx 
Requires:         R-CRAN-PKNCA 
Requires:         R-CRAN-pso 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-rhandsontable 
Requires:         R-CRAN-rstudioapi 
Requires:         R-stats 
Requires:         R-CRAN-shiny 

%description
Complete work flow for the analysis of pharmacokinetic pharmacodynamic
(PKPD), physiologically-based pharmacokinetic (PBPK) and systems
pharmacology models including: creation of ordinary differential
equation-based models, pooled parameter estimation, individual/population
based simulations, rule-based simulations for clinical trial design and
modeling assays, deployment with a customizable 'Shiny' app, and
non-compartmental analysis. System-specific analysis templates can be
generated and each element includes integrated reporting with
'PowerPoint'.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/exec
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/ubinc
%{rlibdir}/%{packname}/INDEX
