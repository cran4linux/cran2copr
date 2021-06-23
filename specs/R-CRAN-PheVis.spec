%global __brp_check_rpaths %{nil}
%global packname  PheVis
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          1%{?dist}%{?buildtag}
Summary:          Automatic Phenotyping of Electronic Health Record at Visit Resolution

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-Rcpp >= 1.0.3
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-knitr 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-viridis 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-Rcpp >= 1.0.3
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-knitr 
Requires:         R-CRAN-lme4 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-randomForest 
Requires:         R-stats 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-viridis 
Requires:         R-CRAN-zoo 

%description
Using Electronic Health Record (EHR) is difficult because most of the time
the true characteristic of the patient is not available. Instead we can
retrieve the International Classification of Disease code related to the
disease of interest or we can count the occurrence of the Unified Medical
Language System. None of them is the true phenotype which needs chart
review to identify. However chart review is time consuming and costly.
'PheVis' is an algorithm which is phenotyping (i.e identify a
characteristic) at the visit level in an unsupervised fashion. It can be
used for chronic or acute diseases. An example of how to use 'PheVis' is
available in the vignette. Basically there are two functions that are to
be used: `train_phevis()` which trains the algorithm and `test_phevis()`
which get the predicted probabilities. The detailed method is described in
preprint by Ferté et al. (2020) <doi:10.1101/2020.06.15.20131458>.

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
