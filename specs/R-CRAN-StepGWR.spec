%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  StepGWR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Hybrid Spatial Model for Prediction and Capturing Spatial Variation in the Data

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-qpdf 
BuildRequires:    R-CRAN-numbers 
BuildRequires:    R-CRAN-MASS 
Requires:         R-stats 
Requires:         R-CRAN-qpdf 
Requires:         R-CRAN-numbers 
Requires:         R-CRAN-MASS 

%description
It is a hybrid spatial model that combines the variable selection
capabilities of stepwise regression methods with the predictive power of
the Geographically Weighted Regression(GWR) model.The developed hybrid
model follows a two-step approach where the stepwise variable selection
method is applied first to identify the subset of predictors that have the
most significant impact on the response variable, and then a GWR model is
fitted using those selected variables for spatial prediction at test or
unknown locations. For method details,see Leung, Y., Mei, C. L. and Zhang,
W. X. (2000).<DOI:10.1068/a3162>.This hybrid spatial model aims to improve
the accuracy and interpretability of GWR predictions by selecting a subset
of relevant variables through a stepwise selection process.This approach
is particularly useful for modeling spatially varying relationships and
improving the accuracy of spatial predictions.

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
