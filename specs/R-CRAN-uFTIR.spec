%global __brp_check_rpaths %{nil}
%global packname  uFTIR
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Process and Analyze Agilent Cary 620 FTIR Microscope Images

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    gdal-devel >= 1.11.4
BuildRequires:    proj-devel >= 4.8.0
BuildRequires:    sqlite-devel
BuildRequires:    R-devel >= 4.0.4.0
Requires:         R-core >= 4.0.4.0
BuildRequires:    R-parallel >= 4.0.4
BuildRequires:    R-methods >= 4.0.4
BuildRequires:    R-CRAN-raster >= 3.4.13
BuildRequires:    R-CRAN-sp >= 1.4.5
BuildRequires:    R-CRAN-Rcpp >= 1.0.7
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-parallel >= 4.0.4
Requires:         R-methods >= 4.0.4
Requires:         R-CRAN-raster >= 3.4.13
Requires:         R-CRAN-sp >= 1.4.5
Requires:         R-CRAN-Rcpp >= 1.0.7

%description
A set of tools to read, process, and summarize Agilent Cary 620 uFTIR
Microscope hyperspectral images primarily intended for microplastic
analysis.

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
