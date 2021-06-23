%global __brp_check_rpaths %{nil}
%global packname  FlowScreen
%global packver   1.2.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.6
Release:          3%{?dist}%{?buildtag}
Summary:          Daily Streamflow Trend and Change Point Screening

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-zyp 
BuildRequires:    R-CRAN-changepoint 
BuildRequires:    R-CRAN-evir 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-zyp 
Requires:         R-CRAN-changepoint 
Requires:         R-CRAN-evir 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-utils 

%description
Screens daily streamflow time series for temporal trends and
change-points. This package has been primarily developed for assessing the
quality of daily streamflow time series. It also contains tools for
plotting and calculating many different streamflow metrics. The package
can be used to produce summary screening plots showing change-points and
significant temporal trends for high flow, low flow, and/or baseflow
statistics, or it can be used to perform more detailed hydrological time
series analyses. The package was designed for screening daily streamflow
time series from Water Survey Canada and the United States Geological
Survey but will also work with streamflow time series from many other
agencies.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
