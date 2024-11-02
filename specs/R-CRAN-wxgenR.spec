%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  wxgenR
%global packver   1.4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.2
Release:          1%{?dist}%{?buildtag}
Summary:          A Stochastic Weather Generator with Seasonality

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lubridate 
BuildRequires:    R-CRAN-msm 
BuildRequires:    R-CRAN-sm 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-lubridate 
Requires:         R-CRAN-msm 
Requires:         R-CRAN-sm 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-foreach 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-magrittr 

%description
A weather generator to simulate precipitation and temperature for regions
with seasonality. Users input training data containing precipitation,
temperature, and seasonality (up to 26 seasons). Including weather season
as a training variable allows users to explore the effects of potential
changes in season duration as well as average start- and end-time dates
due to phenomena like climate change. Data for training should be a single
time series but can originate from station data, basin averages, grid
cells, etc. Bearup, L., Gangopadhyay, S., & Mikkelson, K. (2021).
"Hydroclimate Analysis Lower Santa Cruz River Basin Study (Technical
Memorandum No ENV-2020-056)." Bureau of Reclamation. Gangopadhyay, S.,
Bearup, L. A., Verdin, A., Pruitt, T., Halper, E., & Shamir, E. (2019,
December 1). "A collaborative stochastic weather generator for climate
impacts assessment in the Lower Santa Cruz River Basin, Arizona." Fall
Meeting 2019, American Geophysical Union.
<https://ui.adsabs.harvard.edu/abs/2019AGUFMGC41G1267G>.

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
