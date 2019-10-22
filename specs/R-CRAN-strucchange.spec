%global packname  strucchange
%global packver   1.5-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.2
Release:          1%{?dist}
Summary:          Testing, Monitoring, and Dating Structural Changes

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-sandwich 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 

%description
Testing, monitoring and dating structural changes in (linear) regression
models. strucchange features tests/methods from the generalized
fluctuation test framework as well as from the F test (Chow test)
framework. This includes methods to fit, plot and test fluctuation
processes (e.g., CUSUM, MOSUM, recursive/moving estimates) and F
statistics, respectively. It is possible to monitor incoming data online
using fluctuation processes. Finally, the breakpoints in regression models
with structural changes can be estimated together with confidence
intervals. Emphasis is always given to methods for visualizing the data.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
