%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ruimtehol
%global packver   0.3.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.2
Release:          1%{?dist}%{?buildtag}
Summary:          Learn Text 'Embeddings' with 'Starspace'

License:          MPL-2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Rcpp >= 0.11.5
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-BH 
Requires:         R-CRAN-Rcpp >= 0.11.5
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-stats 

%description
Wraps the 'StarSpace' library
<https://github.com/facebookresearch/StarSpace> allowing users to
calculate word, sentence, article, document, webpage, link and entity
'embeddings'. By using the 'embeddings', you can perform text based
multi-label classification, find similarities between texts and
categories, do collaborative-filtering based recommendation as well as
content-based recommendation, find out relations between entities,
calculate graph 'embeddings' as well as perform semi-supervised learning
and multi-task learning on plain text. The techniques are explained in
detail in the paper: 'StarSpace: Embed All The Things!' by Wu et al.
(2017), available at <arXiv:1709.03856>.

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
