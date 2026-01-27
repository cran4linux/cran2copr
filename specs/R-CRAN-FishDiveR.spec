%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FishDiveR
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Classify Aquatic Animal Behaviours from Vertical Movement Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-cowplot 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-FactoMineR 
BuildRequires:    R-CRAN-geometry 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-CRAN-suncalc 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-WaveletComp 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-cowplot 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-FactoMineR 
Requires:         R-CRAN-geometry 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-moments 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-Rfast 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-scales 
Requires:         R-CRAN-suncalc 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-WaveletComp 

%description
Quantitatively analyse depth time-series data from pop-up satellite
archival tags (PSATs) through the application of continuous wavelet
transformation (CWT) combined with Principal Component Analysis (PCA), and
k-means clustering. Import, crop, and plot depth time-depth records
(TDRs). Using CWT to detect important signals within the non-stationary
data, we create daily wavelet statistics to summarise vertical movements
on different wavelet periods and combine with daily and diel depth
statistics. Classify depth time-series with unsupervised k-means
clustering into 24-hour periods of vertical movement behaviour with
distinct patterns of vertical movement. Plot example days from each
behaviour cluster, and plot the TDR coloured by cluster. Based on
principals of combining CWT with k-means first developed by Sakamoto
(2009) <doi:10.1371/journal.pone.0005379> and redeveloped by Beale (2026)
<doi:10.21203/rs.3.rs-6907076/v1>.

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
