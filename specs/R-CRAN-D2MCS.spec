%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  D2MCS
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Data Driving Multiple Classifier System

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2
Requires:         R-core >= 4.2
BuildArch:        noarch
BuildRequires:    R-CRAN-caret 
BuildRequires:    R-CRAN-devtools 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-FSelector 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggrepel 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-infotheo 
BuildRequires:    R-CRAN-mccr 
BuildRequires:    R-CRAN-mltools 
BuildRequires:    R-CRAN-ModelMetrics 
BuildRequires:    R-CRAN-questionr 
BuildRequires:    R-CRAN-recipes 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-tictoc 
BuildRequires:    R-CRAN-varhandle 
Requires:         R-CRAN-caret 
Requires:         R-CRAN-devtools 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-FSelector 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggrepel 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-infotheo 
Requires:         R-CRAN-mccr 
Requires:         R-CRAN-mltools 
Requires:         R-CRAN-ModelMetrics 
Requires:         R-CRAN-questionr 
Requires:         R-CRAN-recipes 
Requires:         R-CRAN-R6 
Requires:         R-CRAN-tictoc 
Requires:         R-CRAN-varhandle 

%description
Provides a novel framework to able to automatically develop and deploy an
accurate Multiple Classifier System based on the feature-clustering
distribution achieved from an input dataset. 'D2MCS' was developed focused
on four main aspects: (i) the ability to determine an effective method to
evaluate the independence of features, (ii) the identification of the
optimal number of feature clusters, (iii) the training and tuning of ML
models and (iv) the execution of voting schemes to combine the outputs of
each classifier comprising the Multiple Classifier System.

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
