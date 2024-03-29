%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  NetLogoR
%global packver   1.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Build and Run Spatially Explicit Agent-Based Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-quickPlot >= 1.0.2
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-utils 
Requires:         R-CRAN-quickPlot >= 1.0.2
Requires:         R-CRAN-data.table 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-terra 
Requires:         R-utils 

%description
Build and run spatially explicit agent-based models using only the R
platform. 'NetLogoR' follows the same framework as the 'NetLogo' software
(Wilensky (1999) <http://ccl.northwestern.edu/netlogo/>) and is a
translation in R of the structure and functions of 'NetLogo'. 'NetLogoR'
provides new R classes to define model agents and functions to implement
spatially explicit agent-based models in the R environment. This package
allows benefiting of the fast and easy coding phase from the highly
developed 'NetLogo' framework, coupled with the versatility, power and
massive resources of the R software. Examples of two models from the
NetLogo software repository (Ants
<http://ccl.northwestern.edu/netlogo/models/Ants>) and
Wolf-Sheep-Predation
(<http://ccl.northwestern.edu/netlogo/models/WolfSheepPredation>), and a
third, Butterfly, from Railsback and Grimm (2012)
<https://www.railsback-grimm-abm-book.com/>, all written using 'NetLogoR'
are available. The 'NetLogo' code of the original version of these models
is provided alongside. A programming guide inspired from the 'NetLogo'
Programming Guide
(<https://ccl.northwestern.edu/netlogo/docs/programming.html>) and a
dictionary of 'NetLogo' primitives
(<https://ccl.northwestern.edu/netlogo/docs/dictionary.html>) equivalences
are also available. NOTE: To increment 'time', these functions can use a
for loop or can be integrated with a discrete event simulator, such as
'SpaDES' (<https://cran.r-project.org/package=SpaDES>). The suggested
package 'fastshp' can be installed with 'install.packages("fastshp", repos
= ("<https://rforge.net>"), type = "source")'.

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
