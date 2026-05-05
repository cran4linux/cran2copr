%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SmoothPLS
%global packver   0.1.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.5
Release:          1%{?dist}%{?buildtag}
Summary:          Partial Least-Squares Algorithm for Categorical and Scalar Functional Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS >= 7.3.64
BuildRequires:    R-CRAN-fda >= 6.2.0
BuildRequires:    R-stats >= 4.4.1
BuildRequires:    R-utils >= 4.4.1
BuildRequires:    R-CRAN-ggplot2 >= 3.5.1
BuildRequires:    R-CRAN-pls >= 2.8.5
BuildRequires:    R-CRAN-pracma >= 2.4.4
BuildRequires:    R-CRAN-magrittr >= 2.0.3
BuildRequires:    R-CRAN-mgcv >= 1.9.1
BuildRequires:    R-CRAN-tidyr >= 1.3.1
BuildRequires:    R-CRAN-dplyr >= 1.1.4
BuildRequires:    R-CRAN-rlang >= 1.1.0
BuildRequires:    R-CRAN-cfda >= 0.12.1
BuildRequires:    R-CRAN-future.apply 
BuildRequires:    R-CRAN-future 
Requires:         R-CRAN-MASS >= 7.3.64
Requires:         R-CRAN-fda >= 6.2.0
Requires:         R-stats >= 4.4.1
Requires:         R-utils >= 4.4.1
Requires:         R-CRAN-ggplot2 >= 3.5.1
Requires:         R-CRAN-pls >= 2.8.5
Requires:         R-CRAN-pracma >= 2.4.4
Requires:         R-CRAN-magrittr >= 2.0.3
Requires:         R-CRAN-mgcv >= 1.9.1
Requires:         R-CRAN-tidyr >= 1.3.1
Requires:         R-CRAN-dplyr >= 1.1.4
Requires:         R-CRAN-rlang >= 1.1.0
Requires:         R-CRAN-cfda >= 0.12.1
Requires:         R-CRAN-future.apply 
Requires:         R-CRAN-future 

%description
Performs the Partial Least-Squares ('PLS') algorithm for functional data
through the concept of active area integration. This approach builds upon
the basis expansion methods for functional 'PLS' regression described in
Aguilera et al. (2010) <doi:10.1016/j.chemolab.2010.09.007>. The package
seamlessly handles both Scalar Functional Data ('SFD') and Categorical
Functional Data ('CFD'), providing interpretable regression curves even
for discrete state changes. It was developed during a PhD thesis between
'DECATHLON' and French research institute 'INRIA' 2022-2026. The
'SmoothPLS' method does not directly decompose the data into a basis;
rather, it assumes the data is known as precisely as desired, and for
every 'PLS' component, the weight functions are decomposed into the basis.
For both single-state and multi-state 'CFD' as well as 'SFD', the
algorithm is implemented for a scalar response. To provide a baseline, a
naive 'PLS' method on time-value functions and standard Functional 'PLS'
are also implemented.

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
