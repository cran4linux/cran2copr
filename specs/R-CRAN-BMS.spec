%global packname  BMS
%global packver   0.3.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.4
Release:          3%{?dist}
Summary:          Bayesian Model Averaging Library

License:          Artistic-2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.5
Requires:         R-core >= 2.5
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-stats 

%description
Bayesian model averaging for linear models with a wide choice of
(customizable) priors. Built-in priors include coefficient priors (fixed,
flexible and hyper-g priors), 5 kinds of model priors, moreover model
sampling by enumeration or various MCMC approaches. Post-processing
functions allow for inferring posterior inclusion and model probabilities,
various moments, coefficient and predictive densities. Plotting functions
available for posterior model size, MCMC convergence, predictive and
coefficient densities, best models representation, BMA comparison.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
