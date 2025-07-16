%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  RootsExtremaInflections
%global packver   1.2.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.5
Release:          1%{?dist}%{?buildtag}
Summary:          Finds Roots, Extrema and Inflection Points of a Curve

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-iterators 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-inflection 
Requires:         R-CRAN-iterators 
Requires:         R-CRAN-foreach 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-inflection 

%description
Implementation of Taylor Regression Estimator (TRE), Tulip Extreme Finding
Estimator (TEFE), Bell Extreme Finding Estimator (BEFE), Integration
Extreme Finding Estimator (IEFE) and Integration Root Finding Estimator
(IRFE) for roots, extrema and inflections of a curve . Christopoulos, DT
(2019) <doi:10.13140/RG.2.2.17158.32324> . Christopoulos, DT (2016)
<doi:10.2139/ssrn.3043076> . Christopoulos, DT (2016)
<https://demovtu.veltech.edu.in/wp-content/uploads/2016/04/Paper-04-2016.pdf>
. Christopoulos, DT (2014) <doi:10.48550/arXiv.1206.5478> .

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
