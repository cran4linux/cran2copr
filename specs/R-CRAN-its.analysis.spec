%global packname  its.analysis
%global packver   1.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.1
Release:          3%{?dist}
Summary:          Running Interrupted Time Series Analysis

License:          MIT + file LICENCE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-car 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-boot 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-car 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-forecast 
Requires:         R-boot 
Requires:         R-CRAN-ggplot2 

%description
Two functions for running and then post-estimating an Interrupted Time
Series Analysis model. This is a solution for running time series analyses
on temporally short data. See English (2019) 'The its.analysis R package -
Modelling short time series data'
<https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3398189> for an
overview of the method.

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
%license %{rlibdir}/%{packname}/LICENCE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
