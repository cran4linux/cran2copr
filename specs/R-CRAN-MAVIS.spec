%global packname  MAVIS
%global packver   1.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.3
Release:          3%{?dist}
Summary:          Meta Analysis via Shiny

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.3
Requires:         R-core >= 3.0.3
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyAce 
BuildRequires:    R-CRAN-metafor 
BuildRequires:    R-CRAN-MAc 
BuildRequires:    R-CRAN-MAd 
BuildRequires:    R-CRAN-quantreg 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-compute.es 
BuildRequires:    R-CRAN-SCMA 
BuildRequires:    R-CRAN-SCRT 
BuildRequires:    R-CRAN-irr 
BuildRequires:    R-CRAN-shinyBS 
BuildRequires:    R-CRAN-weightr 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyAce 
Requires:         R-CRAN-metafor 
Requires:         R-CRAN-MAc 
Requires:         R-CRAN-MAd 
Requires:         R-CRAN-quantreg 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-compute.es 
Requires:         R-CRAN-SCMA 
Requires:         R-CRAN-SCRT 
Requires:         R-CRAN-irr 
Requires:         R-CRAN-shinyBS 
Requires:         R-CRAN-weightr 

%description
Interactive shiny application for running a meta-analysis, provides
support for both random effects and fixed effects models with the
'metafor' package. Additional support is included for calculating effect
sizes plus support for single case designs, graphical output, and
detecting publication bias.

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
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/aRma
%doc %{rlibdir}/%{packname}/shiny
%{rlibdir}/%{packname}/INDEX
