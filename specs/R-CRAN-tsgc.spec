%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tsgc
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Time Series Methods Based on Growth Curves

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.5.0
BuildRequires:    R-CRAN-KFAS 
BuildRequires:    R-CRAN-xts 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-kableExtra 
Requires:         R-CRAN-ggplot2 >= 3.5.0
Requires:         R-CRAN-KFAS 
Requires:         R-CRAN-xts 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-tidyr 
Requires:         R-methods 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-kableExtra 

%description
Provides tools for modelling and forecasting epidemic trajectories using a
dynamic Gompertz model within a state space framework, with the Kalman
filter for robust estimation of non-linear growth. Includes a
reinitialization feature to adapt to new waves, and a leading-indicator
extension that uses a related series moving ahead of the variable of
interest (e.g. cases ahead of hospitalisations) to improve short-horizon
forecasts, with model and lag selection via rolling-origin
cross-validation. Applicable to data at daily, monthly, quarterly, or
annual frequency, and to non-epidemic trajectories with similar dynamics,
such as innovation diffusion and product adoption. Includes functions for
data preprocessing, model fitting, forecast visualization, and accuracy
evaluation using standard error measures. Methods are described in Harvey
and Kattuman (2020) <doi:10.1162/99608f92.828f40de>, Harvey and Kattuman
(2021) <doi:10.1098/rsif.2021.0179>, and Ashby, Harvey, Kattuman, Tang,
and Thamotheram (2024)
<https://www.jbs.cam.ac.uk/wp-content/uploads/2024/03/cchle-tsgc-paper-2024.pdf>.

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
