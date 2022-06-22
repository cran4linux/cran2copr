%global __brp_check_rpaths %{nil}
%global packname  micEconSNQP
%global packver   0.6-10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.10
Release:          1%{?dist}%{?buildtag}
Summary:          Symmetric Normalized Quadratic Profit Function

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.4.0
Requires:         R-core >= 2.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-systemfit >= 1.0.0
BuildRequires:    R-CRAN-miscTools >= 0.6.1
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-systemfit >= 1.0.0
Requires:         R-CRAN-miscTools >= 0.6.1
Requires:         R-CRAN-MASS 

%description
Tools for econometric production analysis with the Symmetric Normalized
Quadratic (SNQ) profit function, e.g. estimation, imposing convexity in
prices, and calculating elasticities and shadow prices.

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
