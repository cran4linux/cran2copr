%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  AutoAds
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Advertisement Metrics Calculation

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-rlang 

%description
Calculations of the most common metrics of automated advertisement and
plotting of them with trend and forecast. Calculations and description of
metrics is taken from different RTB platforms support documentation.
Plotting and forecasting is based on packages 'forecast', described in Rob
J Hyndman and George Athanasopoulos (2021) "Forecasting: Principles and
Practice" <https://otexts.com/fpp3/> and Rob J Hyndman et al
"Documentation for 'forecast'" (2003)
<https://pkg.robjhyndman.com/forecast/>, and 'ggplot2', described in
Hadley Wickham et al "Documentation for 'ggplot2'" (2015)
<https://ggplot2.tidyverse.org/>, and Hadley Wickham, Danielle Navarro,
and Thomas Lin Pedersen (2015) "ggplot2: Elegant Graphics for Data
Analysis" <https://ggplot2-book.org/>.

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
