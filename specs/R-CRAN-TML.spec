%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  TML
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Tropical Geometry Tools for Machine Learning

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-RcppAlgos 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-CRAN-combinat 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-lpSolve 
BuildRequires:    R-CRAN-lpSolveAPI 
BuildRequires:    R-CRAN-magick 
BuildRequires:    R-CRAN-miscTools 
BuildRequires:    R-CRAN-phangorn 
BuildRequires:    R-CRAN-rcdd 
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-phytools 
BuildRequires:    R-CRAN-maps 
BuildRequires:    R-CRAN-cluster 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-RcppAlgos 
Requires:         R-CRAN-Rfast 
Requires:         R-CRAN-combinat 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-lpSolve 
Requires:         R-CRAN-lpSolveAPI 
Requires:         R-CRAN-magick 
Requires:         R-CRAN-miscTools 
Requires:         R-CRAN-phangorn 
Requires:         R-CRAN-rcdd 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-phytools 
Requires:         R-CRAN-maps 
Requires:         R-CRAN-cluster 

%description
Suite of tropical geometric tools for use in machine learning
applications. These methods may be summarized in the following references:
Yoshida, et al. (2022) <arxiv:2209.15045>, Barnhill et al. (2023)
<arxiv:2303.02539>, Barnhill and Yoshida (2023)
<doi:10.21203/rs.3.rs-3047827/v1>, Yoshida et al. (2022)
<arXiv:2206.04206>, and Yoshida et al. (2019)
<doi:10.1007/s11538-018-0493-4>.

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
