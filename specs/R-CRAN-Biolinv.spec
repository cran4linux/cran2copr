%global packname  Biolinv
%global packver   0.1-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          3%{?dist}
Summary:          Modelling and Forecasting Biological Invasions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.4
Requires:         R-core >= 3.2.4
BuildArch:        noarch
BuildRequires:    R-CRAN-fields >= 8.3.6
BuildRequires:    R-grDevices >= 3.3.2
BuildRequires:    R-stats >= 3.3.2
BuildRequires:    R-CRAN-raster >= 2.5.2
BuildRequires:    R-CRAN-spatstat >= 1.48.0
BuildRequires:    R-CRAN-sp >= 1.2.4
BuildRequires:    R-CRAN-classInt >= 0.1.23
Requires:         R-CRAN-fields >= 8.3.6
Requires:         R-grDevices >= 3.3.2
Requires:         R-stats >= 3.3.2
Requires:         R-CRAN-raster >= 2.5.2
Requires:         R-CRAN-spatstat >= 1.48.0
Requires:         R-CRAN-sp >= 1.2.4
Requires:         R-CRAN-classInt >= 0.1.23

%description
Analysing and forecasting biological invasions time series with a
stochastic, non-mechanistic approach that gives proper weight to the
anthropic component, accounts for habitat suitability and provides
measures of precision for its estimates.

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
