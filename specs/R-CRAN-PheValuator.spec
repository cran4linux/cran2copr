%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PheValuator
%global packver   2.2.18
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.18
Release:          1%{?dist}%{?buildtag}
Summary:          Rapid Phenotype Evaluation

License:          Apache License 2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.1
Requires:         R-core >= 4.1.1
BuildArch:        noarch
BuildRequires:    R-CRAN-PatientLevelPrediction >= 6.0.4
BuildRequires:    R-CRAN-FeatureExtraction >= 2.1.5
BuildRequires:    R-CRAN-SqlRender >= 1.5.2
BuildRequires:    R-CRAN-dplyr >= 0.7.8
BuildRequires:    R-CRAN-DatabaseConnector 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-ParallelLogger 
BuildRequires:    R-CRAN-tibble 
Requires:         R-CRAN-PatientLevelPrediction >= 6.0.4
Requires:         R-CRAN-FeatureExtraction >= 2.1.5
Requires:         R-CRAN-SqlRender >= 1.5.2
Requires:         R-CRAN-dplyr >= 0.7.8
Requires:         R-CRAN-DatabaseConnector 
Requires:         R-methods 
Requires:         R-CRAN-ParallelLogger 
Requires:         R-CRAN-tibble 

%description
Evaluates phenotype algorithms by developing a diagnostic prediction model
using a set of noisy positives and noisy negatives. It can then apply the
model to a large cohort to create a set of subjects each with a predicted
probability for the health outcome of interest.  This cohort can then be
used to evaluate phenotype algorithms through the calculation of the
necessary performance characteristics - sensitivity, specificity, and
positive and negative predictive value. Based on work by Swerdel (2022)
<doi:10.1016/j.jbi.2022.104177> and Swerdel (2019)
<doi:10.1016/j.jbi.2019.103258>.

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
