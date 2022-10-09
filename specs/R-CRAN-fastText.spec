%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fastText
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Efficient Learning of Word Representations and Sentence Classification

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildRequires:    R-CRAN-Rcpp >= 1.0.0
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grid 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-stats 
Requires:         R-CRAN-Rcpp >= 1.0.0
Requires:         R-CRAN-ggplot2 
Requires:         R-grid 
Requires:         R-utils 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-data.table 
Requires:         R-stats 

%description
An interface to the 'fastText'
<https://github.com/facebookresearch/fastText> library for efficient
learning of word representations and sentence classification. The
'fastText' algorithm is explained in detail in (i) "Enriching Word Vectors
with subword Information", Piotr Bojanowski, Edouard Grave, Armand Joulin,
Tomas Mikolov, 2017, <doi:10.1162/tacl_a_00051>; (ii) "Bag of Tricks for
Efficient Text Classification", Armand Joulin, Edouard Grave, Piotr
Bojanowski, Tomas Mikolov, 2017, <doi:10.18653/v1/e17-2068>; (iii)
"FastText.zip: Compressing text classification models", Armand Joulin,
Edouard Grave, Piotr Bojanowski, Matthijs Douze, Herve Jegou, Tomas
Mikolov, 2016, <arXiv:1612.03651>.

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
