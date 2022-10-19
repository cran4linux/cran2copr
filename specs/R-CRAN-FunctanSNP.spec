%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FunctanSNP
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Functional Analysis (with Interactions) for Dense SNP Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-lava 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-fda 
BuildRequires:    R-CRAN-funData 
BuildRequires:    R-graphics 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-lava 
Requires:         R-CRAN-MASS 
Requires:         R-stats 
Requires:         R-CRAN-fda 
Requires:         R-CRAN-funData 
Requires:         R-graphics 

%description
An implementation of revised functional regression models for multiple
genetic variation data, such as single nucleotide polymorphism (SNP) data,
which provides revised functional linear regression models, partially
functional interaction regression analysis with penalty-based techniques
and corresponding drawing functions, etc.(Ruzong Fan, Yifan Wang, James L.
Mills, Alexander F. Wilson, Joan E. Bailey-Wilson, and Momiao Xiong (2013)
<doi:10.1002/gepi.21757>).

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
