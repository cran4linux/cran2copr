%global packname  ROI.plugin.clp
%global packver   0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4
Release:          1%{?dist}%{?buildtag}
Summary:          'Clp (Coin-or linear programming)' Plugin for the 'R' Optimization Interface

License:          EPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-clpAPI >= 1.2.7
BuildRequires:    R-CRAN-ROI >= 0.2.5
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-slam 
BuildRequires:    R-Matrix 
Requires:         R-CRAN-clpAPI >= 1.2.7
Requires:         R-CRAN-ROI >= 0.2.5
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-slam 
Requires:         R-Matrix 

%description
Enhances the R Optimization Infrastructure (ROI) package by registering
the COIN-OR Clp open-source solver from the COIN-OR suite
<https://projects.coin-or.org/>. It allows for solving linear programming
with continuous objective variables keeping sparse constraints definition.

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
