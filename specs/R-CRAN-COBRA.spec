%global packname  COBRA
%global packver   0.99.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.99.4
Release:          1%{?dist}
Summary:          Nonlinear Aggregation of Predictors

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core

%description
This package performs prediction for regression-oriented problems,
aggregating in a nonlinear scheme any basic regression machines suggested
by the context and provided by the user. If the user has no valuable
knowledge on the data, four defaults machines wrappers are implemented so
as to cover a minimal spectrum of prediction methods. If necessary, the
computations may be parallelized. The method is described in Biau,
Fischer, Guedj and Malley (2013), "COBRA: A Nonlinear Aggregation
Strategy".

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
