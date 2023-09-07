%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  adimpro
%global packver   0.9.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.6
Release:          1%{?dist}%{?buildtag}
Summary:          Adaptive Smoothing of Digital Images

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Recommends:       dcraw
Recommends:       ImageMagick
BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-CRAN-awsMethods >= 1.1.1
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
Requires:         R-CRAN-awsMethods >= 1.1.1
Requires:         R-grDevices 
Requires:         R-methods 

%description
Implements tools for manipulation of digital images and the Propagation
Separation approach by Polzehl and Spokoiny (2006)
<DOI:10.1007/s00440-005-0464-1> for smoothing digital images, see Polzehl
and Tabelow (2007) <DOI:10.18637/jss.v019.i01>.

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
