%global packname  leafR
%global packver   0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3
Release:          3%{?dist}%{?buildtag}
Summary:          Calculates the Leaf Area Index (LAD) and Other Related Functions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-lidR 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-lazyeval 
Requires:         R-CRAN-lidR 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-raster 
Requires:         R-stats 
Requires:         R-CRAN-lazyeval 

%description
A set of functions for analyzing the structure of forests based on the
leaf area density (LAD) and leaf area index (LAI) measures calculated from
Airborne Laser Scanning (ALS), i.e., scanning lidar (Light Detection and
Ranging) data. The methodology is discussed and described in Almeida et
al. (2019) <doi:10.3390/rs11010092> and Stark et al. (2012)
<doi:10.1111/j.1461-0248.2012.01864.x>.

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
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
