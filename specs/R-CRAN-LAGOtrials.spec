%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  LAGOtrials
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Learn-as-You-Go Adaptive Trial Optimization

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-rje 
BuildRequires:    R-CRAN-NlcOptim 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-bslib 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-shinyjs 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-rje 
Requires:         R-CRAN-NlcOptim 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-bslib 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-shinyjs 
Requires:         R-CRAN-Rcpp 

%description
Optimizes interventions for adaptive "Learn-As-you-GO" (LAGO) trials, in
which the intervention package is updated between stages using
accumulating data. Given data from completed stages, lago_optimization()
fits the outcome model (via 'stats' generalized linear models or, for
clustered designs, cluster-robust variance) and computes the cost-optimal
recommended intervention for the next stage that is expected to reach a
target mean outcome and/or a desired statistical power.
get_confidence_set() constructs confidence sets for the optimal
intervention, and visualize_cost() and lago_report() summarize the cost
surface and results. Methods are described in Nevo, Lok and Spiegelman
(2021) <doi:10.1214/20-aos1978> and Bing, Spiegelman, Nevo and Lok (2025)
<doi:10.1093/biomtc/ujaf061>.

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
