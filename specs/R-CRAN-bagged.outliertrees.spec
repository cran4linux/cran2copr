%global __brp_check_rpaths %{nil}
%global packname  bagged.outliertrees
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Robust Explainable Outlier Detection Based on OutlierTree

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-outliertree 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-doSNOW 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-rlist 
BuildRequires:    R-CRAN-data.table 
Requires:         R-CRAN-outliertree 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-doSNOW 
Requires:         R-parallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-rlist 
Requires:         R-CRAN-data.table 

%description
Bagged OutlierTrees is an explainable unsupervised outlier detection
method based on an ensemble implementation of the existing OutlierTree
procedure (Cortes, 2020). This implementation takes advantage of bootstrap
aggregating (bagging) to improve robustness by reducing the possible
masking effect and subsequent high variance (similarly to Isolation
Forest), hence the name "Bagged OutlierTrees". To learn more about the
base procedure OutlierTree (Cortes, 2020), please refer to
<arXiv:2001.00636>.

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
