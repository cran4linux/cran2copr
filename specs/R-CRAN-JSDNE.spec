%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  JSDNE
%global packver   4.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.5
Release:          1%{?dist}%{?buildtag}
Summary:          Estimating the Age using Auricular Surface by DNE

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-molaR 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-Rvcg 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-molaR 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-Rvcg 

%description
The age is estimated by calculating the Dirichlet Normal Energy (DNE) on
the whole auricular surface and the apex of the auricular surface. It
involves three estimation methods: principal component discriminant
analysis (PCQDA), and principal component logistic regression analysis
(PCLR) methods, principal component regression analysis with Southeast
Asian (A_PCR), and principal component regression analysis with
multipopulation (M_PCR). The package is created with the data from the
Louis Lopes Collection in Lisbon, the 21st Century Identified Human
Remains Collection in Coimbra, and the CAL Milano Cemetery Skeletal
Collection in Milan, and the skeletal collection at Khon Kaen University
(KKU) Human Skeletal Research Centre (HSRC), housed in the Department of
Anatomy in the Faculty of Medicine at KKU in Khon Kaen.

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
