%global packname  simsurv
%global packver   0.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          2%{?dist}
Summary:          Simulate Survival Data

License:          GPL (>= 3) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-methods 
Requires:         R-stats 

%description
Simulate survival times from standard parametric survival distributions
(exponential, Weibull, Gompertz), 2-component mixture distributions, or a
user-defined hazard, log hazard, cumulative hazard, or log cumulative
hazard function. Baseline covariates can be included under a proportional
hazards assumption. Time dependent effects (i.e. non-proportional hazards)
can be included by interacting covariates with linear time or a
user-defined function of time. Clustered event times are also
accommodated. The 2-component mixture distributions can allow for a
variety of flexible baseline hazard functions reflecting those seen in
practice. If the user wishes to provide a user-defined hazard or log
hazard function then this is possible, and the resulting cumulative hazard
function does not need to have a closed-form solution. Note that this
package is modelled on the 'survsim' package available in the 'Stata'
software (see Crowther and Lambert (2012)
<http://www.stata-journal.com/sjpdf.html?articlenum=st0275> or Crowther
and Lambert (2013) <doi:10.1002/sim.5823>).

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
