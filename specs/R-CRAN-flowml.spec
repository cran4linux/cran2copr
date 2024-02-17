%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  flowml
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          A Backend for a 'nextflow' Pipeline that Performs Machine-Learning-Based Modeling of Biomedical Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ABCanalysis 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-fastshap 
BuildRequires:    R-CRAN-furrr 
BuildRequires:    R-CRAN-future 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-optparse 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-rjson 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-CRAN-rsample 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-vip 
Requires:         R-CRAN-ABCanalysis 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-fastshap 
Requires:         R-CRAN-furrr 
Requires:         R-CRAN-future 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-optparse 
Requires:         R-parallel 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-rjson 
Requires:         R-CRAN-rlang 
Requires:         R-CRAN-rsample 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-utils 
Requires:         R-CRAN-vip 

%description
Provides functionality to perform machine-learning-based modeling in a
computation pipeline. Its functions contain the basic steps of
machine-learning-based knowledge discovery workflows, including model
training and optimization, model evaluation, and model testing. To perform
these tasks, the package builds heavily on existing machine-learning
packages, such as 'caret' <https://github.com/topepo/caret/> and
associated packages. The package can train multiple models, optimize model
hyperparameters by performing a grid search or a random search, and
evaluates model performance by different metrics. Models can be validated
either on a test data set, or in case of a small sample size by k-fold
cross validation or repeated bootstrapping. It also allows for
0-Hypotheses generation by performing permutation experiments.
Additionally, it offers methods of model interpretation and item
categorization to identify the most informative features from a high
dimensional data space. The functions of this package can easily be
integrated into computation pipelines (e.g. 'nextflow'
<https://www.nextflow.io/>) and hereby improve scalability,
standardization, and re-producibility in the context of machine-learning.

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
