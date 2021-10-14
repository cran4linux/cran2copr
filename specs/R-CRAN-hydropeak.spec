%global __brp_check_rpaths %{nil}
%global packname  hydropeak
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Detect and Characterize Sub-Daily Flow Fluctuations

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-utils 
BuildRequires:    R-parallel 
Requires:         R-utils 
Requires:         R-parallel 

%description
An important environmental impact on running water ecosystems is caused by
hydropeaking - the discontinuous release of turbine water because of peaks
of energy demand. An event-based algorithm is implemented to detect flow
fluctuations referring to increase events (IC) and decrease events (DC).
For each event, a set of parameters related to the fluctuation intensity
is calculated: maximum flow fluctuation rate mafr(), mean flow fluctuation
rate mefr(), amplitude amp(), flow ratio fr(), and duration dur(). The
framework is introduced in Greimel et al. (2016) "A method to detect and
characterize sub-daily flow fluctuations" <doi:10.1002/hyp.10773> and can
be used to identify different fluctuation types according to the potential
source: e.g., sub-daily flow fluctuations caused by hydropeaking,
rainfall, or snow and glacier melt.

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
