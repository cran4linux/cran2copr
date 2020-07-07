%global packname  ltbayes
%global packver   0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4
Release:          3%{?dist}
Summary:          Simulation-Based Bayesian Inference for Latent Traits of ItemResponse Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.1
Requires:         R-core >= 3.3.1
BuildRequires:    R-CRAN-numDeriv >= 2016.8.1
BuildRequires:    R-CRAN-MHadaptive >= 1.1.8
BuildRequires:    R-CRAN-mcmc >= 0.9.4
Requires:         R-CRAN-numDeriv >= 2016.8.1
Requires:         R-CRAN-MHadaptive >= 1.1.8
Requires:         R-CRAN-mcmc >= 0.9.4

%description
Functions for simulating realizations from the posterior distribution of a
latent trait of an item response model. Distributions are conditional on
one or a subset of response patterns (e.g., sum scores). Functions for
computing likelihoods, Fisher and observed information, posterior modes,
and profile likelihood confidence intervals are also included. These
functions are designed to be easily amenable to user-specified models.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
