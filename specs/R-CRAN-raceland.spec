%global packname  raceland
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Pattern-Based Zoneless Method for Analysis and Visualization ofRacial Topography

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildRequires:    R-CRAN-comat >= 0.7.0
BuildRequires:    R-CRAN-fasterize 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-plotwidgets 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-rgdal 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-fasterize 
Requires:         R-methods 
Requires:         R-CRAN-plotwidgets 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-rgdal 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-comat >= 0.7.0

%description
Implements a computational framework for a pattern-based, zoneless
analysis, and visualization of (ethno)racial topography (Dmowska,
Stepinski, and Nowosad (2020) <doi:10.1016/j.apgeog.2020.102239>). It is a
reimagined approach for analyzing residential segregation and racial
diversity based on the concept of 'landscape’ used in the domain of
landscape ecology.

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
