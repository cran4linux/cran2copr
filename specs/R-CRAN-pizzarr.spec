%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pizzarr
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Slice into 'Zarr' Arrays

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildArch:        noarch
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-qs2 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-utils 
Requires:         R-CRAN-jsonlite 
Requires:         R-stats 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-qs2 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-memoise 
Requires:         R-utils 

%description
An implementation of chunked, compressed, N-dimensional arrays for R.
'Zarr' spec V2 (2024) <doi:10.5281/zenodo.11320255>.

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
