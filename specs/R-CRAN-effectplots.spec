%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  effectplots
%global packver   0.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.2
Release:          1%{?dist}%{?buildtag}
Summary:          Effect Plots

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildRequires:    R-CRAN-collapse 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-grDevices 
BuildRequires:    R-CRAN-labeling 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-plotly 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-scales 
BuildRequires:    R-stats 
Requires:         R-CRAN-collapse 
Requires:         R-CRAN-ggplot2 
Requires:         R-grDevices 
Requires:         R-CRAN-labeling 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-plotly 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-scales 
Requires:         R-stats 

%description
High-performance implementation of various effect plots useful for
regression and probabilistic classification tasks.  The package includes
partial dependence plots (Friedman, 2021, <doi:10.1214/aos/1013203451>),
accumulated local effect plots and M-plots (both from Apley and Zhu, 2016,
<doi:10.1111/rssb.12377>), as well as plots that describe the statistical
associations between model response and features.  It supports
visualizations with either 'ggplot2' or 'plotly', and is compatible with
most models, including 'Tidymodels', models wrapped in 'DALEX' explainers,
or models with case weights.

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
