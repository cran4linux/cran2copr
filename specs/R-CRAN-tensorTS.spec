%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tensorTS
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Factor and Autoregressive Models for Tensor Time Series

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-tensor 
BuildRequires:    R-CRAN-rTensor 
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-graphics 
Requires:         R-CRAN-tensor 
Requires:         R-CRAN-rTensor 
Requires:         R-CRAN-expm 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-pracma 
Requires:         R-graphics 

%description
Factor and autoregressive models for matrix and tensor valued time series.
We provide functions for estimation, simulation and prediction. The models
are discussed in Li et al (2021) <doi:10.48550/arXiv.2110.00928>, Chen et
al (2020) <DOI:10.1080/01621459.2021.1912757>, Chen et al (2020)
<DOI:10.1016/j.jeconom.2020.07.015>, and Xiao et al (2020)
<doi:10.48550/arXiv.2006.02611>.

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
