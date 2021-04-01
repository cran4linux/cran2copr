%global packname  spatstat.local
%global packver   4.1-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Extension to 'spatstat' for Local Composite Likelihood

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-spatstat.utils >= 2.1
BuildRequires:    R-CRAN-spatstat.data >= 2.0
BuildRequires:    R-CRAN-spatstat.sparse >= 2.0
BuildRequires:    R-CRAN-spatstat.geom >= 2.0
BuildRequires:    R-CRAN-spatstat.core >= 2.0
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-tensor 
Requires:         R-CRAN-spatstat.utils >= 2.1
Requires:         R-CRAN-spatstat.data >= 2.0
Requires:         R-CRAN-spatstat.sparse >= 2.0
Requires:         R-CRAN-spatstat.geom >= 2.0
Requires:         R-CRAN-spatstat.core >= 2.0
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-tensor 

%description
Extension to the 'spatstat' package, enabling the user to fit point
process models to point pattern data by local composite likelihood
('geographically weighted regression').

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
