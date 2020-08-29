%global packname  amber
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Automated Model Benchmarking R Package

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.4.0
Requires:         R-core >= 3.4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-classInt 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-latex2exp 
BuildRequires:    R-CRAN-ncdf4 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-CRAN-scico 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-CRAN-xtable 
Requires:         R-CRAN-classInt 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-latex2exp 
Requires:         R-CRAN-ncdf4 
Requires:         R-parallel 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-rgeos 
Requires:         R-CRAN-scico 
Requires:         R-CRAN-sp 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-viridis 
Requires:         R-CRAN-xtable 

%description
Functions that quantify how well the Canadian Land Surface Scheme
Including Biogeochemical Cycles (CLASSIC) reproduces land surface
processes when compared against reference data. To summarize model
performance across different statistical metrics, this package employs a
skill score system that was originally developed by Collier et. al.,
(2018) <doi:10.1029/2018MS001354> .

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
