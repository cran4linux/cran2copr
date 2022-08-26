%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  CDM
%global packver   8.2-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          8.2.6
Release:          1%{?dist}%{?buildtag}
Summary:          Cognitive Diagnosis Modeling

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-polycor 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-mvtnorm 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-CRAN-polycor 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 
Requires:         R-utils 

%description
Functions for cognitive diagnosis modeling and multidimensional item
response modeling for dichotomous and polytomous item responses. This
package enables the estimation of the DINA and DINO model (Junker &
Sijtsma, 2001, <doi:10.1177/01466210122032064>), the multiple group
(polytomous) GDINA model (de la Torre, 2011,
<doi:10.1007/s11336-011-9207-7>), the multiple choice DINA model (de la
Torre, 2009, <doi:10.1177/0146621608320523>), the general diagnostic model
(GDM; von Davier, 2008, <doi:10.1348/000711007X193957>), the structured
latent class model (SLCA; Formann, 1992,
<doi:10.1080/01621459.1992.10475229>) and regularized latent class
analysis (Chen, Li, Liu, & Ying, 2017, <doi:10.1007/s11336-016-9545-6>).
See George, Robitzsch, Kiefer, Gross, and Uenlue (2017)
<doi:10.18637/jss.v074.i02> or Robitzsch and George (2019,
<doi:10.1007/978-3-030-05584-4_26>) for further details on estimation and
the package structure. For tutorials on how to use the CDM package see
George and Robitzsch (2015, <doi:10.20982/tqmp.11.3.p189>) as well as
Ravand and Robitzsch (2015).

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
