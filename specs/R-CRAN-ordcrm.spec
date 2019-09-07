%global packname  ordcrm
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Likelihood-Based Continual Reassessment Method (CRM) DoseFinding Designs

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.1
Requires:         R-core >= 3.3.1
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-rms 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-rms 

%description
Provides the setup and calculations needed to run a likelihood-based
continual reassessment method (CRM) dose finding trial and performs
simulations to assess design performance under various scenarios. 3 dose
finding designs are included in this package: ordinal proportional odds
model (POM) CRM, ordinal continuation ratio (CR) model CRM, and the binary
2-parameter logistic model CRM. These functions allow customization of
design characteristics to vary sample size, cohort sizes, target
dose-limiting toxicity (DLT) rates, discrete or continuous dose levels,
combining ordinal grades 0 and 1 into one category, and incorporate safety
and/or stopping rules. For POM and CR model designs, ordinal toxicity
grades are specified by common terminology criteria for adverse events
(CTCAE) version 4.0. Function 'pseudodata' creates the necessary starting
models for these 3 designs, and function 'nextdose' estimates the next
dose to test in a cohort of patients for a target DLT rate. We also
provide the function 'crmsimulations' to assess the performance of these 3
dose finding designs under various scenarios.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
