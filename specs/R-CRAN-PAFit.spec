%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PAFit
%global packver   1.2.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.11
Release:          1%{?dist}%{?buildtag}
Summary:          Generative Mechanism Estimation in Temporal Complex Networks

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildRequires:    R-CRAN-Rcpp >= 0.11.3
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-VGAM 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-magicaxis 
BuildRequires:    R-CRAN-networkDynamic 
BuildRequires:    R-CRAN-network 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-mapproj 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-ggplot2 
Requires:         R-CRAN-Rcpp >= 0.11.3
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-VGAM 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-magicaxis 
Requires:         R-CRAN-networkDynamic 
Requires:         R-CRAN-network 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-mapproj 
Requires:         R-CRAN-knitr 
Requires:         R-methods 
Requires:         R-CRAN-ggplot2 

%description
Statistical methods for estimating preferential attachment and node
fitness generative mechanisms in temporal complex networks are provided.
Thong Pham et al. (2015) <doi:10.1371/journal.pone.0137796>. Thong Pham et
al. (2016) <doi:10.1038/srep32558>. Thong Pham et al. (2020)
<doi:10.18637/jss.v092.i03>. Thong Pham et al. (2021)
<doi:10.1093/comnet/cnab024>.

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
