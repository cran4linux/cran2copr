%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sarp.snowprofile.pyface
%global packver   0.4.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.3
Release:          1%{?dist}%{?buildtag}
Summary:          'python' Modules from Snowpack and Avalanche Research

License:          CC BY-SA 4.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-sarp.snowprofile >= 1.3.0
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-data.table 
Requires:         R-CRAN-sarp.snowprofile >= 1.3.0
Requires:         R-utils 
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-data.table 

%description
The development of post-processing functionality for simulated snow
profiles by the snow and avalanche community is often done in 'python'.
This package aims to make some of these tools accessible to 'R' users.
Currently integrated modules contain functions to calculate dry snow layer
instabilities in support of avalache hazard assessments following the
publications of Richter, Schweizer, Rotach, and Van Herwijnen (2019)
<doi:10.5194/tc-13-3353-2019>, and Mayer, Van Herwijnen, Techel, and
Schweizer (2022) <doi:10.5194/tc-2022-34>.

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
