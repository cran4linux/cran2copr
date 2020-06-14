%global packname  EMAtools
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          2%{?dist}
Summary:          Data Management Tools for Real-Time Monitoring/EcologicalMomentary Assessment Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-sjstats >= 0.10.2
BuildRequires:    R-CRAN-DataCombine 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-lmerTest 
Requires:         R-CRAN-sjstats >= 0.10.2
Requires:         R-CRAN-DataCombine 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-lmerTest 

%description
Do data management functions common in real-time monitoring (also called:
ecological momentary assessment, experience sampling, micro-longitudinal)
data, including creating power curves for multilevel data, centering on
participant means and merging event-level data into momentary data sets
where you need the events to correspond to the nearest data point in the
momentary data. This is VERY early release software, and more features
will be added over time.

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
