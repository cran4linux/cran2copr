%global packname  IDF
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}
Summary:          Estimation and Plotting of IDF Curves

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats4 
BuildRequires:    R-CRAN-evd 
BuildRequires:    R-CRAN-ismev 
Requires:         R-stats4 
Requires:         R-CRAN-evd 
Requires:         R-CRAN-ismev 

%description
Intensity-duration-frequency (IDF) curves are a widely used analysis-tool
in hydrology to assess extreme values of precipitation [e.g. Mailhot et
al., 2007, <doi:10.1016/j.jhydrol.2007.09.019>]. The package 'IDF'
provides a function to read precipitation data from German weather service
(DWD) 'webwerdis'
<http://www.dwd.de/EN/ourservices/webwerdis/webwerdis.html> files and
Berlin station data from 'Stadtmessnetz'
<http://www.geo.fu-berlin.de/en/met/service/stadtmessnetz/index.html>
files, and additionally IDF parameters can be estimated also from a given
data.frame containing a precipitation time series. The data is aggregated
to given levels yearly intensity maxima are calculated either for the
whole year or given months. From these intensity maxima IDF parameters are
estimated on the basis of a duration-dependent generalised extreme value
distribution [Koutsoyannis et al., 1998,
<doi:10.1016/S0022-1694(98)00097-3>]. IDF curves based on these estimated
parameters can be plotted.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
