%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  asremlPlus
%global packver   4.4.51
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.4.51
Release:          1%{?dist}%{?buildtag}
Summary:          Augments 'ASReml-R' in Fitting Mixed Models and Packages Generally in Exploring Prediction Differences

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dae 
BuildRequires:    R-CRAN-devtools 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-nloptr 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-qqplotr 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-rlang 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-sticky 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-tryCatchLog 
BuildRequires:    R-utils 
Requires:         R-CRAN-dae 
Requires:         R-CRAN-devtools 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-ggplot2 
Requires:         R-graphics 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-CRAN-nloptr 
Requires:         R-parallel 
Requires:         R-CRAN-qqplotr 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-rlang 
Requires:         R-stats 
Requires:         R-CRAN-sticky 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-tryCatchLog 
Requires:         R-utils 

%description
Assists in automating the selection of terms to include in mixed models
when 'asreml' is used to fit the models. Procedures are available for
choosing models that conform to the hierarchy or marginality principle,
for fitting and choosing between two-dimensional spatial models using
correlation, natural cubic smoothing spline and P-spline models. A history
of the fitting of a sequence of models is kept in a data frame. Also used
to compute functions and contrasts of, to investigate differences between
and to plot predictions obtained using any model fitting function. The
content falls into the following natural groupings: (i) Data, (ii) Model
modification functions, (iii) Model selection and description functions,
(iv) Model diagnostics and simulation functions, (v) Prediction production
and presentation functions, (vi) Response transformation functions, (vii)
Object manipulation functions, and (viii) Miscellaneous functions (for
further details see 'asremlPlus-package' in help). The 'asreml' package
provides a computationally efficient algorithm for fitting a wide range of
linear mixed models using Residual Maximum Likelihood. It is a commercial
package and a license for it can be purchased from 'VSNi'
<https://vsni.co.uk/> as 'asreml-R', who will supply a zip file for local
installation/updating (see <https://asreml.kb.vsni.co.uk/>). It is not
needed for functions that are methods for 'alldiffs' and 'data.frame'
objects. The package 'asremPlus' can also be installed from
<http://chris.brien.name/rpackages/>.

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
