%global __brp_check_rpaths %{nil}
%global packname  fTrading
%global packver   3042.79
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3042.79
Release:          3%{?dist}%{?buildtag}
Summary:          Rmetrics - Trading and Rebalancing Financial Instruments

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.1
Requires:         R-core >= 2.15.1
BuildArch:        noarch
BuildRequires:    R-CRAN-timeDate 
BuildRequires:    R-CRAN-timeSeries 
BuildRequires:    R-CRAN-fBasics 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-CRAN-timeDate 
Requires:         R-CRAN-timeSeries 
Requires:         R-CRAN-fBasics 
Requires:         R-graphics 
Requires:         R-stats 

%description
A collection of functions for trading and rebalancing financial
instruments. It implements various technical indicators to analyse time
series such as moving averages or stochastic oscillators.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
