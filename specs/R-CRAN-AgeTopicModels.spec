%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  AgeTopicModels
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Inferring Age-Dependent Disease Topic from Diagnosis Data

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-pROC 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-utils 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggrepel 
Requires:         R-grDevices 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-pROC 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-utils 

%description
We propose an age-dependent topic modelling (ATM) model, providing a
low-rank representation of longitudinal records of hundreds of distinct
diseases in large electronic health record data sets. The model assigns to
each individual topic weights for several disease topics; each disease
topic reflects a set of diseases that tend to co-occur as a function of
age, quantified by age-dependent topic loadings for each disease. The
model assumes that for each disease diagnosis, a topic is sampled based on
the individual’s topic weights (which sum to 1 across topics, for a given
individual), and a disease is sampled based on the individual’s age and
the age-dependent topic loadings (which sum to 1 across diseases, for a
given topic at a given age). The model generalises the Latent Dirichlet
Allocation (LDA) model by allowing topic loadings for each topic to vary
with age. References: Jiang (2023) <doi:10.1038/s41588-023-01522-8>.

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
