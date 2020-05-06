%global packname  DescriptiveStats.OBeu
%global packver   1.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.2
Release:          1%{?dist}
Summary:          Descriptive Statistics 'OpenBudgets.eu'

License:          GPL-2 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-RCurl 
BuildRequires:    R-CRAN-reshape 
BuildRequires:    R-stats 
Requires:         R-CRAN-dplyr 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-RCurl 
Requires:         R-CRAN-reshape 
Requires:         R-stats 

%description
Estimate and return the needed parameters for visualizations designed for
'OpenBudgets.eu' <http://openbudgets.eu/> datasets. Calculate descriptive
statistical measures in budget data of municipalities across Europe,
according to the 'OpenBudgets.eu' data model. There are functions for
measuring central tendency and dispersion of amount variables along with
their distributions and correlations and the frequencies of categorical
variables for a given dataset. Also, can be used generally to other
datasets, to extract visualization parameters, convert them to 'JSON'
format and use them as input in a different graphical interface.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
