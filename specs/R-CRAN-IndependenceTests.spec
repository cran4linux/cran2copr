%global packname  IndependenceTests
%global packver   0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Non-Parametric Tests of Independence Between Random Vectors

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.6.0
Requires:         R-core >= 2.6.0
BuildRequires:    R-CRAN-xtable 
BuildRequires:    R-CRAN-CompQuadForm 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Runuran 
BuildRequires:    R-parallel 
Requires:         R-CRAN-xtable 
Requires:         R-CRAN-CompQuadForm 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Runuran 
Requires:         R-parallel 

%description
Functions for non-parametric tests of independence (mutual or serial)
between some quantitative random vectors, as described in Bilodeau M. and
Lafaye de Micheaux P. (2009) <doi:10.1016/j.jspi.2008.11.006>, in Beran
R., Bilodeau M. and Lafaye de Micheaux P. (2007)
<doi:10.1016/j.jmva.2007.01.009> and in Fan Y., Lafaye de Micheaux P.,
Penev S. and Salopek D. (2017) <doi:10.1016/j.jmva.2016.09.014>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
