%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  redistverse
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Easily Install and Load Redistricting Software

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-redist 
BuildRequires:    R-CRAN-redistmetrics 
BuildRequires:    R-CRAN-geomander 
BuildRequires:    R-CRAN-ggredist 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-censable 
BuildRequires:    R-CRAN-tinytiger 
BuildRequires:    R-CRAN-easycensus 
BuildRequires:    R-CRAN-PL94171 
BuildRequires:    R-CRAN-alarmdata 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-birdie 
BuildRequires:    R-CRAN-baf 
Requires:         R-CRAN-redist 
Requires:         R-CRAN-redistmetrics 
Requires:         R-CRAN-geomander 
Requires:         R-CRAN-ggredist 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-censable 
Requires:         R-CRAN-tinytiger 
Requires:         R-CRAN-easycensus 
Requires:         R-CRAN-PL94171 
Requires:         R-CRAN-alarmdata 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-birdie 
Requires:         R-CRAN-baf 

%description
Easy installation, loading, and control of packages for redistricting data
downloading, spatial data processing, simulation, analysis, and
visualization. This package makes it easy to install and load multiple
'redistverse' packages at once. The 'redistverse' is developed and
maintained by the Algorithm-Assisted Redistricting Methodology (ALARM)
Project. For more details see <https://alarm-redist.org>.

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
