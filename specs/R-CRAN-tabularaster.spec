%global packname  tabularaster
%global packver   0.6.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.6.5
Release:          2%{?dist}
Summary:          Tidy Tools for 'Raster' Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.5
Requires:         R-core >= 3.2.5
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-fasterize 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-raster 
BuildRequires:    R-CRAN-silicate 
BuildRequires:    R-CRAN-spatstat 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-fasterize 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-raster 
Requires:         R-CRAN-silicate 
Requires:         R-CRAN-spatstat 
Requires:         R-CRAN-tibble 

%description
Facilities to work with vector and raster data in efficient repeatable and
systematic work flow. Missing functionality in existing packages is
included here to allow extraction from raster data with 'simple features'
and 'Spatial' types and to make extraction consistent and straightforward.
Extract cell numbers from raster data and return the cells as a data frame
rather than as lists of matrices or vectors. The functions here allow
spatial data to be used without special handling for the format currently
in use.

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
