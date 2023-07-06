%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  nutriNetwork
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Structure Learning with Copula Graphical Model

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-parallel 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-glasso 
BuildRequires:    R-CRAN-huge 
BuildRequires:    R-CRAN-tmvtnorm 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-igraph 
Requires:         R-parallel 
Requires:         R-methods 
Requires:         R-CRAN-glasso 
Requires:         R-CRAN-huge 
Requires:         R-CRAN-tmvtnorm 

%description
Statistical tool for learning the structure of direct associations among
variables for continuous data, discrete data and mixed discrete-continuous
data. The package is based on the copula graphical model in Behrouzi and
Wit (2017) <doi:10.1111/rssc.12287>.

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
