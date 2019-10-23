%global packname  FamEvent
%global packver   2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0
Release:          1%{?dist}
Summary:          Family Age-at-Onset Data Simulation and Penetrance Estimation

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-survival 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-kinship2 
BuildRequires:    R-CRAN-truncnorm 
BuildRequires:    R-CRAN-eha 
BuildRequires:    R-CRAN-pracma 
Requires:         R-survival 
Requires:         R-MASS 
Requires:         R-CRAN-kinship2 
Requires:         R-CRAN-truncnorm 
Requires:         R-CRAN-eha 
Requires:         R-CRAN-pracma 

%description
Simulates age-at-onset traits associated with a segregating major gene in
family data obtained from population-based, clinic-based, or multi-stage
designs. Appropriate ascertainment correction is utilized to estimate
age-dependent penetrance functions either parametrically from the fitted
model or nonparametrically from the data. The Expectation and Maximization
algorithm can infer missing genotypes and carrier probabilities estimated
from family's genotype and phenotype information or from a fitted model.
Plot functions include pedigrees of simulated families and predicted
penetrance curves based on specified parameter values.

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
