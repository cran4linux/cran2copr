%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  MARSGWR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          A Hybrid Spatial Model for Capturing Spatially Varying Relationships Between Variables in the Data

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-qpdf 
BuildRequires:    R-CRAN-numbers 
BuildRequires:    R-CRAN-earth 
Requires:         R-stats 
Requires:         R-CRAN-qpdf 
Requires:         R-CRAN-numbers 
Requires:         R-CRAN-earth 

%description
It is a hybrid spatial model that combines the strength of two widely used
regression models, MARS (Multivariate Adaptive Regression Splines) and GWR
(Geographically Weighted Regression) to provide an effective approach for
predicting a response variable at unknown locations. The MARS model is
used in the first step of the development of a hybrid model to identify
the most important predictor variables that assist in predicting the
response variable. For method details see, Friedman, J.H. (1991).
<DOI:10.1214/aos/1176347963>.The GWR model is then used to predict the
response variable at testing locations based on these selected variables
that account for spatial variations in the relationships between the
variables. This hybrid model can improve the accuracy of the predictions
compared to using an individual model alone.This developed hybrid spatial
model can be useful particularly in cases where the relationship between
the response variable and predictor variables is complex and non-linear,
and varies across locations.

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
