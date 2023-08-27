%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  beezdemand
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Behavioral Economic Easy Demand

License:          GPL-2 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.5
Requires:         R-core >= 2.5
BuildArch:        noarch
BuildRequires:    R-CRAN-nlsr 
BuildRequires:    R-CRAN-nlstools 
BuildRequires:    R-CRAN-nls2 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-optimx 
Requires:         R-CRAN-nlsr 
Requires:         R-CRAN-nlstools 
Requires:         R-CRAN-nls2 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-reshape2 
Requires:         R-stats 
Requires:         R-CRAN-optimx 

%description
Facilitates many of the analyses performed in studies of behavioral
economic demand. The package supports commonly-used options for modeling
operant demand including (1) data screening proposed by Stein, Koffarnus,
Snider, Quisenberry, & Bickel (2015; <doi:10.1037/pha0000020>), (2)
fitting models of demand such as linear (Hursh, Raslear, Bauman, & Black,
1989, <doi:10.1007/978-94-009-2470-3_22>), exponential (Hursh &
Silberberg, 2008, <doi:10.1037/0033-295X.115.1.186>) and modified
exponential (Koffarnus, Franck, Stein, & Bickel, 2015,
<doi:10.1037/pha0000045>), and (3) calculating numerous measures relevant
to applied behavioral economists (Intensity, Pmax, Omax). Also supports
plotting and comparing data.

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
