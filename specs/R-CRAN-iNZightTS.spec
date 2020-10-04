%global packname  iNZightTS
%global packver   1.5.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.2
Release:          3%{?dist}%{?buildtag}
Summary:          Time Series for 'iNZight'

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-grid 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-egg 
BuildRequires:    R-CRAN-rlang 
Requires:         R-methods 
Requires:         R-grid 
Requires:         R-CRAN-gridExtra 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-egg 
Requires:         R-CRAN-rlang 

%description
Provides a collection of functions for working with time series data,
including functions for drawing, decomposing, and forecasting. Includes
capabilities to compare multiple series and fit both additive and
multiplicative models. Used by 'iNZight', a graphical user interface
providing easy exploration and visualisation of data for students of
statistics, available in both desktop and online versions. Holt (1957)
<doi:10.1016/j.ijforecast.2003.09.015>, Winters (1960)
<doi:10.1287/mnsc.6.3.324>, Cleveland, Cleveland, & Terpenning (1990)
"STL: A Seasonal-Trend Decomposition Procedure Based on Loess".

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
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
