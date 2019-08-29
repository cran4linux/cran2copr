%global packname  ForeCA
%global packver   0.2.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.4
Release:          1%{?dist}
Summary:          Forecastable Component Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ifultools >= 2.0.0
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-sapa 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-utils 
Requires:         R-CRAN-ifultools >= 2.0.0
Requires:         R-MASS 
Requires:         R-CRAN-sapa 
Requires:         R-graphics 
Requires:         R-CRAN-reshape2 
Requires:         R-utils 

%description
Implementation of Forecastable Component Analysis ('ForeCA'), including
main algorithms and auxiliary function (summary, plotting, etc.) to apply
'ForeCA' to multivariate time series data. 'ForeCA' is a novel dimension
reduction (DR) technique for temporally dependent signals. Contrary to
other popular DR methods, such as 'PCA' or 'ICA', 'ForeCA' takes time
dependency explicitly into account and searches for the most
''forecastable'' signal. The measure of forecastability is based on the
Shannon entropy of the spectral density of the transformed signal.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
