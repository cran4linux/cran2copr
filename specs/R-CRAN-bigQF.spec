%global __brp_check_rpaths %{nil}
%global packname  bigQF
%global packver   1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Quadratic Forms in Large Matrices

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-svd 
BuildRequires:    R-CRAN-CompQuadForm 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-coxme 
Requires:         R-methods 
Requires:         R-CRAN-svd 
Requires:         R-CRAN-CompQuadForm 
Requires:         R-CRAN-Matrix 
Requires:         R-stats 
Requires:         R-CRAN-coxme 

%description
A computationally-efficient leading-eigenvalue approximation to tail
probabilities and quantiles of large quadratic forms, in particular for
the Sequence Kernel Association Test (SKAT) used in genomics
<doi:10.1002/gepi.22136>. Also provides stochastic singular value
decomposition for dense or sparse matrices.

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
