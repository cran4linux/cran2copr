%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  kanjistat
%global packver   0.14.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.14.2
Release:          1%{?dist}%{?buildtag}
Summary:          A Statistical Framework for the Analysis of Japanese Kanji Characters

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1
Requires:         R-core >= 4.1
BuildRequires:    R-CRAN-transport >= 0.15
BuildRequires:    R-methods 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-dendextend 
BuildRequires:    R-CRAN-gsubfn 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-png 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-RANN 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-ROI 
BuildRequires:    R-CRAN-sysfonts 
BuildRequires:    R-CRAN-showtext 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-lifecycle 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-transport >= 0.15
Requires:         R-methods 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-dendextend 
Requires:         R-CRAN-gsubfn 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-png 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-RANN 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-ROI 
Requires:         R-CRAN-sysfonts 
Requires:         R-CRAN-showtext 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-lifecycle 
Requires:         R-CRAN-Rcpp 

%description
Various tools and data sets that support the study of kanji, including
their morphology, decomposition and concepts of distance and similarity
between them.

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
