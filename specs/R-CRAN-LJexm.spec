%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  LJexm
%global packver   1.0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Extract, Convert, and Merge 'pdf' Files from 'zip' Files

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-pdftools 
BuildRequires:    R-CRAN-rstudioapi 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-webshot 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-pdftools 
Requires:         R-CRAN-rstudioapi 
Requires:         R-utils 
Requires:         R-CRAN-webshot 

%description
Extracts 'zip' files, converts 'Word', 'Excel', and 'html'/'htm' files to
'pdf' format. 'Word' and 'Excel' conversion uses 'VBScript', while
'html'/'htm' conversion uses 'webshot' and 'PhantomJS'. Additionally, the
package merges 'pdf' files into a single document. This package is only
supported on 'Windows' due to 'VBScript' dependencies.

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
