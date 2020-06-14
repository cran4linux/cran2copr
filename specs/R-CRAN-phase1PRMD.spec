%global packname  phase1PRMD
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          2%{?dist}
Summary:          Personalized Repeated Measurement Design for Phase I ClinicalTrials

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-coda >= 0.13
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-rjags 
BuildRequires:    R-CRAN-arrayhelpers 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-kableExtra 
BuildRequires:    R-CRAN-knitr 
Requires:         R-CRAN-coda >= 0.13
Requires:         R-CRAN-ggplot2 
Requires:         R-stats 
Requires:         R-CRAN-rjags 
Requires:         R-CRAN-arrayhelpers 
Requires:         R-MASS 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-kableExtra 
Requires:         R-CRAN-knitr 

%description
Implements Bayesian phase I repeated measurement design that accounts for
multidimensional toxicity endpoints and longitudinal efficacy measure from
multiple treatment cycles. The package provides flags to fit a variety of
model-based phase I design, including 1 stage models with or without
individualized dose modification, 3-stage models with or without
individualized dose modification, etc. Functions are provided to recommend
dosage selection based on the data collected in the available patient
cohorts and to simulate trial characteristics given design parameters.
Yin, Jun, et al. (2017) <doi:10.1002/sim.7134>.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
