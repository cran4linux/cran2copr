%global packname  msltrend
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          2%{?dist}
Summary:          Improved Techniques to Estimate Trend, Velocity and Accelerationfrom Sea Level Records

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.2
Requires:         R-core >= 3.2.2
BuildArch:        noarch
BuildRequires:    R-CRAN-forecast >= 6.2
BuildRequires:    R-CRAN-changepoint >= 2.1.1
BuildRequires:    R-CRAN-plyr >= 1.8.3
BuildRequires:    R-CRAN-zoo >= 1.7.12
BuildRequires:    R-CRAN-Rssa >= 0.13
BuildRequires:    R-CRAN-tseries >= 0.10.34
Requires:         R-CRAN-forecast >= 6.2
Requires:         R-CRAN-changepoint >= 2.1.1
Requires:         R-CRAN-plyr >= 1.8.3
Requires:         R-CRAN-zoo >= 1.7.12
Requires:         R-CRAN-Rssa >= 0.13
Requires:         R-CRAN-tseries >= 0.10.34

%description
Analysis of annual average ocean water level time series from long
(minimum length 80 years) individual records, providing improved estimates
of trend (mean sea level) and associated real-time velocities and
accelerations. Improved trend estimates are based on Singular Spectrum
Analysis methods. Various gap-filling options are included to accommodate
incomplete time series records. The package also contains a forecasting
module to consider the implication of user defined quantum of sea level
rise between the end of the available historical record and the year 2100.
A wide range of screen and pdf plotting options are available in the
package.

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
