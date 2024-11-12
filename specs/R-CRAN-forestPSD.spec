%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  forestPSD
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Forest Population Structure and Numeric Dynamics

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-TTR 
BuildRequires:    R-CRAN-modelr 
BuildRequires:    R-CRAN-minpack.lm 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-TTR 
Requires:         R-CRAN-modelr 
Requires:         R-CRAN-minpack.lm 
Requires:         R-stats 
Requires:         R-utils 

%description
Analysis of forest population structure and quantitative dynamics is the
research and evaluation of the composition, distribution, age structure
and changes in quantity over time of various populations in the forest. By
deeply understanding these characteristics of forest populations,
scientific basis can be provided for the management, protection and
sustainable utilization of forest resources. This R package conducts a
systematic analysis of forest population structure and quantitative
dynamics through analyzing age structure, compiling life tables,
population quantitative dynamic change indices and time series models, in
order to provide support for forest population protection and sustainable
management. References: Zhang Y, Wang J, Wang X, et
al(2024)<doi:10.3390/plants13070946>. Yuan G, Guo Q, Xie N, et
al(2023)<doi:10.1007/s11629-022-7429-z>.

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
