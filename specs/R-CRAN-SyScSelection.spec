%global packname  SyScSelection
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          2%{?dist}
Summary:          Systemic Scenario Selection for Stress Testing

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-stats 
Requires:         R-CRAN-pracma 
Requires:         R-stats 

%description
Quasi-Monte-Carlo algorithm for systematic generation of shock scenarios
from an arbitrary multivariate elliptical distribution. The algorithm
selects a systematic mesh of arbitrary fineness that approximately evenly
covers an isoprobability ellipsoid in d dimensions (Flood, Mark D. &
Korenko, George G. (2013) <doi:10.1080/14697688.2014.926018>). This
package is the 'R' analogy to the 'Matlab' code published by Flood &
Korenko in above-mentioned paper.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
