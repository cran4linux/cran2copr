%global packname  mederrRank
%global packver   0.0.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.8
Release:          3%{?dist}
Summary:          Bayesian Methods for Identifying the Most Harmful MedicationErrors

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-BB 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-CRAN-BB 
Requires:         R-methods 
Requires:         R-CRAN-numDeriv 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-stats 

%description
Two distinct but related statistical approaches to the problem of
identifying the combinations of medication error characteristics that are
more likely to result in harm are implemented in this package: 1) a
Bayesian hierarchical model with optimal Bayesian ranking on the log odds
of harm, and 2) an empirical Bayes model that estimates the ratio of the
observed count of harm to the count that would be expected if error
characteristics and harm were independent. In addition, for the Bayesian
hierarchical model, the package provides functions to assess the
sensitivity of results to different specifications of the random effects
distributions.

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
