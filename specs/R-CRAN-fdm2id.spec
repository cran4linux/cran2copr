%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fdm2id
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Data Mining and R Programming for Beginners

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-arules 
BuildRequires:    R-CRAN-arulesViz 
BuildRequires:    R-CRAN-FactoMineR 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-pls 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-arules 
Requires:         R-CRAN-arulesViz 
Requires:         R-CRAN-FactoMineR 
Requires:         R-CRAN-nnet 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-mclust 
Requires:         R-methods 
Requires:         R-CRAN-pls 
Requires:         R-stats 
Requires:         R-utils 

%description
Contains functions to simplify the use of data mining methods
(classification, regression, clustering, etc.), for students and beginners
in R programming. Various R packages are used and wrappers are built
around the main functions, to standardize the use of data mining methods
(input/output): it brings a certain loss of flexibility, but also a gain
of simplicity. The package name came from the French "Fouille de Données
en Master 2 Informatique Décisionnelle".

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
