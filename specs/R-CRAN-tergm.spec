%global packname  tergm
%global packver   3.6.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.6.1
Release:          1%{?dist}
Summary:          Fit, Simulate and Diagnose Models for Network Evolution Based onExponential-Family Random Graph Models

License:          GPL-3 + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-MASS >= 7.3.51.4
BuildRequires:    R-CRAN-statnet.common >= 4.2.0
BuildRequires:    R-CRAN-ergm >= 3.10.1
BuildRequires:    R-nlme >= 3.1.139
BuildRequires:    R-CRAN-network >= 1.15
BuildRequires:    R-CRAN-robustbase >= 0.93.5
BuildRequires:    R-CRAN-coda >= 0.19.2
BuildRequires:    R-CRAN-networkDynamic >= 0.10.0
Requires:         R-MASS >= 7.3.51.4
Requires:         R-CRAN-statnet.common >= 4.2.0
Requires:         R-CRAN-ergm >= 3.10.1
Requires:         R-nlme >= 3.1.139
Requires:         R-CRAN-network >= 1.15
Requires:         R-CRAN-robustbase >= 0.93.5
Requires:         R-CRAN-coda >= 0.19.2
Requires:         R-CRAN-networkDynamic >= 0.10.0

%description
An integrated set of extensions to the 'ergm' package to analyze and
simulate network evolution based on exponential-family random graph models
(ERGM). 'tergm' is a part of the 'statnet' suite of packages for network
analysis.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
