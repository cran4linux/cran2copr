%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  GRANDpriv
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Graph Release with Assured Node Differential Privacy

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-EnvStats 
BuildRequires:    R-CRAN-rmutil 
BuildRequires:    R-CRAN-RSpectra 
BuildRequires:    R-CRAN-diffpriv 
BuildRequires:    R-CRAN-truncnorm 
BuildRequires:    R-CRAN-randnet 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-HCD 
BuildRequires:    R-CRAN-transport 
Requires:         R-CRAN-EnvStats 
Requires:         R-CRAN-rmutil 
Requires:         R-CRAN-RSpectra 
Requires:         R-CRAN-diffpriv 
Requires:         R-CRAN-truncnorm 
Requires:         R-CRAN-randnet 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-HCD 
Requires:         R-CRAN-transport 

%description
Implements a novel method for privatizing network data using differential
privacy. Provides functions for generating synthetic networks based on LSM
(Latent Space Model), applying differential privacy to network latent
positions to achieve overall network privatization, and evaluating the
utility of privatized networks through various network statistics. The
privatize and evaluate functions support both LSM and RDPG (Random Dot
Product Graph). For generating RDPG networks, users are encouraged to use
the 'randnet' package <https://CRAN.R-project.org/package=randnet>. For
more details, see the "proposed method" section of Liu, Bi, and Li (2025)
<doi:10.48550/arXiv.2507.00402>.

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
