%global packname  pltesim
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          2%{?dist}
Summary:          Simulate Probabilistic Long-Term Effects in Models with TemporalDependence

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-coreSim 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-coreSim 
Requires:         R-CRAN-ggplot2 

%description
Calculates and depicts probabilistic long-term effects in binary models
with temporal dependence variables. The package performs two tasks. First,
it calculates the change in the probability of the event occurring given a
change in a theoretical variable. Second, it calculates the rolling
difference in the future probability of the event for two scenarios: one
where the event occurred at a given time and one where the event does not
occur. The package is consistent with the recent movement to depict
meaningful and easy-to-interpret quantities of interest with the requisite
measures of uncertainty. It is the first to make it easy for researchers
to interpret short- and long-term effects of explanatory variables in
binary autoregressive models, which can have important implications for
the correct interpretation of these models.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
