%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  shinyLottie
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Seamlessly Integrate 'Lottie' Animations into 'shiny' Applications

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-htmltools 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-htmltools 

%description
Easily integrate and control 'Lottie' animations within 'shiny'
applications', without the need for idiosyncratic expression or use of
'JavaScript'. This includes utilities for generating animation instances,
controlling playback, manipulating animation properties, and more. For
more information on 'Lottie', see: <https://airbnb.io/lottie/#/>.
Additionally, see the official 'Lottie' GitHub repository at
<https://github.com/airbnb/lottie>.

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
