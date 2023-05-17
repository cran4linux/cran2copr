%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  navigation
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Analyze the Impact of Sensor Error Modelling on Navigation Performance

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildRequires:    R-CRAN-Rcpp >= 0.8.0
BuildRequires:    R-CRAN-RcppArmadillo >= 0.2.0
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-simts 
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-CRAN-rbenchmark 
BuildRequires:    R-CRAN-leaflet 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-pbmcapply 
Requires:         R-CRAN-Rcpp >= 0.8.0
Requires:         R-CRAN-RcppArmadillo >= 0.2.0
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-simts 
Requires:         R-CRAN-expm 
Requires:         R-CRAN-rbenchmark 
Requires:         R-CRAN-leaflet 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-pbmcapply 

%description
Implements the framework presented in Cucci, D. A., Voirol, L., Khaghani,
M. and Guerrier, S. (2023) <doi:10.1109/TIM.2023.3267360> which allows to
analyze the impact of sensor error modeling on the performance of
integrated navigation (sensor fusion) based on inertial measurement unit
(IMU), Global Positioning System (GPS), and barometer data. The framework
relies on Monte Carlo simulations in which a Vanilla Extended Kalman
filter is coupled with realistic and user-configurable noise generation
mechanisms to recover a reference trajectory from noisy measurements. The
evaluation of several statistical metrics of the solution, aggregated over
hundreds of simulated realizations, provides reasonable estimates of the
expected performances of the system in real-world conditions.

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
