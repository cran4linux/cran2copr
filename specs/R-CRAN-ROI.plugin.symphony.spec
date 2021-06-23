%global __brp_check_rpaths %{nil}
%global packname  ROI.plugin.symphony
%global packver   1.0-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          'SYMPHONY' Plug-in for the 'R' Optimization Interface

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    coin-or-SYMPHONY-devel >= 5.6.16
BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ROI >= 0.3.0
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-Rsymphony 
BuildRequires:    R-CRAN-slam 
Requires:         R-CRAN-ROI >= 0.3.0
Requires:         R-methods 
Requires:         R-CRAN-Rsymphony 
Requires:         R-CRAN-slam 

%description
Enhances the R Optimization Infrastructure ('ROI') package by registering
the 'SYMPHONY' open-source solver from the COIN-OR suite. It allows for
solving mixed integer linear programming (MILP) problems as well as all
variants/combinations of LP, IP.

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
