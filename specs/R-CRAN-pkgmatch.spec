%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pkgmatch
%global packver   0.5.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.4
Release:          1%{?dist}%{?buildtag}
Summary:          Find R Packages Matching Either Descriptions or Other R Packages

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-curl >= 6.0.0
BuildRequires:    R-CRAN-brio 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-fs 
BuildRequires:    R-CRAN-httr2 
BuildRequires:    R-CRAN-memoise 
BuildRequires:    R-CRAN-piggyback 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-rvest 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-tokenizers 
BuildRequires:    R-CRAN-treesitter 
BuildRequires:    R-CRAN-treesitter.r 
BuildRequires:    R-CRAN-vctrs 
Requires:         R-CRAN-curl >= 6.0.0
Requires:         R-CRAN-brio 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-fs 
Requires:         R-CRAN-httr2 
Requires:         R-CRAN-memoise 
Requires:         R-CRAN-piggyback 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-rvest 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-tokenizers 
Requires:         R-CRAN-treesitter 
Requires:         R-CRAN-treesitter.r 
Requires:         R-CRAN-vctrs 

%description
Find R packages from CRAN, 'rOpenSci', or Bioconductor corpora. Packages
can be matched to general text descriptions, to names of installed
packages, or to local paths to entire source repositories. The package is
used to list the most similar packages for each new submission to the
'rOpenSci' software peer-review program ('rOpenSci' authors, 2026;
<doi:10.5281/zenodo.18885936>).

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
