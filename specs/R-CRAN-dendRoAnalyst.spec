%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  dendRoAnalyst
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Tool for Processing and Analyzing Dendrometer Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-tidyverse 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-CRAN-pspline 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-CRAN-signal 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-changepoint 
BuildRequires:    R-CRAN-WaveletComp 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-CRAN-tidyverse 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-minpack.lm 
Requires:         R-CRAN-pspline 
Requires:         R-CRAN-moments 
Requires:         R-CRAN-signal 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-changepoint 
Requires:         R-CRAN-WaveletComp 

%description
Tools for importing, cleaning, analyzing, and visualizing high-resolution
dendrometer data and for linking them with climate data. Dendrometer and
climate records can be imported with automatic date-time parsing
(read.dendrometer(), read.climate()) and checked for a regular temporal
resolution (reso_dm()). Preprocessing functions detect and correct
artificial jumps with a threshold-based or an automatic changepoint method
(jump.locator()), detect and fill gaps with spline, seasonal, or network
interpolation (dm.na.interpolation(), network.interpolation()), and
truncate or resample the series (dendro.truncate(), dendro.resample()).
Daily statistics (daily.data()), the stem-cycle approach (phase.sc()), and
the zero-growth approach (phase.zg()) separate radial growth from
reversible stem shrinkage and swelling. The function phase.zg() also
returns metrics of tree water deficit (TWD) phases, including the
event-based ABr index, and the daily drought indices of Peters et al.
(2025) <doi:10.1111/nph.70266>. Climate data can be summarized at daily
and sub-daily scales and attached to daily, phase-level, and point-level
outputs (dm_add_climate()). Event-based climate analyses, superposed epoch
analyses, and adverse-period analyses (dm_event_climate(),
dm_epoch_test(), clim.twd()) relate tree responses to climate conditions.
Seasonal growth can be fitted with Gompertz, logistic, Richards,
generalized additive model, LOESS, and spline functions, detrended, and
compared among methods (dm.growth.fit(), dm.detrend.fit(),
dm.growth.evaluate()). Running correlations with climate (mov.cor.dm())
and wavelet power and coherence analyses based on 'WaveletComp'
(dm_wavelet(), dm_wavelet_coherence()) are also provided. Most outputs
have dedicated plot methods, and an optional 'shiny' application
(dendroanalyst()) allows the complete workflow to be run without
programming. The zero-growth approach follows Zweifel et al. (2016)
<doi:10.1111/nph.13995>, and the first version of the package is described
in Aryal et al. (2020) <doi:10.1016/j.dendro.2020.125772>.

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
