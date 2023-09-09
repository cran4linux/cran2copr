%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rebib
%global packver   0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          Convert and Aggregate Bibliographies

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-tools 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-logger 
BuildRequires:    R-CRAN-xfun 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-whisker 
Requires:         R-tools 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-logger 
Requires:         R-CRAN-xfun 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-whisker 

%description
Authors working with 'LaTeX' articles use the built-in bibliography
options and 'BibTeX' files. While this might work with 'LaTeX', it does
not function well with Web articles. As a way out, 'rebib' offers tools to
convert and combine bibliographies from both sources.

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
