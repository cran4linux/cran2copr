%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  biplotEZ
%global packver   2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.0
Release:          1%{?dist}%{?buildtag}
Summary:          EZ-to-Use Biplots

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-splines 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-withr 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-plotrix 
Requires:         R-splines 
Requires:         R-stats 
Requires:         R-CRAN-withr 

%description
Provides users with an EZ-to-use platform for representing data with
biplots. Currently principal component analysis (PCA) and canonical
variate analysis (CVA) biplots are included. This is accompanied by
various formatting options for the samples and axes. Alpha-bags and
concentration ellipses are included for visual enhancements and
interpretation. For an extensive discussion on the topic, see Gower, J.C.,
Lubbe, S. and le Roux, N.J. (2011, ISBN: 978-0-470-01255-0) Understanding
Biplots. Wiley: Chichester.

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
