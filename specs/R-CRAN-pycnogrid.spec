%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pycnogrid
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Flexible Pycnophylactic Interpolation to Discrete Global and Local Grid Systems

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-a5R 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-h3o 
BuildRequires:    R-CRAN-hexify 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-s2 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-sfdep 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-a5R 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-h3o 
Requires:         R-CRAN-hexify 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-s2 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-sfdep 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-tibble 

%description
Provides tools for pycnophylactic interpolation of polygon totals to
discrete global and local grid systems. The method follows Tobler (1979)
<doi:10.1080/01621459.1979.10481647>, preserving source-zone totals while
smoothing values across neighboring target cells.

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
