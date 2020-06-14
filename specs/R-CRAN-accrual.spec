%global packname  accrual
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          2%{?dist}
Summary:          Bayesian Accrual Prediction

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.3
Requires:         R-core >= 3.1.3
BuildArch:        noarch
BuildRequires:    R-CRAN-tcltk2 
BuildRequires:    R-CRAN-fgui 
BuildRequires:    R-CRAN-SMPracticals 
Requires:         R-CRAN-tcltk2 
Requires:         R-CRAN-fgui 
Requires:         R-CRAN-SMPracticals 

%description
Subject recruitment for medical research is challenging. Slow patient
accrual leads to delay in research. Accrual monitoring during the process
of recruitment is critical. Researchers need reliable tools to manage the
accrual rate. We developed a Bayesian method that integrates researcher's
experience on previous trials and data from the current study, providing
reliable prediction on accrual rate for clinical studies. In this R
package, we present functions for Bayesian accrual prediction which can be
easily used by statisticians and clinical researchers.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
