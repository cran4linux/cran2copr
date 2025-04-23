%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rob
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Run Orders with Assignment-Expansion Method

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-FMC 
BuildRequires:    R-CRAN-minimalRSD 
Requires:         R-CRAN-FMC 
Requires:         R-CRAN-minimalRSD 

%description
It enables the identification of sequentialexperimentation orders for
factorial designs that jointly reduce bias and the number of level
changes. The method used is that presented by Conto et al. (2025), known
as the Assignment-Expansion method, which consists of adapting the linear
programming assignment problem to generate balanced experimentation
orders. The properties identified are then generalized to designs with a
larger number of factors and levels using the expansion method proposed by
Correa et al. (2009) and later generalized by Bhowmik et al. (2017). For
more details see Conto et al. (2025) <doi:10.1016/j.cie.2024.110844>,
Correa et al. (2009) <doi:10.1080/02664760802499337> and Bhowmik et al.
(2017) <doi:10.1080/03610926.2016.1152490>.

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
