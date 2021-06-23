%global __brp_check_rpaths %{nil}
%global packname  GeomComb
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          2%{?dist}%{?buildtag}
Summary:          (Geometric) Forecast Combination Methods

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-forecast >= 7.3
BuildRequires:    R-CRAN-ggplot2 >= 2.1.0
BuildRequires:    R-CRAN-psych >= 1.6.9
BuildRequires:    R-Matrix >= 1.2.6
BuildRequires:    R-CRAN-ForecastCombinations >= 1.1
BuildRequires:    R-CRAN-mtsdi >= 0.3.3
Requires:         R-CRAN-forecast >= 7.3
Requires:         R-CRAN-ggplot2 >= 2.1.0
Requires:         R-CRAN-psych >= 1.6.9
Requires:         R-Matrix >= 1.2.6
Requires:         R-CRAN-ForecastCombinations >= 1.1
Requires:         R-CRAN-mtsdi >= 0.3.3

%description
Provides eigenvector-based (geometric) forecast combination methods; also
includes simple approaches (simple average, median, trimmed and winsorized
mean, inverse rank method) and regression-based combination. Tools for
data pre-processing are available in order to deal with common problems in
forecast combination (missingness, collinearity).

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

%files
%{rlibdir}/%{packname}
