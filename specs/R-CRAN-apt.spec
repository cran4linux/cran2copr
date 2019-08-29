%global packname  apt
%global packver   2.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.5
Release:          1%{?dist}
Summary:          Asymmetric Price Transmission

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-erer 
BuildRequires:    R-CRAN-gWidgets 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-CRAN-urca 
BuildRequires:    R-CRAN-copula 
Requires:         R-CRAN-erer 
Requires:         R-CRAN-gWidgets 
Requires:         R-CRAN-car 
Requires:         R-CRAN-urca 
Requires:         R-CRAN-copula 

%description
Asymmetric price transmission between two time series is assessed. Several
functions are available for linear and nonlinear threshold cointegration,
and furthermore, symmetric and asymmetric error correction model. A
graphical user interface is also included for major functions included in
the package, so users can also use these functions in a more intuitive
way.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
