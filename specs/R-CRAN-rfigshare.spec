%global __brp_check_rpaths %{nil}
%global packname  rfigshare
%global packver   0.3.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.8
Release:          1%{?dist}%{?buildtag}
Summary:          An R Interface to 'figshare'

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-httr >= 0.3
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-RJSONIO 
BuildRequires:    R-CRAN-httpuv 
BuildRequires:    R-CRAN-yaml 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-XML 
Requires:         R-CRAN-httr >= 0.3
Requires:         R-methods 
Requires:         R-CRAN-RJSONIO 
Requires:         R-CRAN-httpuv 
Requires:         R-CRAN-yaml 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-XML 

%description
An R interface to 'figshare'.

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
