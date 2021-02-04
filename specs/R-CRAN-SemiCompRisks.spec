%global packname  SemiCompRisks
%global packver   3.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.4
Release:          1%{?dist}%{?buildtag}
Summary:          Hierarchical Models for Parametric and Semi-Parametric Analyses of Semi-Competing Risks Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    gsl-devel
BuildRequires:    R-devel >= 3.3.0
Requires:         R-core >= 3.3.0
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-Formula 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-Formula 

%description
Hierarchical multistate models are considered to perform the analysis of
independent/clustered semi-competing risks data. The package allows to
choose the specification for model components from a range of options
giving users substantial flexibility, including: accelerated failure time
or proportional hazards regression models; parametric or non-parametric
specifications for baseline survival functions and cluster-specific random
effects distribution; a Markov or semi-Markov specification for terminal
event following non-terminal event. While estimation is mainly performed
within the Bayesian paradigm, the package also provides the maximum
likelihood estimation approach for several parametric models. The package
also includes functions for univariate survival analysis as complementary
analysis tools.

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
