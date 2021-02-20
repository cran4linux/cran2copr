%global packname  CAST
%global packver   0.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          'caret' Applications for Spatial-Temporal Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-reshape 
BuildRequires:    R-CRAN-FNN 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-zoo 
BuildRequires:    R-methods 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-lattice 
Requires:         R-CRAN-caret 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-ggplot2 
Requires:         R-graphics 
Requires:         R-CRAN-reshape 
Requires:         R-CRAN-FNN 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-zoo 
Requires:         R-methods 
Requires:         R-grDevices 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-lattice 

%description
Supporting functionality to run 'caret' with spatial or spatial-temporal
data. 'caret' is a frequently used package for model training and
prediction using machine learning. This package includes functions to
improve spatial-temporal modelling tasks using 'caret'. It prepares data
for Leave-Location-Out and Leave-Time-Out cross-validation which are
target-oriented validation strategies for spatial-temporal models. To
decrease overfitting and improve model performances, the package
implements a forward feature selection that selects suitable predictor
variables in view to their contribution to the target-oriented
performance. CAST further includes functionality to estimate the (spatial)
area of applicability of prediction models by analysing the similarity
between new data and training data.

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
