%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Rhobots
%global packver   0.1.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.10
Release:          1%{?dist}%{?buildtag}
Summary:          'BERTopic'-Style Topic Modeling Without 'Python'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-torch 
BuildRequires:    R-CRAN-safetensors 
BuildRequires:    R-CRAN-hfhub 
BuildRequires:    R-CRAN-tok 
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-CRAN-uwot 
BuildRequires:    R-CRAN-dbscan 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-wordpiece 
BuildRequires:    R-CRAN-Rcpp 
Requires:         R-CRAN-torch 
Requires:         R-CRAN-safetensors 
Requires:         R-CRAN-hfhub 
Requires:         R-CRAN-tok 
Requires:         R-CRAN-jsonlite 
Requires:         R-CRAN-uwot 
Requires:         R-CRAN-dbscan 
Requires:         R-CRAN-Matrix 
Requires:         R-stats 
Requires:         R-CRAN-wordpiece 
Requires:         R-CRAN-Rcpp 

%description
Implements the 'BERTopic' topic modeling pipeline directly in R:
transformer-based sentence embedding, Uniform Manifold Approximation and
Projection dimensionality reduction, Hierarchical Density-Based Spatial
Clustering of Applications with Noise clustering, and class-based term
frequency-inverse document frequency topic extraction - all without any
dependency on 'Python', 'conda', or 'reticulate'. Every stage runs in R
through 'torch', 'safetensors', 'tok', 'uwot', and 'dbscan'. The package
mirrors the accessor API of the original 'Python' package, adds integrated
quality metrics and hyperparameter search tools, and introduces
part-of-speech filtered and C-value-ranked representation models.

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
