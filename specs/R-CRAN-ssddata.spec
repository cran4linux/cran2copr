%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ssddata
%global packver   2.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Species Sensitivity Distribution Data

License:          Apache License (== 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-chk 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-utils 
Requires:         R-CRAN-chk 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-Rdpack 
Requires:         R-utils 

%description
Reference data sets of species sensitivities to compare the results of
fitting species sensitivity distributions using software such as
'ssdtools' and 'Burrlioz'.  It consists of curated data sets for
individual chemicals from Australian, New Zealand and Canadian
organizations, several data sets from anonymous sources, and larger
uncurated compilations drawn from the ANZTOX, WQBench and EnviroTox
databases. It also includes a data set of the results of fitting various
distributions using different software.

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
