%global packname  BWGS
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          BreedWheat Genomic Selection Pipeline

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rrBLUP 
BuildRequires:    R-CRAN-BGLR 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-brnn 
BuildRequires:    R-CRAN-e1071 
Requires:         R-CRAN-rrBLUP 
Requires:         R-CRAN-BGLR 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-brnn 
Requires:         R-CRAN-e1071 

%description
Package for Breed Wheat Genomic Selection Pipeline. The R package 'BWGS'
is developed by Gilles Charmet <gilles.charmet@inra.fr>. This repository
is forked from original repository
<https://forgemia.inra.fr/umr-gdec/bwgs> and modified as a R package.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
