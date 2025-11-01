%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PredPsych
%global packver   0.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5
Release:          1%{?dist}%{?buildtag}
Summary:          Predictive Approaches in Psychology

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-rpart 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-mclust 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-party 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-statmod 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-rpart 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-mclust 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-party 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-statmod 

%description
Recent years have seen an increased interest in novel methods for
analyzing quantitative data from experimental psychology. Currently,
however, they lack an established and accessible software framework. Many
existing implementations provide no guidelines, consisting of small code
snippets, or sets of packages. In addition, the use of existing packages
often requires advanced programming experience. 'PredPsych' is a
user-friendly toolbox based on machine learning predictive algorithms. It
comprises of multiple functionalities for multivariate analyses of
quantitative behavioral data based on machine learning models.

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
