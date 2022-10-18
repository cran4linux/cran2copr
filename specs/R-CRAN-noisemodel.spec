%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  noisemodel
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Noise Models for Classification Datasets

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-classInt 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ExtDist 
BuildRequires:    R-CRAN-lsr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-RSNNS 
BuildRequires:    R-CRAN-C50 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-FNN 
Requires:         R-CRAN-classInt 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ExtDist 
Requires:         R-CRAN-lsr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-RSNNS 
Requires:         R-CRAN-C50 

%description
Implementation of models for the controlled introduction of errors in
classification datasets. This package contains the noise models described
in Saez (2022) <doi:10.3390/math10203736> that allow corrupting class
labels, attributes and both simultaneously.

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
