%global packname  EvalEst
%global packver   2015.4-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2015.4.2
Release:          3%{?dist}
Summary:          Dynamic Systems Estimation - Extensions

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.5.0
Requires:         R-core >= 2.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tframe >= 2007.5.3
BuildRequires:    R-CRAN-dse >= 2007.10.1
BuildRequires:    R-CRAN-tfplot 
BuildRequires:    R-CRAN-setRNG 
Requires:         R-CRAN-tframe >= 2007.5.3
Requires:         R-CRAN-dse >= 2007.10.1
Requires:         R-CRAN-tfplot 
Requires:         R-CRAN-setRNG 

%description
Provides functions for evaluating (time series) model estimation methods.
These facilitate Monte Carlo experiments of repeated simulations and
estimations. Also provides methods for looking at the distribution of the
results from these experiments, including model roots (which are an
equivalence class invariant).

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
