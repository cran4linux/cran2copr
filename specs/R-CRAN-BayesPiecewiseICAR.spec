%global packname  BayesPiecewiseICAR
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          2%{?dist}
Summary:          Hierarchical Bayesian Model for a Hazard Function

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-mvtnorm 

%description
Fits a piecewise exponential hazard to survival data using a Hierarchical
Bayesian model with an Intrinsic Conditional Autoregressive formulation
for the spatial dependency in the hazard rates for each piece. This
function uses Metropolis- Hastings-Green MCMC to allow the number of split
points to vary. This function outputs graphics that display the histogram
of the number of split points and the trace plots of the hierarchical
parameters. The function outputs a list that contains the posterior
samples for the number of split points, the location of the split points,
and the log hazard rates corresponding to these splits. Additionally, this
outputs the posterior samples of the two hierarchical parameters, Mu and
Sigma^2.

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
