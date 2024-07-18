%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  sdm
%global packver   1.2-46
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.46
Release:          1%{?dist}%{?buildtag}
Summary:          Species Distribution Modelling

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-terra 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-raster 
Requires:         R-methods 
Requires:         R-CRAN-terra 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-raster 

%description
An extensible framework for developing species distribution models using
individual and community-based approaches, generate ensembles of models,
evaluate the models, and predict species potential distributions in space
and time. For more information, please check the following paper: Naimi,
B., Araujo, M.B. (2016) <doi:10.1111/ecog.01881>.

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
