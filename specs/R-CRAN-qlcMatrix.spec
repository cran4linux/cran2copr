%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  qlcMatrix
%global packver   0.9.8
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.8
Release:          1%{?dist}%{?buildtag}
Summary:          Utility Sparse Matrix Functions for Quantitative Language Comparison

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2
Requires:         R-core >= 3.2
BuildArch:        noarch
BuildRequires:    R-CRAN-Matrix >= 1.2
BuildRequires:    R-CRAN-slam >= 0.1.32
BuildRequires:    R-CRAN-sparsesvd 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-docopt 
Requires:         R-CRAN-Matrix >= 1.2
Requires:         R-CRAN-slam >= 0.1.32
Requires:         R-CRAN-sparsesvd 
Requires:         R-methods 
Requires:         R-CRAN-docopt 

%description
Extension of the functionality of the 'Matrix' package for using sparse
matrices. Some of the functions are very general, while other are highly
specific for special data format as used for quantitative language
comparison.

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
