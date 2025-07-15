%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  classmap
%global packver   1.2.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2.6
Release:          1%{?dist}%{?buildtag}
Summary:          Visualizing Classification Results

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-robustbase 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-cellWise 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-kernlab 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-rpart 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-scales 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-robustbase 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-cellWise 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-kernlab 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-rpart 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-scales 

%description
Tools to visualize the results of a classification or a regression. The
graphical displays include stacked plots, silhouette plots, quasi residual
plots, class maps, predictions plots, and predictions correlation plots.
Implements the techniques described and illustrated in Raymaekers J.,
Rousseeuw P.J., Hubert M. (2022). Class maps for visualizing
classification results. emph{Technometrics}, 64(2), 151–165.
doi{10.1080/00401706.2021.1927849} (open access), Raymaekers J.,
Rousseeuw P.J.(2022). Silhouettes and quasi residual plots for neural nets
and tree-based classifiers. emph{Journal of Computational and Graphical
Statistics}, 31(4), 1332–1343. doi{10.1080/10618600.2022.2050249}, and
Rousseeuw, P.J. (2025). Explainable Linear and Generalized Linear Models
by the Predictions Plot. <doi:10.48550/arXiv.2412.16980> (open access).
Examples can be found in the vignettes:
"Discriminant_analysis_examples","K_nearest_neighbors_examples",
"Support_vector_machine_examples", "Rpart_examples",
"Random_forest_examples", "Neural_net_examples", and "predsplot_examples".

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
