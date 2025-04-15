%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  msigdbr
%global packver   10.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          10.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          MSigDB Gene Sets for Multiple Organisms in a Tidy Data Format

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildArch:        noarch
BuildRequires:    R-CRAN-babelgene >= 22.9
BuildRequires:    R-CRAN-tidyselect >= 1.2.0
BuildRequires:    R-CRAN-dplyr >= 1.1.1
BuildRequires:    R-CRAN-assertthat 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-babelgene >= 22.9
Requires:         R-CRAN-tidyselect >= 1.2.0
Requires:         R-CRAN-dplyr >= 1.1.1
Requires:         R-CRAN-assertthat 
Requires:         R-CRAN-lifecycle 
Requires:         R-methods 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-tibble 

%description
Provides the 'Molecular Signatures Database' (MSigDB) gene sets typically
used with the 'Gene Set Enrichment Analysis' (GSEA) software (Subramanian
et al. 2005 <doi:10.1073/pnas.0506580102>, Liberzon et al. 2015
<doi:10.1016/j.cels.2015.12.004>, Castanza et al. 2023
<doi:10.1038/s41592-023-02014-7>) as an R data frame. The package includes
the human genes as listed in MSigDB as well as the corresponding symbols
and IDs for frequently studied model organisms such as mouse, rat, pig,
fly, and yeast.

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
