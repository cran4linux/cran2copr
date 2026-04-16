%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mcmsector
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Estimating Subnational Public and Private Contraceptive Supply Shares Over Time

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0
Requires:         R-core >= 4.0
BuildArch:        noarch
BuildRequires:    R-CRAN-haven 
BuildRequires:    R-CRAN-survey 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-openxlsx 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-labelled 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-haven 
Requires:         R-CRAN-survey 
Requires:         R-stats 
Requires:         R-CRAN-openxlsx 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-labelled 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 

%description
Engaging the private sector in contraceptive method supply is critical for
equitable, sustainable, and accessible healthcare systems. This package
implements Bayesian hierarchical models to estimate public and private
contraceptive supply shares over time at national and subnational levels,
using Demographic and Health Survey (DHS) data. Penalized splines are used
to track supply shares over time, and spatial correlation structures link
national and subnational estimates in data- sparse settings. For more
details see Comiskey (2025) <doi:10.48550/arXiv.2510.25153>.

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
