%global __brp_check_rpaths %{nil}
%global packname  jlsm
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Joint Latent Space Model for Social Networks with Multivariate Attributes

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-ellipse 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-expm 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-lvm4net 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-network 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-MASS 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-CRAN-ellipse 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-expm 
Requires:         R-CRAN-boot 
Requires:         R-CRAN-matrixcalc 
Requires:         R-CRAN-lvm4net 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-network 
Requires:         R-CRAN-Matrix 
Requires:         R-grDevices 

%description
Joint latent space models for social networks and multivariate attributes
using a fast inference approach (Wang et al. (2019) <arXiv:1910.12128>).

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
