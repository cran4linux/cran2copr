%global packname  foieGras
%global packver   0.7-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.5
Release:          1%{?dist}%{?buildtag}
Summary:          Fit Continuous-Time State-Space and Latent Variable Models for Quality Control of Argos Satellite (and Other) Telemetry Data and for Estimating Movement Behaviour

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-ggplot2 >= 3.0.0
BuildRequires:    R-CRAN-tibble >= 2.1.3
BuildRequires:    R-CRAN-TMB >= 1.7.15
BuildRequires:    R-CRAN-dplyr >= 1.0.0
BuildRequires:    R-CRAN-sf >= 0.9.4
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-trip 
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-furrr 
BuildRequires:    R-CRAN-CircStats 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-tmvtnorm 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-RcppEigen 
Requires:         R-CRAN-ggplot2 >= 3.0.0
Requires:         R-CRAN-tibble >= 2.1.3
Requires:         R-CRAN-TMB >= 1.7.15
Requires:         R-CRAN-dplyr >= 1.0.0
Requires:         R-CRAN-sf >= 0.9.4
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-trip 
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-future 
Requires:         R-CRAN-furrr 
Requires:         R-CRAN-CircStats 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-tmvtnorm 
Requires:         R-parallel 
Requires:         R-CRAN-lifecycle 

%description
Fits continuous-time random walk and correlated random walk state-space
models for quality control animal tracking data ('Argos', processed
light-level 'geolocation', 'GPS'). Template Model Builder ('TMB') is used
for fast estimation. The 'Argos' data can be: (older) least squares-based
locations; (newer) Kalman filter-based locations with error ellipse
information; or a mixture of both. The models estimate two sets of
location states corresponding to: 1) each observation, which are (usually)
irregularly timed; and 2) user-specified time intervals (regular or
irregular). Latent variable models are provided to estimate move
persistence along tracks as an index of behaviour. Track simulation
functions are provided. 'Jonsen I', 'McMahon CR', 'Patterson TA',
'Auger-Méthé M', 'Harcourt R', 'Hindell MA', 'Bestley S' (2019) Movement
responses to environment: fast inference of variation among southern
elephant seals with a mixed effects model. Ecology 100:e02566
<doi:10.1002/ecy.2566>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
