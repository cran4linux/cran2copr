%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mantar
%global packver   0.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Missingness Alleviation for Network Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-mathjaxr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-glassoFast 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-mathjaxr 
Requires:         R-stats 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-glassoFast 

%description
Provides functionality for estimating cross-sectional network structures
representing partial correlations while accounting for missing data.
Networks are estimated via neighborhood selection or regularization, with
model selection guided by information criteria. Missing data can be
handled primarily via multiple imputation or a maximum likelihood-based
approach, as demonstrated by Nehler and Schultze (2025a)
<doi:10.31234/osf.io/qpj35> and Nehler and Schultze (2025b)
<doi:10.1080/00273171.2025.2503833>. Deletion-based approaches are also
available but play a secondary role.

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
