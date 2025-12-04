%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  idiolect
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Forensic Authorship Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-quanteda 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-fdrtool 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-kgrams 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-proxy 
BuildRequires:    R-CRAN-quanteda.textstats 
BuildRequires:    R-CRAN-spacyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-textclean 
Requires:         R-CRAN-quanteda 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-fdrtool 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-kgrams 
Requires:         R-CRAN-pbapply 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-proxy 
Requires:         R-CRAN-quanteda.textstats 
Requires:         R-CRAN-spacyr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-textclean 

%description
Carry out comparative authorship analysis of disputed and undisputed texts
within the Likelihood Ratio Framework for expressing evidence in forensic
science. This package contains implementations of well-known algorithms
for comparative authorship analysis, such as Smith and Aldridge's (2011)
Cosine Delta <doi:10.1080/09296174.2011.533591> or Koppel and Winter's
(2014) Impostors Method <doi:10.1002/asi.22954>, as well as functions to
measure their performance and to calibrate their outputs into
Log-Likelihood Ratios.

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
