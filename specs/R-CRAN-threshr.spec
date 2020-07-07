%global packname  threshr
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          3%{?dist}
Summary:          Threshold Selection and Uncertainty for Extreme Value Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rust >= 1.2.2
BuildRequires:    R-CRAN-revdbayes >= 1.2.0
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-CRAN-rust >= 1.2.2
Requires:         R-CRAN-revdbayes >= 1.2.0
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-stats 

%description
Provides functions for the selection of thresholds for use in extreme
value models, based mainly on the methodology in Northrop, Attalides and
Jonathan (2017) <doi:10.1111/rssc.12159>. It also performs predictive
inferences about future extreme values, based either on a single threshold
or on a weighted average of inferences from multiple thresholds, using the
'revdbayes' package <https://cran.r-project.org/package=revdbayes>. At the
moment only the case where the data can be treated as independent
identically distributed observations is considered.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
