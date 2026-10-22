%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  EventStudy
%global packver   0.66.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.66.0
Release:          1%{?dist}%{?buildtag}
Summary:          Event Study Analysis

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-distributional 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-distributional 
Requires:         R-methods 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 

%description
Financial event study analysis. Implements the classical event study
methodology of MacKinlay (1997) <https://www.jstor.org/stable/2729691>
with multiple return models: market model, market adjusted, comparison
period mean adjusted, Fama and French three-factor (1993)
<doi:10.1016/0304-405X(93)90023-5> and five-factor (2015)
<doi:10.1016/j.jfineco.2014.10.010>, Carhart (1997) four-factor
<doi:10.1111/j.1540-6261.1997.tb03808.x>, generalized autoregressive
conditional heteroskedasticity (GARCH; Bollerslev, 1986)
<doi:10.1016/0304-4076(86)90063-1>, rolling window, and dynamic
conditional correlation GARCH (DCC-GARCH; Engle, 2002)
<doi:10.1198/073500102288618487>. Provides parametric and non-parametric
test statistics, including the standardized cross-sectional test of
Boehmer, Musumeci and Poulsen (1991) <doi:10.1016/0304-405X(91)90032-F>
and its cross-correlation adjustment by Kolari and Pynnonen (2010)
<doi:10.1093/rfs/hhq072>; buy-and-hold abnormal returns (Barber and Lyon,
1997) <doi:10.1016/S0304-405X(96)00890-2>; volume and volatility event
studies; cross-sectional regression; intraday event studies; panel
difference-in-differences event studies with the estimators of Callaway
and Sant'Anna (2021) <doi:10.1016/j.jeconom.2020.12.001>, de Chaisemartin
and D'Haultfoeuille (2020) <doi:10.1257/aer.20181169>, and Borusyak,
Jaravel and Spiess (2024) <doi:10.1093/restud/rdae007>; synthetic control
methods (Abadie, Diamond and Hainmueller, 2010)
<doi:10.1198/jasa.2009.ap08746>; wild bootstrap inference; multiple
testing corrections; power analysis via simulation; data download helpers;
automated reporting; and visualization tools. Results can be exported to
comma-separated values (CSV), 'Excel', or 'LaTeX'.

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
