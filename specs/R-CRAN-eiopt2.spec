%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  eiopt2
%global packver   0.1.1-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1.6
Release:          1%{?dist}%{?buildtag}
Summary:          Ecological Inference for RxC Tables via Nonlinear Quadratic Optimization

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-alabama 
BuildRequires:    R-CRAN-quadprog 
Requires:         R-CRAN-alabama 
Requires:         R-CRAN-quadprog 

%description
Estimates RxC (R by C) vote transfer matrices (ecological contingency
tables) from aggregate data by simultaneously minimizing Euclidean
row-standardized unit-to-global distances. Acknowledgements: The authors
wish to thank Generalitat Valenciana, Consellería de Educación, Cultura,
Universidades y Empleo (grant CIAICO/2023/031) for supporting this
research.

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
