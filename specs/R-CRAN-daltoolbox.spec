%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  daltoolbox
%global packver   1.0.707
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.707
Release:          1%{?dist}%{?buildtag}
Summary:          Leveraging Experiment Lines to Data Analytics

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-MLmetrics 
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-class 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-dbscan 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-elmNNRcpp 
BuildRequires:    R-CRAN-forecast 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-reshape 
BuildRequires:    R-CRAN-tree 
BuildRequires:    R-CRAN-reticulate 
Requires:         R-CRAN-FNN 
Requires:         R-CRAN-MLmetrics 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-class 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-dbscan 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-elmNNRcpp 
Requires:         R-CRAN-forecast 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-reshape 
Requires:         R-CRAN-tree 
Requires:         R-CRAN-reticulate 

%description
The natural increase in the complexity of current research experiments and
data demands better tools to enhance productivity in Data Analytics. The
package is a framework designed to address the modern challenges in data
analytics workflows. The package is inspired by Experiment Line concepts.
It aims to provide seamless support for users in developing their data
mining workflows by offering a uniform data model and method API. It
enables the integration of various data mining activities, including data
preprocessing, classification, regression, clustering, and time series
prediction. It also offers options for hyper-parameter tuning and supports
integration with existing libraries and languages. Overall, the package
provides researchers with a comprehensive set of functionalities for data
science, promoting ease of use, extensibility, and integration with
various tools and libraries. Information on Experiment Line is based on
Ogasawara et al. (2009) <doi:10.1007/978-3-642-02279-1_20>.

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
