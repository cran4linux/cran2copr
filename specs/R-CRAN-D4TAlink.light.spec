%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  D4TAlink.light
%global packver   2.1.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.9
Release:          1%{?dist}%{?buildtag}
Summary:          FAIR Data - Workflow Management

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-rmarkdown 
BuildRequires:    R-CRAN-openssl 
BuildRequires:    R-utils 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-rmarkdown 
Requires:         R-CRAN-openssl 
Requires:         R-utils 

%description
Tools, methods and processes for the management of analysis workflows.
These lightweight solutions facilitate structuring R&D activities. These
solutions were developed to comply with FAIR principles as discussed by
Jacobsen et al. (2017) <doi:10.1162/dint_r_00024>, and with ALCOA+
principles as proposed by the U.S. FDA.

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
