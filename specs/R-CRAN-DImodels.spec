%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  DImodels
%global packver   1.3.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.3
Release:          1%{?dist}%{?buildtag}
Summary:          Diversity-Interactions (DI) Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.6.0
Requires:         R-core >= 3.6.0
BuildArch:        noarch
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-hnp 
BuildRequires:    R-CRAN-rootSolve 
BuildRequires:    R-CRAN-multcomp 
BuildRequires:    R-CRAN-multcompView 
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-hnp 
Requires:         R-CRAN-rootSolve 
Requires:         R-CRAN-multcomp 
Requires:         R-CRAN-multcompView 

%description
The 'DImodels' package is suitable for analysing data from biodiversity
and ecosystem function studies using the Diversity-Interactions (DI)
modelling approach introduced by Kirwan et al. (2009)
<doi:10.1890/08-1684.1>. Suitable data will contain proportions for each
species and a community-level response variable, and may also include
additional factors, such as blocks or treatments. The package can perform
data manipulation tasks, such as computing pairwise interactions (the
DI_data() function), can perform an automated model selection process (the
autoDI() function) and has the flexibility to fit a wide range of
user-defined DI models (the DI() function).

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
