%global packname  raters
%global packver   2.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.1
Release:          3%{?dist}
Summary:          A Modification of Fleiss' Kappa in Case of Nominal and OrdinalVariables

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch

%description
The kappa statistic implemented by Fleiss is a very popular index for
assessing the reliability of agreement among multiple observers. It is
used both in the psychological and in the psychiatric field. Other fields
of application are typically medicine, biology and engineering.
Unfortunately,the kappa statistic may behave inconsistently in case of
strong agreement between raters, since this index assumes lower values
than it would have been expected. We propose a modification kappa
implemented by Fleiss in case of nominal and ordinal variables. Monte
Carlo simulations are used both to testing statistical hypotheses and to
calculating percentile bootstrap confidence intervals based on proposed
statistic in case of nominal and ordinal data.

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
