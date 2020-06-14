%global packname  relabeLoadings
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          2%{?dist}
Summary:          Relabel Loadings from MCMC Output for Confirmatory FactorAnalysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
In confirmatory factor analysis (CFA), structural constraints typically
ensure that the model is identified up to all possible reflections, i.e.,
column sign changes of the matrix of loadings. Such reflection invariance
is problematic for Bayesian CFA when the reflection modes are not well
separated in the posterior distribution. Imposing rotational constraints
-- fixing some loadings to be zero or positive in order to pick a factor
solution that corresponds to one reflection mode -- may not provide a
satisfactory solution for Bayesian CFA. The function 'relabel' uses the
relabeling algorithm of Erosheva and Curtis to correct for sign invariance
in MCMC draws from CFA models. The MCMC draws should come from Bayesian
CFA models that are fit without rotational constraints.

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
