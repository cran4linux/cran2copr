%global packname  semtree
%global packver   0.9.16
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.16
Release:          1%{?dist}%{?buildtag}
Summary:          Recursive Partitioning for Structural Equation Models

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-rpart.plot >= 3.0.6
BuildRequires:    R-CRAN-OpenMx >= 2.6.9
BuildRequires:    R-CRAN-bitops 
BuildRequires:    R-CRAN-sets 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-rpart 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-strucchange 
BuildRequires:    R-CRAN-sandwich 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-clisymbols 
BuildRequires:    R-CRAN-future.apply 
Requires:         R-CRAN-rpart.plot >= 3.0.6
Requires:         R-CRAN-OpenMx >= 2.6.9
Requires:         R-CRAN-bitops 
Requires:         R-CRAN-sets 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-rpart 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-lavaan 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-tidyr 
Requires:         R-methods 
Requires:         R-CRAN-strucchange 
Requires:         R-CRAN-sandwich 
Requires:         R-CRAN-zoo 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-clisymbols 
Requires:         R-CRAN-future.apply 

%description
SEM Trees and SEM Forests -- an extension of model-based decision trees
and forests to Structural Equation Models (SEM). SEM trees hierarchically
split empirical data into homogeneous groups each sharing similar data
patterns with respect to a SEM by recursively selecting optimal predictors
of these differences. SEM forests are an extension of SEM trees. They are
ensembles of SEM trees each built on a random sample of the original data.
By aggregating over a forest, we obtain measures of variable importance
that are more robust than measures from single trees. A description of the
method was published by Brandmaier, von Oertzen, McArdle, & Lindenberger
(2013; <doi:10.1037/a0030001>) and Arnold, Voelkle, & Brandmaier (2020;
<doi:10.3389/fpsyg.2020.564403>).

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
