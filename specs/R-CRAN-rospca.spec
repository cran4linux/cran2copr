%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rospca
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Robust Sparse PCA using the ROSPCA Algorithm

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.14.0
Requires:         R-core >= 2.14.0
BuildArch:        noarch
BuildRequires:    R-CRAN-mrfDepth >= 1.0.5
BuildRequires:    R-CRAN-robustbase >= 0.92.6
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-pcaPP 
BuildRequires:    R-CRAN-rrcov 
BuildRequires:    R-CRAN-elasticnet 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-pracma 
Requires:         R-CRAN-mrfDepth >= 1.0.5
Requires:         R-CRAN-robustbase >= 0.92.6
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-parallel 
Requires:         R-CRAN-pcaPP 
Requires:         R-CRAN-rrcov 
Requires:         R-CRAN-elasticnet 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-pracma 

%description
Implementation of robust sparse PCA using the ROSPCA algorithm of Hubert
et al. (2016) <DOI:10.1080/00401706.2015.1093962>.

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
