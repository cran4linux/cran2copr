%global packname  Momocs
%global packver   1.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          Morphometrics using R

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-dendextend 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-geometry 
BuildRequires:    R-CRAN-geomorph 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-jpeg 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-rgeos 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-vegan 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-dendextend 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-geometry 
Requires:         R-CRAN-geomorph 
Requires:         R-CRAN-ggplot2 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-jpeg 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-rgeos 
Requires:         R-CRAN-sp 
Requires:         R-utils 
Requires:         R-CRAN-vegan 
Requires:         R-CRAN-tibble 

%description
The goal of 'Momocs' is to provide a complete, convenient, reproducible
and open-source toolkit for 2D morphometrics. It includes most common 2D
morphometrics approaches on outlines, open outlines, configurations of
landmarks, traditional morphometrics, and facilities for data preparation,
manipulation and visualization with a consistent grammar throughout. It
allows reproducible, complex morphometrics analyses and other
morphometrics approaches should be easy to plug in, or develop from, on
top of this canvas.

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
