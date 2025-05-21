%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BFF
%global packver   4.4.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.4.2
Release:          1%{?dist}%{?buildtag}
Summary:          Bayes Factor Functions

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-gsl 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-rlang 
Requires:         R-grDevices 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-gsl 
Requires:         R-stats 
Requires:         R-CRAN-rlang 

%description
Bayes factors represent the ratio of probabilities assigned to data by
competing scientific hypotheses. However, one drawback of Bayes factors is
their dependence on prior specifications that define null and alternative
hypotheses. Additionally, there are challenges in their computation. To
address these issues, we define Bayes factor functions (BFFs) directly
from common test statistics. BFFs express Bayes factors as a function of
the prior densities used to define the alternative hypotheses. These prior
densities are centered on standardized effects, which serve as indices for
the BFF. Therefore, BFFs offer a summary of evidence in favor of
alternative hypotheses that correspond to a range of scientifically
interesting effect sizes. Such summaries remove the need for arbitrary
thresholds to determine "statistical significance." BFFs are available in
closed form and can be easily computed from z, t, chi-squared, and F
statistics. They depend on hyperparameters "r" and "tau^2", which
determine the shape and scale of the prior distributions defining the
alternative hypotheses. Plots of BFFs versus effect size provide
informative summaries of hypothesis tests that can be easily aggregated
across studies.

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
