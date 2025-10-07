%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  normref
%global packver   0.0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Continuous Norming

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-gamlss 
BuildRequires:    R-CRAN-gamlss.dist 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-openxlsx2 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-withr 
Requires:         R-CRAN-gamlss 
Requires:         R-CRAN-gamlss.dist 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-openxlsx2 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-Rdpack 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-withr 

%description
A toolbox for calculating continuous norms for psychological tests, where
the norms can be age-dependent. The norms are based Generalized Additive
Models for Location, Scale, and Shape (GAMLSS) for the test scores in the
normative sample. The package includes functions for model selection,
reliability estimation, and calculating norms, including confidence
intervals. For more details, see Timmerman et al. (2021)
<doi:10.1037/met0000348>.

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
