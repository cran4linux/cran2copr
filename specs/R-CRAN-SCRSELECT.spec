%global packname  SCRSELECT
%global packver   1.3-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.3
Release:          2%{?dist}
Summary:          Performs Bayesian Variable Selection on the Covariates in aSemi-Competing Risks Model

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.2
Requires:         R-core >= 3.2.2
BuildArch:        noarch
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-mvtnorm 

%description
Contains four functions used in the DIC-tau_g procedure. SCRSELECT() and
SCRSELECTRUN() uses Stochastic Search Variable Selection to select
important covariates in the three hazard functions of a semi-competing
risks model. These functions perform the Gibbs sampler for variable
selection and a Metropolis-Hastings-Green sampler for the number of split
points and parameters for the three baseline hazard function. The function
SCRSELECT() returns the posterior sample of all quantities sampled in the
Gibbs sampler after a burn-in period to a desired file location, while the
function SCRSELECTRUN() returns posterior values of important quantities
to the DIC-Tau_g procedure in a list. The function DICTAUG() returns a
list containing the DIC values for the unique models visited by the
DIC-Tau_g grid search. The function ReturnModel() uses SCRSELECTRUN() and
DICTAUG() to return a summary of the posterior coefficient vectors for the
optimal model along with saving this posterior sample to a desired path
location.

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
