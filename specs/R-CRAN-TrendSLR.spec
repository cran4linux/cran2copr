%global __brp_check_rpaths %{nil}
%global packname  TrendSLR
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Estimating Trend, Velocity and Acceleration from Sea LevelRecords

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.2
Requires:         R-core >= 3.2.2
BuildArch:        noarch
BuildRequires:    R-CRAN-forecast >= 6.2
BuildRequires:    R-CRAN-changepoint >= 2.1.1
BuildRequires:    R-CRAN-plyr >= 1.8.3
BuildRequires:    R-CRAN-imputeTS >= 1.8
BuildRequires:    R-CRAN-zoo >= 1.7.12
BuildRequires:    R-CRAN-Rssa >= 0.13.1
BuildRequires:    R-CRAN-tseries >= 0.10.34
Requires:         R-CRAN-forecast >= 6.2
Requires:         R-CRAN-changepoint >= 2.1.1
Requires:         R-CRAN-plyr >= 1.8.3
Requires:         R-CRAN-imputeTS >= 1.8
Requires:         R-CRAN-zoo >= 1.7.12
Requires:         R-CRAN-Rssa >= 0.13.1
Requires:         R-CRAN-tseries >= 0.10.34

%description
Analysis of annual average ocean water level time series, providing
improved estimates of trend (mean sea level) and associated real-time
velocities and accelerations. Improved trend estimates are based on
singular spectrum analysis methods. Various gap-filling options are
included to accommodate incomplete time series records. The package also
includes a range of diagnostic tools to inspect the components comprising
the original time series which enables expert interpretation and selection
of likely trend components. A wide range of screen and plot to file
options are available in the package.

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
