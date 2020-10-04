%global packname  ForecastComb
%global packver   1.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.1
Release:          2%{?dist}%{?buildtag}
Summary:          Forecast Combination Methods

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.2
Requires:         R-core >= 3.0.2
BuildArch:        noarch
BuildRequires:    R-CRAN-forecast >= 7.3
BuildRequires:    R-CRAN-quantreg >= 5.29
BuildRequires:    R-CRAN-ggplot2 >= 2.1.0
BuildRequires:    R-CRAN-psych >= 1.6.9
BuildRequires:    R-CRAN-quadprog >= 1.5.5
BuildRequires:    R-Matrix >= 1.2.6
BuildRequires:    R-CRAN-mtsdi >= 0.3.3
Requires:         R-CRAN-forecast >= 7.3
Requires:         R-CRAN-quantreg >= 5.29
Requires:         R-CRAN-ggplot2 >= 2.1.0
Requires:         R-CRAN-psych >= 1.6.9
Requires:         R-CRAN-quadprog >= 1.5.5
Requires:         R-Matrix >= 1.2.6
Requires:         R-CRAN-mtsdi >= 0.3.3

%description
Provides geometric- and regression-based forecast combination methods
under a unified user interface for the packages 'ForecastCombinations' and
'GeomComb'. Additionally, updated tools and convenience functions for data
pre-processing are available in order to deal with common problems in
forecast combination (missingness, collinearity). For method details see
Hsiao C, Wan SK (2014). <doi:10.1016/j.jeconom.2013.11.003>, Hansen BE
(2007). <doi:10.1111/j.1468-0262.2007.00785.x>, Elliott G, Gargano A,
Timmermann A (2013). <doi:10.1016/j.jeconom.2013.04.017>, and Clemen RT
(1989). <doi:10.1016/0169-2070(89)90012-5>.

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
