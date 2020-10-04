%global packname  dsa
%global packver   0.74.18
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.74.18
Release:          3%{?dist}%{?buildtag}
Summary:          Seasonal Adjustment of Daily Time Series

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-R2HTML 
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-grid 
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-tsoutliers 
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-rJava 
BuildRequires:    R-CRAN-timeDate 
BuildRequires:    R-CRAN-dygraphs 
BuildRequires:    R-CRAN-extrafont 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-stats 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-R2HTML 
Requires:         R-CRAN-xtable 
Requires:         R-grid 
Requires:         R-tools 
Requires:         R-CRAN-tsoutliers 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-rJava 
Requires:         R-CRAN-timeDate 
Requires:         R-CRAN-dygraphs 
Requires:         R-CRAN-extrafont 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-reshape2 
Requires:         R-stats 

%description
Seasonal- and calendar adjustment of time series with daily frequency
using the DSA approach developed by Ollech, Daniel (2018): Seasonal
adjustment of daily time series. Bundesbank Discussion Paper 41/2018.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
