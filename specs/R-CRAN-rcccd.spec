%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rcccd
%global packver   0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          Class Cover Catch Digraph Classification

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-RANN 
BuildRequires:    R-CRAN-Rfast 
BuildRequires:    R-CRAN-proxy 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-RANN 
Requires:         R-CRAN-Rfast 
Requires:         R-CRAN-proxy 

%description
Fit Class Cover Catch Digraph Classification models that can be used in
machine learning. Pure and proper and random walk approaches are
available. Methods are explained in Priebe et al. (2001)
<doi:10.1016/S0167-7152(01)00129-8>, Priebe et al. (2003)
<doi:10.1007/s00357-003-0003-7>, and Manukyan and Ceyhan (2016)
<doi:10.48550/arXiv.1904.04564>.

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
