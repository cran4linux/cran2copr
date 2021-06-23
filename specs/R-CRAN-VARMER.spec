%global __brp_check_rpaths %{nil}
%global packname  VARMER
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Variational Merging

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-deldir 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-gstat 
BuildRequires:    R-CRAN-Metrics 
BuildRequires:    R-CRAN-hydroGOF 
BuildRequires:    R-CRAN-tictoc 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-parallel 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-deldir 
Requires:         R-grDevices 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-gstat 
Requires:         R-CRAN-Metrics 
Requires:         R-CRAN-hydroGOF 
Requires:         R-CRAN-tictoc 
Requires:         R-CRAN-cluster 
Requires:         R-parallel 

%description
A new mathematical formulation to merge observed data with gridded images
of environmental variables using partial differential equations in a
variational setting. The original method was created, developed and
published by Ulloa, Samaniego, Campozano and Ballari (2018)
<doi:10.1002/2017JD027982>.

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
