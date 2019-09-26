%global packname  surrosurv
%global packver   1.1.25
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.25
Release:          1%{?dist}
Summary:          Evaluation of Failure Time Surrogate Endpoints in IndividualPatient Data Meta-Analyses

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-optimx 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-copula 
BuildRequires:    R-CRAN-eha 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-MASS 
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-msm 
BuildRequires:    R-CRAN-mvmeta 
BuildRequires:    R-CRAN-optextras 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-parfm 
BuildRequires:    R-survival 
BuildRequires:    R-CRAN-SurvCorr 
Requires:         R-stats 
Requires:         R-CRAN-optimx 
Requires:         R-grDevices 
Requires:         R-CRAN-copula 
Requires:         R-CRAN-eha 
Requires:         R-CRAN-lme4 
Requires:         R-MASS 
Requires:         R-Matrix 
Requires:         R-CRAN-msm 
Requires:         R-CRAN-mvmeta 
Requires:         R-CRAN-optextras 
Requires:         R-parallel 
Requires:         R-CRAN-parfm 
Requires:         R-survival 
Requires:         R-CRAN-SurvCorr 

%description
Provides functions for the evaluation of surrogate endpoints when both the
surrogate and the true endpoint are failure time variables. The approaches
implemented are: (1) the two-step approach (Burzykowski et al, 2001)
<DOI:10.1111/1467-9876.00244> with a copula model (Clayton, Plackett,
Hougaard) at the first step and either a linear regression of log-hazard
ratios at the second step (either adjusted or not for measurement error);
(2) mixed proportional hazard models estimated via mixed Poisson GLM
(Rotolo et al, 2019 <DOI:10.1177/0962280217718582>).

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
