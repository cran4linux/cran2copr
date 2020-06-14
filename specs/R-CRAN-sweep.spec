%global packname  sweep
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          2%{?dist}
Summary:          Tidy Tools for Forecasting

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-forecast >= 8.0
BuildRequires:    R-CRAN-lubridate >= 1.6.0
BuildRequires:    R-CRAN-tibble >= 1.2
BuildRequires:    R-CRAN-tidyr >= 1.0.0
BuildRequires:    R-CRAN-dplyr >= 0.7.0
BuildRequires:    R-CRAN-broom >= 0.4.2
BuildRequires:    R-CRAN-lazyeval >= 0.2.0
BuildRequires:    R-CRAN-timetk >= 0.1.0
Requires:         R-CRAN-forecast >= 8.0
Requires:         R-CRAN-lubridate >= 1.6.0
Requires:         R-CRAN-tibble >= 1.2
Requires:         R-CRAN-tidyr >= 1.0.0
Requires:         R-CRAN-dplyr >= 0.7.0
Requires:         R-CRAN-broom >= 0.4.2
Requires:         R-CRAN-lazyeval >= 0.2.0
Requires:         R-CRAN-timetk >= 0.1.0

%description
Tidies up the forecasting modeling and prediction work flow, extends the
'broom' package with 'sw_tidy', 'sw_glance', 'sw_augment', and
'sw_tidy_decomp' functions for various forecasting models, and enables
converting 'forecast' objects to "tidy" data frames with 'sw_sweep'.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
