%global __brp_check_rpaths %{nil}
%global packname  rcDEA
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Robust and Conditional Data Envelopment Analysis (DEA)

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-np 
BuildRequires:    R-CRAN-Benchmarking 
Requires:         R-CRAN-np 
Requires:         R-CRAN-Benchmarking 

%description
With this package we provide an easy method to compute robust and
conditional Data Envelopment Analysis (DEA), Free Disposal Hull (FDH) and
Benefit of the Doubt (BOD) scores. The robust approach is based on the
work of Cazals, Florens and Simar (2002)
<doi:10.1016/S0304-4076(01)00080-X>. The conditional approach is based on
Daraio and Simar (2007) <doi:10.1007/s11123-007-0049-3>. Besides we
provide graphs to help with the choice of m. We relay on the
'Benchmarking' package to compute the efficiency scores and on the 'np'
package to compute non parametric estimation of similarity among units.

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
