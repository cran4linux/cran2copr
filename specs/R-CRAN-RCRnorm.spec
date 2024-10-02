%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RCRnorm
%global packver   0.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          An Integrated Regression Model for Normalizing 'NanoString nCounter' Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15.0
Requires:         R-core >= 2.15.0
BuildArch:        noarch
BuildRequires:    R-CRAN-truncnorm 
Requires:         R-CRAN-truncnorm 

%description
'NanoString nCounter' is a medium-throughput platform that measures gene
or microRNA expression levels. Here is a publication that introduces this
platform: Malkov (2009) <doi:10.1186/1756-0500-2-80>. Here is the webpage
of 'NanoString nCounter' where you can find detailed information about
this platform
<https://www.nanostring.com/scientific-content/technology-overview/ncounter-technology>.
It has great clinical application, such as diagnosis and prognosis of
cancer. Implements integrated system of random-coefficient hierarchical
regression model to normalize data from 'NanoString nCounter' platform so
that noise from various sources can be removed.

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
