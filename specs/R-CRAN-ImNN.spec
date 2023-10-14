%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ImNN
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Neural Networks for Predicting Volume of Forest Trees

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-MLmetrics 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-neuralnet 
Requires:         R-stats 
Requires:         R-CRAN-MLmetrics 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-neuralnet 

%description
Neural network has potential in forestry modelling. This package is
designed to create and assess Artificial Intelligence based Neural
Networks with varying architectures for prediction of volume of forest
trees using two input features: height and diameter at breast height, as
they are the key factors in predicting volume, therefore development and
validation of efficient volume prediction neural network model is
necessary. This package has been developed using the algorithm of Tabassum
et al. (2022) <doi:10.18805/ag.D-5555>.

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
