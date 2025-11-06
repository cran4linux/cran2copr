%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  EpidigiR
%global packver   0.1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Digital Epidemiological Analysis and Visualization Tools

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-deSolve 
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-tm 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-survival 
Requires:         R-CRAN-deSolve 
Requires:         R-CRAN-sp 
Requires:         R-CRAN-tm 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-survival 

%description
Integrates methods for epidemiological analysis, modeling, and
visualization, including functions for summary statistics, SIR
(Susceptible-Infectious-Recovered) modeling, DALY (Disability-Adjusted
Life Years) estimation, age standardization, diagnostic test evaluation,
NLP (Natural Language Processing) keyword extraction, clinical trial power
analysis, survival analysis, SNP (Single Nucleotide Polymorphism)
association, and machine learning methods such as logistic regression,
k-means clustering, Random Forest, and Support Vector Machine (SVM).
Includes datasets for prevalence estimation, SIR modeling, genomic
analysis, clinical trials, DALY, diagnostic tests, and survival analysis.
Methods are based on Gelman et al. (2013) <doi:10.1201/b16018> and Wickham
et al. (2019, ISBN:9781492052040>.

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
