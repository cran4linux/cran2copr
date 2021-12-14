%global __brp_check_rpaths %{nil}
%global packname  lphom
%global packver   0.3.0-11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.0.11
Release:          1%{?dist}%{?buildtag}
Summary:          Ecological Inference by Linear Programming under Homogeneity

License:          EPL | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Rsymphony >= 0.1.30
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-lpSolve 
Requires:         R-CRAN-Rsymphony >= 0.1.30
Requires:         R-stats 
Requires:         R-CRAN-lpSolve 

%description
Provides a bunch of algorithms based on linear programming for estimating,
under the homogeneity hypothesis, RxC ecological contingency tables (or
vote transition matrices) using exclusively aggregate data (from voting
units). References: Romero, Pavía, Martín and Romero (2020)
<doi:10.1080/02664763.2020.1804842>. Pavía and Romero (2021a)
<doi:10.31124/advance.14716638.v1>. Pavía and Romero (2021b) Symmetry
estimating R×C vote transfer matrices from aggregate data.

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
