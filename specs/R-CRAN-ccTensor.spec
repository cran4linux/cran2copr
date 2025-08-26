%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ccTensor
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          CUR/CX Tensor Decomposition

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-rTensor 
Requires:         R-methods 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-rTensor 

%description
CUR/CX decomposition factorizes a matrix into two factor matrices and
Multidimensional CX Decomposition factorizes a tensor into a core tensor
and some factor matrices. See the reference section of GitHub README.md
<https://github.com/rikenbit/ccTensor>, for details of the methods.

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
