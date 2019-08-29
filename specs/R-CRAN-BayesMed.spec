%global packname  BayesMed
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Default Bayesian Hypothesis Tests for Correlation, PartialCorrelation, and Mediation

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.12.1
Requires:         R-core >= 2.12.1
BuildArch:        noarch
BuildRequires:    R-CRAN-R2jags 
BuildRequires:    R-CRAN-QRM 
BuildRequires:    R-CRAN-polspline 
BuildRequires:    R-CRAN-MCMCpack 
Requires:         R-CRAN-R2jags 
Requires:         R-CRAN-QRM 
Requires:         R-CRAN-polspline 
Requires:         R-CRAN-MCMCpack 

%description
Default Bayesian hypothesis tests for correlation, partial correlation,
and mediation

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
