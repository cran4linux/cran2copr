%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  hybridclock
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          How Long Have Hybrids Been Forming? Hybrid Population Histories from Diagnostic Markers

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-Cubist 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-stats 
Requires:         R-CRAN-Cubist 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-parallel 
Requires:         R-CRAN-ranger 
Requires:         R-stats 

%description
Estimates the history of hybrid populations from diagnostic markers, with
or without a genetic map: the average age of the hybrids, how long ago the
rarer species' ancestry entered, the number of backcrosses, and whether
pure animals of the rarer species are still arriving. Population samples
of hybrid index and interspecies heterozygosity, as defined by Fitzpatrick
(2012) <doi:10.1186/1471-2148-12-131>, are compared with forward
simulations that include drift, small breeding groups, sibling mating and
separate breeding pools, so that inbreeding is not mistaken for age.
Estimates come from 'Cubist' models with split-conformal intervals. Recent
hybrids are also classified individually, and the number of markers needed
to detect backcrossed hybrids follows Boecklen and Howard (1997)
<doi:10.1890/0012-9658(1997)078[2611:GAOHZN]2.0.CO;2>.

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
