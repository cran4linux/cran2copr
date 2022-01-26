%global __brp_check_rpaths %{nil}
%global packname  rrcov3way
%global packver   0.2-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Robust Methods for Multiway Data Analysis, Applicable also for Compositional Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-rrcov 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-ThreeWay 
BuildRequires:    R-CRAN-nnls 
BuildRequires:    R-CRAN-pracma 
Requires:         R-CRAN-rrcov 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-ThreeWay 
Requires:         R-CRAN-nnls 
Requires:         R-CRAN-pracma 

%description
Provides methods for multiway data analysis by means of Parafac and Tucker
3 models. Robust versions (Engelen and Hubert (2011)
<doi:10.1016/j.aca.2011.04.043>) and versions for compositional data are
also provided (Gallo (2015) <doi:10.1080/03610926.2013.798664>, Di Palma
et al. (2018) <doi:10.1080/02664763.2017.1381669>.

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
