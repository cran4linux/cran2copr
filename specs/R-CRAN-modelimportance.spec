%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  modelimportance
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Measuring Contributions of Component Models to Ensemble Forecast Accuracy

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-methods >= 4.4.3
BuildRequires:    R-stats >= 4.4.3
BuildRequires:    R-CRAN-checkmate >= 2.3.3
BuildRequires:    R-CRAN-future >= 1.49.0
BuildRequires:    R-CRAN-rlang >= 1.1.6
BuildRequires:    R-CRAN-dplyr >= 1.1.4
BuildRequires:    R-CRAN-purrr >= 1.0.4
BuildRequires:    R-CRAN-hubUtils >= 0.4.0
BuildRequires:    R-CRAN-furrr >= 0.3.1
BuildRequires:    R-CRAN-hubEvals >= 0.3.0
BuildRequires:    R-CRAN-hubEnsembles >= 0.1.9
Requires:         R-methods >= 4.4.3
Requires:         R-stats >= 4.4.3
Requires:         R-CRAN-checkmate >= 2.3.3
Requires:         R-CRAN-future >= 1.49.0
Requires:         R-CRAN-rlang >= 1.1.6
Requires:         R-CRAN-dplyr >= 1.1.4
Requires:         R-CRAN-purrr >= 1.0.4
Requires:         R-CRAN-hubUtils >= 0.4.0
Requires:         R-CRAN-furrr >= 0.3.1
Requires:         R-CRAN-hubEvals >= 0.3.0
Requires:         R-CRAN-hubEnsembles >= 0.1.9

%description
Provides metrics for quantifying the contribution of individual component
models to the predictive accuracy of ensemble forecasts. The package
implements the Leave-One-Model-Out (LOMO) and
Leave-All-Subset-of-One-Model-Out (LASOMO) model importance metrics,
enabling users to assess the relative importance of component models and
better understand the performance of ensemble forecasting systems. Methods
are described in Kim et al. (2026) <doi:10.1016/j.ijforecast.2025.12.006>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
[ -d %{packname}/src ] && find %{packname}/src/Make* -type f -exec \
  sed -i 's@-g0@@g' {} \; || true
# don't allow local prefix in executable scripts
find -type f -executable -exec sed -Ei 's@#!( )*/usr/local/bin@#!/usr/bin@g' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
# remove buildroot from installed files
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
