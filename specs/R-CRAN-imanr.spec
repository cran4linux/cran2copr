%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  imanr
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Identify the Racial Complex of Native Corns from Mexico

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-missForest 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
Requires:         R-CRAN-missForest 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-dplyr 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 

%description
A model that provides researchers with a powerful tool for the
classification and study of native corn by aiding in the identification of
racial complexes which are fundamental to Mexico's agriculture and
culture. This package has been developed based on data collected by
"Proyecto Global de Maíces Nativos México", which has conducted exhaustive
surveys across the country to document the qualitative and quantitative
characteristics of different types of native maize. The trained model uses
a robust and diverse dataset, enabling it to achieve an 80%% accuracy in
classifying maize racial complexes. The characteristics included in the
analysis comprise geographic location, grain and cob colors, as well as
various physical measurements, such as lengths and widths.

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
