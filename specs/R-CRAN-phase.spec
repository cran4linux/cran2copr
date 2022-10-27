%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  phase
%global packver   1.2.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.5
Release:          1%{?dist}%{?buildtag}
Summary:          Analyse Biological Time-Series Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-circular 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-signal 
BuildRequires:    R-CRAN-zeitgebr 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-behavr 
Requires:         R-CRAN-circular 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-signal 
Requires:         R-CRAN-zeitgebr 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-behavr 

%description
Compiles functions to trim, bin, visualise, and analyse activity/sleep
time-series data collected from the Drosophila Activity Monitor (DAM)
system (Trikinetics, USA). The following methods were used to compute
periodograms - Chi-square periodogram: Sokolove and Bushell (1978)
<doi:10.1016/0022-5193(78)90022-X>, Lomb-Scargle periodogram: Lomb (1976)
<doi:10.1007/BF00648343>, Scargle (1982) <doi:10.1086/160554> and Ruf
(1999) <doi:10.1076/brhm.30.2.178.1422>, and Autocorrelation: Eijzenbach
et al. (1986) <doi:10.1111/j.1440-1681.1986.tb00943.x>. Identification of
activity peaks is done after using a Savitzky-Golay filter (Savitzky and
Golay (1964) <doi:10.1021/ac60214a047>) to smooth raw activity data. Three
methods to estimate anticipation of activity are used based on the
following papers - Slope method: Fernandez et al. (2020)
<doi:10.1016/j.cub.2020.04.025>, Harrisingh method: Harrisingh et al.
(2007) <doi:10.1523/JNEUROSCI.3680-07.2007>, and Stoleru method: Stoleru
et al. (2004) <doi:10.1038/nature02926>. Rose plots and circular analysis
are based on methods from - Batschelet (1981) <ISBN:0120810506> and Zar
(2010) <ISBN:0321656865>.

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
