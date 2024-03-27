%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  vcPB
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Longitudinal PB Varying-Coefficient Groupwise Disparity Model

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-KernSmooth 
BuildRequires:    R-CRAN-rlist 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-methods 
Requires:         R-CRAN-KernSmooth 
Requires:         R-CRAN-rlist 
Requires:         R-CRAN-lme4 
Requires:         R-methods 

%description
Estimating the disparity between two groups based on the extended model of
the Peters-Belson (PB) method. Our model is the first work on the
longitudinal data, and also can set a varying variable to find the
complicated association between other variables and the varying variable.
Our work is an extension of the Peters-Belson method which was originally
published in Peters (1941)<doi:10.1080/00220671.1941.10881036> and Belson
(1956)<doi:10.2307/2985420>.

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
