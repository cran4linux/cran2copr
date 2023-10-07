%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cito
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Building and Training Neural Networks

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-coro 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-torch 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-parabar 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-progress 
BuildRequires:    R-CRAN-cli 
Requires:         R-CRAN-coro 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-torch 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-parabar 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-progress 
Requires:         R-CRAN-cli 

%description
Building and training custom neural networks in the typical R syntax. The
'torch' package is used for numerical calculations, which allows for
training on CPU as well as on a graphics card.

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
