%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  debtkit
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Debt Sustainability Analysis and Fiscal Risk Assessment

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.6.0
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
Requires:         R-CRAN-cli >= 3.6.0
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 

%description
Analyses government debt sustainability using the standard debt dynamics
framework from Blanchard (1990) <doi:10.1787/budget-v2-art12-en> and the
IMF Debt Sustainability Analysis methodology (IMF, 2013) and the Sovereign
Risk and Debt Sustainability Framework (IMF, 2022). Projects debt-to-GDP
paths, decomposes historical debt changes into interest, growth, and
primary balance contributions, and estimates fiscal reaction functions
following Bohn (1998) <doi:10.1162/003355398555793>. Produces stochastic
fan charts via Monte Carlo simulation, standardised stress tests, and IMF-
style heat map risk assessments. Computes S1/S2 sustainability gap
indicators used by the European Commission. All methods are pure
computation with no external dependencies beyond base R; works with fiscal
data from any source.

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
