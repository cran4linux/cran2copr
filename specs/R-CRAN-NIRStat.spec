%global packname  NIRStat
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Novel Statistical Methods for Studying Near-InfraredSpectroscopy (NIRS) Time Series Data

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-mgcv 
BuildRequires:    R-CRAN-gridExtra 
Requires:         R-CRAN-ggplot2 
Requires:         R-mgcv 
Requires:         R-CRAN-gridExtra 

%description
Provides transfusion-related differential tests on Near-infrared
spectroscopy (NIRS) time series with detection limit, which contains two
testing statistics: Mean Area Under the Curve (MAUC) and slope statistic.
This package applied a penalized spline method within imputation setting.
Testing is conducted by a nested permutation approach within imputation.
Refer to Guo et al (2018) <doi:10.1177/0962280218786302> for further
details.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
