%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  controlcharts
%global packver   0.0.19
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.19
Release:          1%{?dist}%{?buildtag}
Summary:          Interactive Plotting for Funnel Plots and Statistical Process Control Charts

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-htmlwidgets 
BuildRequires:    R-CRAN-htmltools 
BuildRequires:    R-CRAN-crosstalk 
BuildRequires:    R-CRAN-QuickJSR 
BuildRequires:    R-CRAN-jsutils 
Requires:         R-CRAN-htmlwidgets 
Requires:         R-CRAN-htmltools 
Requires:         R-CRAN-crosstalk 
Requires:         R-CRAN-QuickJSR 
Requires:         R-CRAN-jsutils 

%description
Generate fully interactive and dynamic funnel plots and statistical
process control ('SPC') charts. All data manipulation, calculation, and
plotting is done in 'JavaScript', allowing for completely dynamic charts
without the need for a Shiny server. For more details see Spiegelhalter
(2004) <doi:10.1002/sim.1970> and Pfadt & Wheeler (1995)
<doi:10.1901/jaba.1995.28-349>.

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
