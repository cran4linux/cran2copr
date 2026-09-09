%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  kfda
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Kernel Fisher Discriminant Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-kernlab 
Requires:         R-CRAN-MASS 

%description
Kernel Fisher Discriminant Analysis (KFDA) is performed using Kernel
Principal Component Analysis (KPCA) and Fisher Discriminant Analysis
(FDA). There are some similar packages. First, 'lfda' is a package that
performs Local Fisher Discriminant Analysis (LFDA) and performs other
functions. In particular, 'lfda' seems to be impossible to test because it
needs the label information of the data in the function argument. Also,
the 'ks' package has a limited dimension, which makes it difficult to
analyze properly. This package is a simple and practical package for KFDA
based on the paper of Yang, J., Jin, Z., Yang, J. Y., Zhang, D., and
Frangi, A. F. (2004) <DOI:10.1016/j.patcog.2003.10.015>.

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
