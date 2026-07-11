%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  conflibertR
%global packver   0.5.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.3
Release:          1%{?dist}%{?buildtag}
Summary:          Inference and Fine-Tuning with 'ConfliBERT' Conflict Text Models

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-reticulate >= 1.34
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-reticulate >= 1.34
Requires:         R-CRAN-cli 
Requires:         R-CRAN-tibble 

%description
An interface to 'ConfliBERT', a pretrained language model for analyzing
text about conflict and political violence (Hu et al. (2022)
<doi:10.18653/v1/2022.naacl-main.400>). Provides functions for named
entity recognition, binary and multilabel classification, and question
answering, plus tools to fine-tune custom classifiers, compare several
base model architectures, and run an interactive active-learning loop for
efficiently labeling new data. Models are downloaded from 'Hugging Face'
and run through the 'transformers' library for 'Python' via the
'reticulate' package.

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
