%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  aglm
%global packver   0.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Accurate Generalized Linear Model

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-glmnet >= 4.0.2
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-mathjaxr 
Requires:         R-CRAN-glmnet >= 4.0.2
Requires:         R-CRAN-assertthat 
Requires:         R-methods 
Requires:         R-CRAN-mathjaxr 

%description
Provides functions to fit Accurate Generalized Linear Model (AGLM) models,
visualize them, and predict for new data. AGLM is defined as a regularized
GLM which applies a sort of feature transformations using a discretization
of numerical features and specific coding methodologies of dummy
variables. For more information on AGLM, see Suguru Fujita, Toyoto Tanaka,
Kenji Kondo and Hirokazu Iwasawa (2020)
<https://www.institutdesactuaires.com/global/gene/link.php?doc_id=16273&fg=1>.

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
