%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  mlr3viz
%global packver   0.5.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.10
Release:          1%{?dist}%{?buildtag}
Summary:          Visualizations for 'mlr3'

License:          LGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 3.3.0
BuildRequires:    R-CRAN-mlr3misc >= 0.7.0
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-viridis 
Requires:         R-CRAN-ggplot2 >= 3.3.0
Requires:         R-CRAN-mlr3misc >= 0.7.0
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-scales 
Requires:         R-utils 
Requires:         R-CRAN-viridis 

%description
Provides visualizations for 'mlr3' objects such as tasks, predictions,
resample results or benchmark results via the autoplot() generic of
'ggplot2'. The returned 'ggplot' objects are intended to provide sensible
defaults, yet can easily be customized to create camera-ready figures.
Visualizations include barplots, boxplots, histograms, ROC curves, and
Precision-Recall curves.

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
