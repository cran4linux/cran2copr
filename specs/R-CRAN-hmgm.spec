%global packname  hmgm
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          High-Dimensional Mixed Graphical Models Estimation

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-rgl 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-nat 
BuildRequires:    R-CRAN-binaryLogic 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
Requires:         R-CRAN-rgl 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-glmnet 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-nat 
Requires:         R-CRAN-binaryLogic 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 
Requires:         R-methods 

%description
Provides weighted lasso framework for high-dimensional mixed data graph
estimation. In the graph estimation stage, the graph structure is
estimated by maximizing the conditional likelihood of one variable given
the rest. We focus on the conditional loglikelihood of each variable and
fit separate regressions to estimate the parameters, much in the spirit of
the neighborhood selection approach proposed by Meinshausen-Buhlmann for
the Gaussian Graphical Model and by Ravikumar for the Ising Model.
Currently, the discrete variables can only take two values. In the future,
method for general discrete data and for visualizing the estimated graph
will be added. For more details, see the linked paper.

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
