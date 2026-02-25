%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BINCOR
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Estimate the Correlation Between Two Irregular Time Series

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-pracma 
Requires:         R-CRAN-pracma 

%description
Estimate the correlation between two irregular time series that are not
necessarily sampled on identical time points. This program is also
applicable to the situation of two evenly spaced time series that are not
on the same time grid. 'BINCOR' is based on a novel estimation approach
proposed by Mudelsee (2010, 2014) to estimate the correlation between two
climate time series with different timescales. The idea is that
autocorrelation (AR1 process) allows to correlate values obtained on
different time points. 'BINCOR' contains four functions: bin_cor() (the
main function to build the binned time series), plot_ts() (to plot and
compare the irregular and binned time series, cor_ts() (to estimate the
correlation between the binned time series) and ccf_ts() (to estimate the
cross-correlation between the binned time series). A description of the
method and package is provided in Polanco-Martínez et al. (2019),
<doi:10.32614/RJ-2019-035>.

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
