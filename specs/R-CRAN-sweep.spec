%global __brp_check_rpaths %{nil}
%global packname  sweep
%global packver   0.2.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.3
Release:          1%{?dist}%{?buildtag}
Summary:          Tidy Tools for Forecasting

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-forecast >= 8.0
BuildRequires:    R-CRAN-timetk >= 2.1.0
BuildRequires:    R-CRAN-lubridate >= 1.6.0
BuildRequires:    R-CRAN-tibble >= 1.2
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-tidyr >= 1.0.0
BuildRequires:    R-CRAN-broom >= 0.5.6
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-forecast >= 8.0
Requires:         R-CRAN-timetk >= 2.1.0
Requires:         R-CRAN-lubridate >= 1.6.0
Requires:         R-CRAN-tibble >= 1.2
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-tidyr >= 1.0.0
Requires:         R-CRAN-broom >= 0.5.6
Requires:         R-CRAN-rlang 

%description
Tidies up the forecasting modeling and prediction work flow, extends the
'broom' package with 'sw_tidy', 'sw_glance', 'sw_augment', and
'sw_tidy_decomp' functions for various forecasting models, and enables
converting 'forecast' objects to "tidy" data frames with 'sw_sweep'.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
