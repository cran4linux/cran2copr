%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  aifeducation
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Artificial Intelligence for Education

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-reticulate >= 1.34.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.10
BuildRequires:    R-CRAN-iotarelr >= 0.1.5
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-irrCAC 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-smotefamily 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-RcppArmadillo 
Requires:         R-CRAN-reticulate >= 1.34.0
Requires:         R-CRAN-Rcpp >= 1.0.10
Requires:         R-CRAN-iotarelr >= 0.1.5
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-irrCAC 
Requires:         R-methods 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-smotefamily 
Requires:         R-CRAN-stringi 
Requires:         R-utils 

%description
In social and educational settings, the use of Artificial Intelligence
(AI) is a challenging task. Relevant data is often only available in
handwritten forms, or the use of data is restricted by privacy policies.
This often leads to small data sets. Furthermore, in the educational and
social sciences, data is often unbalanced in terms of frequencies. To
support educators as well as educational and social researchers in using
the potentials of AI for their work, this package provides a unified
interface for neural nets in 'PyTorch' to deal with natural language
problems. In addition, the package ships with a shiny app, providing a
graphical user interface.  This allows the usage of AI for people without
skills in writing python/R scripts.  The tools integrate existing
mathematical and statistical methods for dealing with small data sets via
pseudo-labeling (e.g. Cascante-Bonilla et al. (2020)
<doi:10.48550/arXiv.2001.06001>) and imbalanced data via the creation of
synthetic cases (e.g.  Bunkhumpornpat et al. (2012)
<doi:10.1007/s10489-011-0287-y>).  Performance evaluation of AI is
connected to measures from content analysis which educational and social
researchers are generally more familiar with (e.g. Berding & Pargmann
(2022) <doi:10.30819/5581>, Gwet (2014) <ISBN:978-0-9708062-8-4>,
Krippendorff (2019) <doi:10.4135/9781071878781>). Estimation of energy
consumption and CO2 emissions during model training is done with the
'python' library 'codecarbon'.  Finally, all objects created with this
package allow to share trained AI models with other people.

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
