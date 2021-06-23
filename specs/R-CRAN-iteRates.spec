%global __brp_check_rpaths %{nil}
%global packname  iteRates
%global packver   3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1
Release:          2%{?dist}%{?buildtag}
Summary:          Parametric rate comparison

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-partitions 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-VGAM 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-apTreeshape 
BuildRequires:    R-CRAN-geiger 
BuildRequires:    R-CRAN-gtools 
Requires:         R-CRAN-partitions 
Requires:         R-stats 
Requires:         R-CRAN-VGAM 
Requires:         R-MASS 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-apTreeshape 
Requires:         R-CRAN-geiger 
Requires:         R-CRAN-gtools 

%description
Iterates through a phylogenetic tree to identify regions of rate variation
using the parametric rate comparison test.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
