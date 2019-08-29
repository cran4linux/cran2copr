%global packname  currentSurvival
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Estimation of CCI and CLFS Functions

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.13.0
Requires:         R-core >= 2.13.0
BuildArch:        noarch
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-cmprsk 
Requires:         R-survival 
Requires:         R-CRAN-cmprsk 

%description
The currentSurvival package contains functions for the estimation of the
current cumulative incidence (CCI) and the current leukaemia-free survival
(CLFS). The CCI is the probability that a patient is alive and in any
disease remission (e.g. complete cytogenetic remission in chronic myeloid
leukaemia) after initiating his or her therapy (e.g. tyrosine kinase
therapy for chronic myeloid leukaemia). The CLFS is the probability that a
patient is alive and in any disease remission after achieving the first
disease remission.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
