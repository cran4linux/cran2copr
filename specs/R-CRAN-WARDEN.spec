%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  WARDEN
%global packver   1.2.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.0
Release:          1%{?dist}%{?buildtag}
Summary:          Workflows for Health Technology Assessments in R using Discrete EveNts

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-doFuture 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-flexsurv 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-progressr 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tidyr 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-future 
Requires:         R-CRAN-doFuture 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-flexsurv 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-progressr 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tidyr 

%description
Toolkit to support and perform discrete event simulations without resource
constraints in the context of health technology assessments (HTA). The
package focuses on cost-effectiveness modelling and aims to be
submission-ready to relevant HTA bodies in alignment with 'NICE TSD 15'
<https://www.sheffield.ac.uk/nice-dsu/tsds/patient-level-simulation>. More
details an examples can be found in the package website
<https://jsanchezalv.github.io/WARDEN/>.

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
