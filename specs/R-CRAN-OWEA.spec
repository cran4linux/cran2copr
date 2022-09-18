%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  OWEA
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Optimal Weight Exchange Algorithm for Optimal Designs for Three Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-gtools >= 3.9.3
BuildRequires:    R-CRAN-shiny >= 1.7.2
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-methods 
Requires:         R-CRAN-gtools >= 3.9.3
Requires:         R-CRAN-shiny >= 1.7.2
Requires:         R-CRAN-MASS 
Requires:         R-methods 

%description
An implementation of optimal weight exchange algorithm Yang(2013)
<doi:10.1080/01621459.2013.806268> for three models. They are Crossover
model with subject dropout, crossover model with proportional first order
residual effects and interference model. You can use it to find either
A-opt or D-opt approximate designs. Exact designs can be automatically
rounded from approximate designs and relative efficiency is provided as
well.

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
