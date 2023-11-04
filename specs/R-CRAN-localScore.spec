%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  localScore
%global packver   1.0.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.11
Release:          1%{?dist}%{?buildtag}
Summary:          Package for Sequence Analysis by Local Score

License:          GPL (>= 2) | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildRequires:    R-CRAN-Rcpp >= 0.12.16
BuildRequires:    R-utils 
Requires:         R-CRAN-Rcpp >= 0.12.16
Requires:         R-utils 

%description
Functionalities for calculating the local score and calculating
statistical relevance (p-value) to find a local Score in a sequence of
given distribution (S. Mercier and J.-J. Daudin (2001)
<https://hal.science/hal-00714174/>) ; S. Karlin and S. Altschul (1990)
<https://www.ncbi.nlm.nih.gov/pmc/articles/PMC53667/> ; S. Mercier, D.
Cellier and F. Charlot (2003) <https://hal.science/hal-00937529v1/> ; A.
Lagnoux, S. Mercier and P. Valois (2017)
<doi:10.1093/bioinformatics/btw699> ).

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
