%global __brp_check_rpaths %{nil}
%global packname  crfsuite
%global packver   0.3.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.4
Release:          1%{?dist}%{?buildtag}
Summary:          Conditional Random Fields for Labelling Sequential Data in Natural Language Processing

License:          BSD_3_clause + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-data.table >= 1.9.6
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-utils 
BuildRequires:    R-tools 
BuildRequires:    R-stats 
Requires:         R-CRAN-data.table >= 1.9.6
Requires:         R-CRAN-Rcpp 
Requires:         R-utils 
Requires:         R-tools 
Requires:         R-stats 

%description
Wraps the 'CRFsuite' library <https://github.com/chokkan/crfsuite>
allowing users to fit a Conditional Random Field model and to apply it on
existing data. The focus of the implementation is in the area of Natural
Language Processing where this R package allows you to easily build and
apply models for named entity recognition, text chunking, part of speech
tagging, intent recognition or classification of any category you have in
mind. Next to training, a small web application is included in the package
to allow you to easily construct training data.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
