%global __brp_check_rpaths %{nil}
%global packname  autohrf
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Automated Generation of Data-Informed GLM Models in Task-Based fMRI Data Analysis

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-gtools >= 3.9.2
BuildRequires:    R-CRAN-ggplot2 >= 3.3.5
BuildRequires:    R-CRAN-magrittr >= 2.0.2
BuildRequires:    R-CRAN-lubridate >= 1.8.0
BuildRequires:    R-CRAN-foreach >= 1.5.2
BuildRequires:    R-CRAN-cowplot >= 1.1.1
BuildRequires:    R-CRAN-RColorBrewer >= 1.1
BuildRequires:    R-CRAN-dplyr >= 1.0.8
BuildRequires:    R-CRAN-doParallel >= 1.0.17
Requires:         R-CRAN-gtools >= 3.9.2
Requires:         R-CRAN-ggplot2 >= 3.3.5
Requires:         R-CRAN-magrittr >= 2.0.2
Requires:         R-CRAN-lubridate >= 1.8.0
Requires:         R-CRAN-foreach >= 1.5.2
Requires:         R-CRAN-cowplot >= 1.1.1
Requires:         R-CRAN-RColorBrewer >= 1.1
Requires:         R-CRAN-dplyr >= 1.0.8
Requires:         R-CRAN-doParallel >= 1.0.17

%description
Analysis of task-related functional magnetic resonance imaging (fMRI)
activity at the level of individual participants is commonly based on
general linear modelling (GLM) that allows us to estimate to what extent
the blood oxygenation level dependent (BOLD) signal can be explained by
task response predictors specified in the GLM model. The predictors are
constructed by convolving the hypothesised timecourse of neural activity
with an assumed hemodynamic response function (HRF). To get valid and
precise estimates of task response, it is important to construct a model
of neural activity that best matches actual neuronal activity. The
construction of models is most often driven by predefined assumptions on
the components of brain activity and their duration based on the task
design and specific aims of the study. However, our assumptions about the
onset and duration of component processes might be wrong and can also
differ across brain regions. This can result in inappropriate or
suboptimal models, bad fitting of the model to the actual data and invalid
estimations of brain activity. Here we present an approach in which
theoretically driven models of task response are used to define
constraints based on which the final model is derived computationally
using the actual data. Specifically, we developed 'autohrf' — a package
for the 'R' programming language that allows for data-driven estimation of
HRF models. The package uses genetic algorithms to efficiently search for
models that fit the underlying data well. The package uses automated
parameter search to find the onset and duration of task predictors which
result in the highest fitness of the resulting GLM based on the fMRI
signal under predefined restrictions. We evaluate the usefulness of the
'autohrf' package on publicly available datasets of task-related fMRI
activity. Our results suggest that by using 'autohrf' users can find
better task related brain activity models in a quick and efficient manner.

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
