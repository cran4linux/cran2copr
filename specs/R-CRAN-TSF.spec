%global __brp_check_rpaths %{nil}
%global packname  TSF
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Two Stage Forecasting (TSF) for Long Memory Time Series inPresence of Structural Break

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-fracdiff 
BuildRequires:    R-CRAN-forecast 
Requires:         R-stats 
Requires:         R-CRAN-fracdiff 
Requires:         R-CRAN-forecast 

%description
Forecasting of long memory time series in presence of structural break by
using TSF algorithm by Papailias and Dias (2015)
<doi:10.1016/j.ijforecast.2015.01.006>.

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
