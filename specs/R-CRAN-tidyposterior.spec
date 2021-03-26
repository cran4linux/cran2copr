%global packname  tidyposterior
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Analysis to Compare Models using Resampling Statistics

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-rstanarm >= 2.21.1
BuildRequires:    R-CRAN-tidyr >= 0.7.1
BuildRequires:    R-CRAN-vctrs >= 0.3.0
BuildRequires:    R-CRAN-tune >= 0.1.2.9000
BuildRequires:    R-CRAN-rsample >= 0.0.2
BuildRequires:    R-CRAN-dplyr > 1.0.0
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-generics 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-workflowsets 
Requires:         R-CRAN-rstanarm >= 2.21.1
Requires:         R-CRAN-tidyr >= 0.7.1
Requires:         R-CRAN-vctrs >= 0.3.0
Requires:         R-CRAN-tune >= 0.1.2.9000
Requires:         R-CRAN-rsample >= 0.0.2
Requires:         R-CRAN-dplyr > 1.0.0
Requires:         R-CRAN-rlang 
Requires:         R-utils 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-generics 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-workflowsets 

%description
Bayesian analysis used here to answer the question: "when looking at
resampling results, are the differences between models 'real'?" To answer
this, a model can be created were the performance statistic is the
resampling statistics (e.g. accuracy or RMSE). These values are explained
by the model types. In doing this, we can get parameter estimates for each
model's affect on performance and make statistical (and practical)
comparisons between models. The methods included here are similar to
Benavoli et al (2017) <https://jmlr.org/papers/v18/16-305.html>.

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
