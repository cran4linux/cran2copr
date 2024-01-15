%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CoastlineFD
%global packver   1.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Calculation of the Fractal Dimension of a Coastline

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-sf 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-readxl 
BuildRequires:    R-CRAN-writexl 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-sfheaders 
Requires:         R-CRAN-sf 
Requires:         R-CRAN-tidyr 
Requires:         R-utils 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-readxl 
Requires:         R-CRAN-writexl 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-sfheaders 

%description
Calculating the fractal dimension of a coastline using the boxes and
dividers methods.

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
