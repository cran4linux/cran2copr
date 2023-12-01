%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  TaylorRussell
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          1%{?dist}%{?buildtag}
Summary:          A Taylor-Russell Function for Multiple Predictors

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5
Requires:         R-core >= 3.5
BuildArch:        noarch
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-shinyWidgets 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-shinyWidgets 

%description
The Taylor Russell model is a widely used method for assessing test
validity in personnel selections tasks. The three functions in this
package extend this model in a number of notable ways. TR() estimates test
validity for a single selection test via the original Taylor Russell
model. It extends this model by allowing users greater flexibility in
argument choice. For example, users can specify any three of the four
parameters (base rate, selection ratio, criterion validity, and positive
predictive value) of the Taylor Russell model and estimate the remaining
parameter (see the help file for examples).  The TaylorRussell() function
generalizes the original Taylor Russell model to allow for multiple
selection tests (predictors).  To our knowledge, this is the first
generalization of the Taylor Russell model to allow for three or more
selection tests (it is also the first to correctly handle models with two
selection tests). TRDemo() is a 'shiny' program for illustrating the
underlying logic of the Taylor Russell model. Taylor, HC and Russell, JT
(1939) "The relationship of validity coefficients to the practical
effectiveness of tests in selection: Discussion and tables"
<doi:10.1037/h0057079>.

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
