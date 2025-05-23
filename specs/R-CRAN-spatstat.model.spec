%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  spatstat.model
%global packver   3.3-6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.3.6
Release:          1%{?dist}%{?buildtag}
Summary:          Parametric Statistical Modelling and Inference for the 'spatstat' Family

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-spatstat.geom >= 3.3.4
BuildRequires:    R-CRAN-spatstat.random >= 3.3.3.005
BuildRequires:    R-CRAN-spatstat.explore >= 3.3.0
BuildRequires:    R-CRAN-spatstat.data >= 3.1.4
BuildRequires:    R-CRAN-spatstat.utils >= 3.1.2
BuildRequires:    R-CRAN-spatstat.univar >= 3.1.1
BuildRequires:    R-CRAN-spatstat.sparse >= 3.1.0
BuildRequires:    R-CRAN-goftest >= 1.2.2
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-utils 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-nlme 
BuildRequires:    R-CRAN-rpart 
BuildRequires:    R-CRAN-mgcv 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-abind 
BuildRequires:    R-CRAN-tensor 
Requires:         R-CRAN-spatstat.geom >= 3.3.4
Requires:         R-CRAN-spatstat.random >= 3.3.3.005
Requires:         R-CRAN-spatstat.explore >= 3.3.0
Requires:         R-CRAN-spatstat.data >= 3.1.4
Requires:         R-CRAN-spatstat.utils >= 3.1.2
Requires:         R-CRAN-spatstat.univar >= 3.1.1
Requires:         R-CRAN-spatstat.sparse >= 3.1.0
Requires:         R-CRAN-goftest >= 1.2.2
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-utils 
Requires:         R-methods 
Requires:         R-CRAN-nlme 
Requires:         R-CRAN-rpart 
Requires:         R-CRAN-mgcv 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-abind 
Requires:         R-CRAN-tensor 

%description
Functionality for parametric statistical modelling and inference for
spatial data, mainly spatial point patterns, in the 'spatstat' family of
packages. (Excludes analysis of spatial data on a linear network, which is
covered by the separate package 'spatstat.linnet'.) Supports parametric
modelling, formal statistical inference, and model validation. Parametric
models include Poisson point processes, Cox point processes, Neyman-Scott
cluster processes, Gibbs point processes and determinantal point
processes. Models can be fitted to data using maximum likelihood, maximum
pseudolikelihood, maximum composite likelihood and the method of minimum
contrast. Fitted models can be simulated and predicted. Formal inference
includes hypothesis tests (quadrat counting tests, Cressie-Read tests,
Clark-Evans test, Berman test, Diggle-Cressie-Loosmore-Ford test, scan
test, studentised permutation test, segregation test, ANOVA tests of
fitted models, adjusted composite likelihood ratio test, envelope tests,
Dao-Genton test, balanced independent two-stage test), confidence
intervals for parameters, and prediction intervals for point counts. Model
validation techniques include leverage, influence, partial residuals,
added variable plots, diagnostic plots, pseudoscore residual plots, model
compensators and Q-Q plots.

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
