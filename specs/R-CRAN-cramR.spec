%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  cramR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Cram Method for Efficient Simultaneous Learning and Evaluation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-caret >= 7.0.1
BuildRequires:    R-stats >= 4.3.3
BuildRequires:    R-CRAN-glmnet >= 4.1.8
BuildRequires:    R-CRAN-grf >= 2.4.0
BuildRequires:    R-CRAN-keras >= 2.15.0
BuildRequires:    R-CRAN-magrittr >= 2.0.3
BuildRequires:    R-CRAN-foreach >= 1.5.2
BuildRequires:    R-CRAN-data.table >= 1.16.4
BuildRequires:    R-CRAN-dplyr >= 1.1.4
BuildRequires:    R-CRAN-doParallel >= 1.0.17
BuildRequires:    R-CRAN-DT >= 0.33
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-rjson 
BuildRequires:    R-CRAN-R.devices 
BuildRequires:    R-CRAN-itertools 
BuildRequires:    R-CRAN-iterators 
Requires:         R-CRAN-caret >= 7.0.1
Requires:         R-stats >= 4.3.3
Requires:         R-CRAN-glmnet >= 4.1.8
Requires:         R-CRAN-grf >= 2.4.0
Requires:         R-CRAN-keras >= 2.15.0
Requires:         R-CRAN-magrittr >= 2.0.3
Requires:         R-CRAN-foreach >= 1.5.2
Requires:         R-CRAN-data.table >= 1.16.4
Requires:         R-CRAN-dplyr >= 1.1.4
Requires:         R-CRAN-doParallel >= 1.0.17
Requires:         R-CRAN-DT >= 0.33
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-rjson 
Requires:         R-CRAN-R.devices 
Requires:         R-CRAN-itertools 
Requires:         R-CRAN-iterators 

%description
Performs the Cram method, a general and efficient approach to simultaneous
learning and evaluation using a generic machine learning algorithm. In a
single pass of batched data, the proposed method repeatedly trains a
machine learning algorithm and tests its empirical performance. Because it
utilizes the entire sample for both learning and evaluation, cramming is
significantly more data-efficient than sample-splitting. Unlike
cross-validation, Cram evaluates the final learned model directly,
providing sharper inference aligned with real-world deployment. The method
naturally applies to both policy learning and contextual bandits, where
decisions are based on individual features to maximize outcomes. The
package includes cram_policy() for learning and evaluating individualized
binary treatment rules, cram_ml() to train and assess the population-level
performance of machine learning models, and cram_bandit() for on-policy
evaluation of contextual bandit algorithms. For all three functions, the
package provides estimates of the average outcome that would result if the
model were deployed, along with standard errors and confidence intervals
for these estimates. Details of the method are described in Jia, Imai, and
Li (2024)
<https://www.hbs.edu/ris/Publication%%20Files/2403.07031v1_a83462e0-145b-4675-99d5-9754aa65d786.pdf>
and Jia et al. (2025) <doi:10.48550/arXiv.2403.07031>.

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
