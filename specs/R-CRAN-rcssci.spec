%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rcssci
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Visualization of Restricted Cubic Splines

License:          Artistic-2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-pacman 
BuildRequires:    R-CRAN-rms 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-survminer 
BuildRequires:    R-CRAN-segmented 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-Cairo 
Requires:         R-CRAN-pacman 
Requires:         R-CRAN-rms 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-survminer 
Requires:         R-CRAN-segmented 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-Cairo 

%description
Restricted Cubic Splines were performed to explore the shape of
association form of "U, inverted U, L" shape and test linearity or
non-linearity base on "Cox,Logistic,linear" regression, and auto output
Restricted Cubic Splines figures. The Restricted Cubic Splines method were
based on Suli Huang (2022) <doi:10.1016/j.ecoenv.2022.113183>,Amit Kaura
(2019) <doi:10.1136/bmj.l6055>, and Harrell Jr (2015,
ISBN:978-3-319-19424-0 (Print) 978-3-319-19425-7 (Online)).

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
