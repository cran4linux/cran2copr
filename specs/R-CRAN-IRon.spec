%global __brp_check_rpaths %{nil}
%global packname  IRon
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Solving Imbalanced Regression Tasks

License:          CC0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ggpubr 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-plot3D 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-scam 
Requires:         R-CRAN-Rcpp 
Requires:         R-stats 
Requires:         R-CRAN-ggpubr 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-plot3D 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-scam 

%description
Imbalanced domain learning has almost exclusively focused on solving
classification tasks, where the objective is to predict cases labelled
with a rare class accurately. Such a well-defined approach for regression
tasks lacked due to two main factors. First, standard regression tasks
assume that each value is equally important to the user. Second, standard
evaluation metrics focus on assessing the performance of the model on the
most common cases. This package contains methods to tackle imbalanced
domain learning problems in regression tasks, where the objective is to
predict extreme (rare) values. The methods contained in this package are:
1) an automatic and non-parametric method to obtain such relevance
functions; 2) visualisation tools; 3) suite of evaluation measures for
optimisation/validation processes; 4) the squared-error relevance area
measure, an evaluation metric tailored for imbalanced regression tasks.
More information can be found in Ribeiro and Moniz (2020)
<doi:10.1007/s10994-020-05900-9>.

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
