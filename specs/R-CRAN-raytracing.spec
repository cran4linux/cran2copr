%global packname  raytracing
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Rossby Wave Ray Tracing

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ncdf4 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-units 
BuildRequires:    R-utils 
Requires:         R-CRAN-ncdf4 
Requires:         R-graphics 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-units 
Requires:         R-utils 

%description
Rossby wave ray paths are traced from a determined source, specified
wavenumber, and direction of propagation. "raytracing" also works with a
set of experiments changing these parameters, making possible the
identification of Rossby wave sources automatically. The theory used here
is based on classical studies, such as Hoskins and Karoly (1981)
<doi:10.1175/1520-0469(1981)038%%3C1179:TSLROA%%3E2.0.CO;2>, Karoly (1983)
<doi:10.1016/0377-0265(83)90013-1>, Hoskins and Ambrizzi (1993)
<doi:10.1175/1520-0469(1993)050%%3C1661:RWPOAR%%3E2.0.CO;2>, and Yang and
Hoskins (1996) <doi:10.1175/1520-0469(1996)053%%3C2365:PORWON%%3E2.0.CO;2>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
