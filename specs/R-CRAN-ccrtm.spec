%global packname  ccrtm
%global packver   0.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.6
Release:          1%{?dist}%{?buildtag}
Summary:          Coupled Chain Radiative Transfer Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.3
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-testthat 
BuildRequires:    R-CRAN-expint 
BuildRequires:    R-CRAN-pracma 
Requires:         R-CRAN-Rcpp >= 1.0.3
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-CRAN-testthat 
Requires:         R-CRAN-expint 
Requires:         R-CRAN-pracma 

%description
A set of radiative transfer models to quantitatively describe the
absorption, reflectance and transmission of solar energy in vegetation,
and model remotely sensed spectral signatures of vegetation at distinct
spatial scales (leaf,canopy and stand). The main principle behind ccrtm is
that many radiative transfer models can form a coupled chain, basically
models that feed into each other in a linked chain (from leaf, to canopy,
to stand, to atmosphere). It allows the simulation of spectral datasets in
the solar spectrum (400-2500nm) using leaf models as PROSPECT5, 5b, and D
which can be coupled with canopy models as 'FLIM', 'SAIL' and 'SAIL2'.
Currently, only a simple atmospheric model ('skyl') is implemented.
Jacquemoud et al 2008 provide the most comprehensive overview of these
models <doi:10.1016/j.rse.2008.01.026>.

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
