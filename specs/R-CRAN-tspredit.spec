%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tspredit
%global packver   1.0.767
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.767
Release:          1%{?dist}%{?buildtag}
Summary:          Time Series Prediction Integrated Tuning

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-mFilter 
BuildRequires:    R-CRAN-DescTools 
BuildRequires:    R-CRAN-KFAS 
BuildRequires:    R-CRAN-daltoolbox 
Requires:         R-CRAN-dplyr 
Requires:         R-stats 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-mFilter 
Requires:         R-CRAN-DescTools 
Requires:         R-CRAN-KFAS 
Requires:         R-CRAN-daltoolbox 

%description
Prediction is one of the most important activities while working with time
series. There are many alternative ways to model the time series. Finding
the right one is challenging to model them. Most data-driven models
(either statistical or machine learning) demand tuning. Setting them right
is mandatory for good predictions. It is even more complex since time
series prediction also demands choosing a data pre-processing that
complies with the chosen model. Many time series frameworks have features
to build and tune models. The package differs as it provides a framework
that seamlessly integrates tuning data pre-processing activities with the
building of models. The package provides functions for defining and
conducting time series prediction, including data pre(post)processing,
decomposition, tuning, modeling, prediction, and accuracy assessment. More
information is available at Izau et al. <doi:10.5753/sbbd.2022.224330>.

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
