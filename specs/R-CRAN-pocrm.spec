%global packname  pocrm
%global packver   0.12
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.12
Release:          1%{?dist}
Summary:          Dose Finding in Drug Combination Phase I Trials Using PO-CRM

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dfcrm 
BuildRequires:    R-nnet 
BuildRequires:    R-stats 
Requires:         R-CRAN-dfcrm 
Requires:         R-nnet 
Requires:         R-stats 

%description
Provides functions to implement and simulate the partial order continual
reassessment method (PO-CRM) of Wages, Conaway and O'Quigley (2011)
<doi:10.1177/1740774511408748> for use in Phase I trials of combinations
of agents. Provides a function for generating a set of initial guesses
(skeleton) for the toxicity probabilities at each combination that
correspond to the set of possible orderings of the toxicity probabilities
specified by the user.

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
