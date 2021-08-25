%global __brp_check_rpaths %{nil}
%global packname  text2map
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          R Tools for Text Matrices, Embeddings, and Networks

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-qgraph >= 1.6.9
BuildRequires:    R-CRAN-igraph >= 1.2.6
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-text2vec 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-kit 
BuildRequires:    R-CRAN-fastmatch 
BuildRequires:    R-CRAN-mlpack 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-qgraph >= 1.6.9
Requires:         R-CRAN-igraph >= 1.2.6
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-text2vec 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-kit 
Requires:         R-CRAN-fastmatch 
Requires:         R-CRAN-mlpack 
Requires:         R-methods 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-rlang 

%description
This is a collection of libraries and utility functions for computational
text analysis for the social sciences. The functions are optimized for
working with various kinds of text matrices. Focusing on the text matrix
as the primary object – which is represented either as a base R dense
matrix or a 'Matrix' package sparse matrix – allows for a consistent and
intuitive interface that stays close to the underlying mathematical
foundation of computational text analysis. In particular, the package
includes functions for working with word embeddings, text networks, and
document-term matrices. Methods developed in Stoltz and Taylor (2019)
<doi:10.1007/s42001-019-00048-6>, Taylor and Stoltz (2020)
<doi:10.1007/s42001-020-00075-8>, Taylor and Stoltz (2020)
<doi:10.15195/v7.a23>, and Stoltz and Taylor (2021)
<doi:10.1016/j.poetic.2021.101567>.

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
