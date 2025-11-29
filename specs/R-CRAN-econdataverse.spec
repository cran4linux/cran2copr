%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  econdataverse
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Easily Load and Install the 'EconDataverse'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.6.1
BuildRequires:    R-CRAN-econdatasets 
BuildRequires:    R-CRAN-econid 
BuildRequires:    R-CRAN-econtools 
BuildRequires:    R-CRAN-imfapi 
BuildRequires:    R-CRAN-imfweo 
BuildRequires:    R-CRAN-oecdoda 
BuildRequires:    R-CRAN-owidapi 
BuildRequires:    R-CRAN-uisapi 
BuildRequires:    R-CRAN-wbids 
BuildRequires:    R-CRAN-wbwdi 
Requires:         R-CRAN-cli >= 3.6.1
Requires:         R-CRAN-econdatasets 
Requires:         R-CRAN-econid 
Requires:         R-CRAN-econtools 
Requires:         R-CRAN-imfapi 
Requires:         R-CRAN-imfweo 
Requires:         R-CRAN-oecdoda 
Requires:         R-CRAN-owidapi 
Requires:         R-CRAN-uisapi 
Requires:         R-CRAN-wbids 
Requires:         R-CRAN-wbwdi 

%description
The 'EconDataverse' is a universe of open-source packages to work
seamlessly with economic data. This package is designed to make it easy to
install and load multiple 'EconDataverse' packages in a single step. Learn
more about the 'EconDataverse' at <https://www.econdataverse.org>.

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
