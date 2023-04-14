%global __brp_check_rpaths %{nil}
%global packname  DBEST
%global packver   1.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.8
Release:          3%{?dist}%{?buildtag}
Summary:          Detecting Breakpoints and Estimating Segments in Trend

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-zoo 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-zoo 

%description
A program for analyzing vegetation time series, with two algorithms: 1)
change detection algorithm that detects trend changes, determines their
type (abrupt or non-abrupt), and estimates their timing, magnitude,
number, and direction; 2) generalization algorithm that simplifies the
temporal trend into main features. The user can set the number of major
breakpoints or magnitude of greatest changes of interest for detection,
and can control the generalization process by setting an additional
parameter of generalization-percentage.

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
