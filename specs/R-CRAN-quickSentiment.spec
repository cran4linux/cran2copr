%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  quickSentiment
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Fast and Flexible Pipeline for Text Classification

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-quanteda 
BuildRequires:    R-CRAN-stopwords 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-textstem 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-xgboost 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-doParallel 
Requires:         R-CRAN-quanteda 
Requires:         R-CRAN-stopwords 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-textstem 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-xgboost 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-doParallel 

%description
A high-level wrapper that simplifies text classification into three
streamlined steps: preprocessing, model training, and prediction. It
unifies the interface for multiple algorithms (including 'glmnet',
'ranger', and 'xgboost') and vectorization methods (Bag-of-Words, Term
Frequency-Inverse Document Frequency (TF-IDF)), allowing users to go from
raw text to a trained sentiment model in two function calls. The resulting
model artifact automatically handles preprocessing for new datasets in the
third step, ensuring consistent prediction pipelines.

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
