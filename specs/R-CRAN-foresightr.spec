%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  foresightr
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Forecasts Chosen by What Would Have Worked

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildRequires:    R-CRAN-ggplot2 >= 3.5.0
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 >= 3.5.0
Requires:         R-stats 
Requires:         R-CRAN-tibble 
Requires:         R-utils 

%description
Time series forecasting that replays the past before trusting a model: a
rolling-origin backtest, Tashman (2000)
<doi:10.1016/S0169-2070(00)00065-0>, refits every candidate at each
origin, the choice is made by out-of-sample error, and prediction
intervals are quantiles of the errors actually observed, for each horizon
and for totals of the next periods. Models include seasonal ARIMA by exact
maximum likelihood with automatic orders, Hyndman and Khandakar (2008)
<doi:10.18637/jss.v027.i03>; exponential smoothing in state space form,
Hyndman, Koehler, Snyder and Grose (2002)
<doi:10.1016/S0169-2070(01)00110-8>; the Theta method, Assimakopoulos and
Nikolopoulos (2000) <doi:10.1016/S0169-2070(00)00066-2>; a trend with
changepoints and events in the manner of Taylor and Letham (2018)
<doi:10.1080/00031305.2017.1380080>; TBATS, De Livera, Hyndman and Snyder
(2011) <doi:10.1198/jasa.2011.tm09771>; seasonal-trend decompositions by
LOESS for one or several seasonal periods, Bandara, Hyndman and Bergmeir
(2021) <doi:10.48550/arXiv.2107.13462>; the method of Croston (1972)
<doi:10.1057/jors.1972.50> for intermittent demand; and ensembles. The
computations are done by the 'Rust' crate 'foresight', bundled with the
package.

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
