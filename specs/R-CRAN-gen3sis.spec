%global packname  gen3sis
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          General Engine for Eco-Evolutionary Simulations

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.16
BuildRequires:    R-Matrix 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-gdistance 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-tools 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-Rcpp >= 0.12.16
Requires:         R-Matrix 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-gdistance 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-stringr 
Requires:         R-tools 
Requires:         R-grDevices 

%description
Contains an engine for spatially-explicit eco-evolutionary mechanistic
models with a modular implementation and several support functions. It
allows exploring the consequences of ecological and macroevolutionary
processes across realistic or theoretical spatio-temporal landscapes on
biodiversity patterns as a general term.

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
