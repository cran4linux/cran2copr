%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SharkDemography
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Shark Demographic Analyses Using Leslie Matrix Models

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-interp 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-popbio 
BuildRequires:    R-CRAN-iterators 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doFuture 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-interp 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-popbio 
Requires:         R-CRAN-iterators 
Requires:         R-parallel 
Requires:         R-CRAN-doFuture 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-magrittr 

%description
Run Leslie Matrix models using Monte Carlo simulations for any specified
shark species. This package was developed during the publication of Smart,
JJ, White, WT, Baje, L, et al. (2020) "Can multi-species shark longline
fisheries be managed sustainably using size limits? Theoretically, yes.
Realistically, no".J Appl Ecol. 2020; 57; 1847–1860.
<doi:10.1111/1365-2664.13659>.

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
