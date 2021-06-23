%global __brp_check_rpaths %{nil}
%global packname  kantorovich
%global packver   3.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Kantorovich Distance Between Probability Measures

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    gmp-devel
BuildRequires:    R-devel >= 2.5.3
Requires:         R-core >= 2.5.3
BuildArch:        noarch
BuildRequires:    R-CRAN-rcdd 
BuildRequires:    R-CRAN-gmp 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-lpSolve 
BuildRequires:    R-CRAN-Rglpk 
BuildRequires:    R-CRAN-slam 
BuildRequires:    R-CRAN-CVXR 
Requires:         R-CRAN-rcdd 
Requires:         R-CRAN-gmp 
Requires:         R-methods 
Requires:         R-CRAN-lpSolve 
Requires:         R-CRAN-Rglpk 
Requires:         R-CRAN-slam 
Requires:         R-CRAN-CVXR 

%description
Computes the Kantorovich distance between two probability measures on a
finite set. The Kantorovich distance is also known as the
Monge-Kantorovich distance or the first Wasserstein distance.

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
