%global packname  NMAoutlier
%global packver   0.1.13
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.13
Release:          2%{?dist}
Summary:          Detecting Outliers in Network Meta-Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-MASS >= 7.3.47
BuildRequires:    R-stats >= 3.4.3
BuildRequires:    R-parallel >= 3.4.1
BuildRequires:    R-CRAN-ggplot2 >= 3.0.0
BuildRequires:    R-CRAN-gridExtra >= 2.3
BuildRequires:    R-CRAN-reshape2 >= 1.4.3
BuildRequires:    R-CRAN-netmeta >= 0.9.7
Requires:         R-MASS >= 7.3.47
Requires:         R-stats >= 3.4.3
Requires:         R-parallel >= 3.4.1
Requires:         R-CRAN-ggplot2 >= 3.0.0
Requires:         R-CRAN-gridExtra >= 2.3
Requires:         R-CRAN-reshape2 >= 1.4.3
Requires:         R-CRAN-netmeta >= 0.9.7

%description
A set of functions providing the forward search algorithm for detecting
outlying studies (i.e., studies with extreme findings) in network
meta-analysis: - provides the length of the initial subset for forward
search algorithm; - iterations of forward search algorithm; - basic set of
studies in each step of forward search algorithm; - summary estimates and
their confidence intervals in each step of forward search algorithm; -
outlying case diagnostics measures; - ranking measures; - heterogeneity
and inconsistency measures; - forward plot for summary estimates and their
confidence intervals; - forward plots for monitored measures: outlying
case diagnostics measures, ranking measures, heterogeneity, and
inconsistency measures.

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
