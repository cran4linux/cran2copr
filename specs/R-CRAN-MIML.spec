%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MIML
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Machine Learning Imputation, Clustering and Survival Analysis for Longitudinal Proteomic Data

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-lightgbm >= 3.3.0
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-lightgbm >= 3.3.0
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-survival 
Requires:         R-stats 
Requires:         R-utils 

%description
Imputes missing biomarker measurements in a wide longitudinal serum panel
with gradient-boosted decision trees, groups the completed panel by
Bayesian consensus clustering, and compares the resulting patient
subgroups by Kaplan-Meier, log-rank and Cox analysis. The imputation
learner is described in Ke et al. (2017)
<https://papers.nips.cc/paper/6907-lightgbm-a-highly-efficient-gradient-boosting-decision-tree>
and the clustering method in Lock and Dunson (2013)
<doi:10.1093/bioinformatics/btt425>. Imputed values are conditional-mean
predictions, so the procedure is a machine-learning single imputation; the
completions carry no between-imputation variance and must not be pooled by
Rubin's rules. Two panels from Gene Expression Omnibus accession
'GSE65622' are included, one for each survival endpoint.

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
