%global __brp_check_rpaths %{nil}
%global packname  SparseTSCGM
%global packver   4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.0
Release:          1%{?dist}%{?buildtag}
Summary:          Sparse Time Series Chain Graphical Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3.2
Requires:         R-core >= 3.3.2
BuildRequires:    R-CRAN-glasso 
BuildRequires:    R-CRAN-longitudinal 
BuildRequires:    R-CRAN-huge 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-network 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-stats 
Requires:         R-CRAN-glasso 
Requires:         R-CRAN-longitudinal 
Requires:         R-CRAN-huge 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-network 
Requires:         R-CRAN-abind 
Requires:         R-stats 

%description
Computes sparse vector autoregressive coefficients and precision matrices
for time series chain graphical models. Fentaw Abegaz and Ernst Wit (2013)
<doi:10.1093/biostatistics/kxt005>.

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
