%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MLCOPULA
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Classification Models with Copula Functions

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-copula 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-GRIDCOPULA 
BuildRequires:    R-CRAN-kde1d 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-TSP 
Requires:         R-CRAN-copula 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-GRIDCOPULA 
Requires:         R-CRAN-kde1d 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-TSP 

%description
Provides several classifiers based on probabilistic models. These
classifiers allow to model the dependence structure of continuous features
through bivariate copula functions and graphical models, see
Salinas-Gutiérrez et al. (2014) <doi:10.1007/s00180-013-0457-y>.

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
