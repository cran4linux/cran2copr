%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  disaggR
%global packver   1.0.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Two-Steps Benchmarks for Time Series Disaggregation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-CRAN-RColorBrewer >= 1.1.2
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-RColorBrewer >= 1.1.2
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 

%description
The twoStepsBenchmark() and threeRuleSmooth() functions allow you to
disaggregate a low-frequency time series with higher frequency time
series, using the French National Accounts methodology. The aggregated sum
of the resulting time series is strictly equal to the low-frequency time
series within the benchmarking window. Typically, the low-frequency time
series is an annual one, unknown for the last year, and the high frequency
one is either quarterly or monthly. See "Methodology of quarterly national
accounts", Insee Méthodes N°126, by Insee (2012, ISBN:978-2-11-068613-8,
<https://www.insee.fr/en/information/2579410>).

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
