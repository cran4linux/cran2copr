%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  funpca
%global packver   9.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          9.0
Release:          1%{?dist}%{?buildtag}
Summary:          Functional Principal Component Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-Brobdingnag 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-fda 
Requires:         R-CRAN-Brobdingnag 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-fda 

%description
Functional principal component analysis under the Linear Mixed Models
representation of smoothing splines. The method utilizes the
Demmler-Reinsch basis and assumes error independence. For more details
see: F. Rosales (2016)
<https://ediss.uni-goettingen.de/handle/11858/00-1735-0000-0028-87F9-6>.

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
