%global packname  workloopR
%global packver   1.1.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.4
Release:          1%{?dist}%{?buildtag}
Summary:          Analysis of Work Loops and Other Data from Muscle Physiology Experiments

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-pracma >= 2.0.7
BuildRequires:    R-CRAN-signal >= 0.7.6
Requires:         R-CRAN-pracma >= 2.0.7
Requires:         R-CRAN-signal >= 0.7.6

%description
Functions for the import, transformation, and analysis of data from muscle
physiology experiments. The work loop technique is used to evaluate the
mechanical work and power output of muscle. Josephson (1985)
<doi:10.1242/jeb.114.1.493> modernized the technique for application in
comparative biomechanics. Although our initial motivation was to provide
functions to analyze work loop experiment data, as we developed the
package we incorporated the ability to analyze data from experiments that
are often complementary to work loops. There are currently three supported
experiment types: work loops, simple twitches, and tetanus trials. Data
can be imported directly from .ddf files or via an object constructor
function. Through either method, data can then be cleaned or transformed
via methods typically used in studies of muscle physiology. Data can then
be analyzed to determine the timing and magnitude of force development and
relaxation (for isometric trials) or the magnitude of work, net power, and
instantaneous power among other things (for work loops). Although we do
not provide plotting functions, all resultant objects are designed to be
friendly to visualization via either base-R plotting or 'tidyverse'
functions. This package has been peer-reviewed by rOpenSci (v. 1.1.0).

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
