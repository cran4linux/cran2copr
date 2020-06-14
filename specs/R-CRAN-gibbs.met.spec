%global packname  gibbs.met
%global packver   1.1-3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.3
Release:          2%{?dist}
Summary:          Naive Gibbs Sampling with Metropolis Steps

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.5.1
Requires:         R-core >= 2.5.1
BuildArch:        noarch

%description
This package provides two generic functions for performing Markov chain
sampling in a naive way for a user-defined target distribution, which
involves only continuous variables. The function "gibbs_met" performs
Gibbs sampling with each 1-dimensional distribution sampled with
Metropolis update using Gaussian proposal distribution centered at the
previous state. The function "met_gaussian" updates the whole state with
Metropolis method using independent Gaussian proposal distribution
centered at the previous state. The sampling is carried out without
considering any special tricks for improving efficiency. This package is
aimed at only routine applications of MCMC in moderate-dimensional
problems.

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
