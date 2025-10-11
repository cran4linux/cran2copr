%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  vscc
%global packver   0.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8
Release:          1%{?dist}%{?buildtag}
Summary:          Variable Selection for Clustering and Classification

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ManlyMix 
BuildRequires:    R-CRAN-teigen 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-MixGHD 
Requires:         R-CRAN-ManlyMix 
Requires:         R-CRAN-teigen 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-MixGHD 

%description
Performs variable selection/feature reduction under a clustering or
classification framework. In particular, it can be used in an automated
fashion using mixture model-based methods ('teigen' and 'mclust' are
currently supported). Can account for mixtures of non-Gaussian
distributions via Manly transform (via 'ManlyMix'). See Andrews and
McNicholas (2014) <doi:10.1007/s00357-013-9139-2> and Neal and McNicholas
(2023) <doi:10.48550/arXiv.2305.16464>.

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
