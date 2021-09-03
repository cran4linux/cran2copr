%global __brp_check_rpaths %{nil}
%global packname  asremlPlus
%global packver   4.3-19
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          4.3.19
Release:          1%{?dist}%{?buildtag}
Summary:          Augments 'ASReml-R' in Fitting Mixed Models and Packages Generally in Exploring Prediction Differences

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dae 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-reshape 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-sticky 
BuildRequires:    R-CRAN-RColorBrewer 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-doParallel 
Requires:         R-CRAN-dae 
Requires:         R-CRAN-ggplot2 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-utils 
Requires:         R-CRAN-reshape 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-sticky 
Requires:         R-CRAN-RColorBrewer 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-CRAN-foreach 
Requires:         R-parallel 
Requires:         R-CRAN-doParallel 

%description
Assists in automating the selection of terms to include in mixed models
when 'asreml' is used to fit the models. Also used to display, in tables
and graphs, predictions obtained using any model fitting function and to
explore differences between predictions. The content falls into the
following natural groupings: (i) Data, (ii) Object manipulation functions,
(iii) Model modification functions, (iv) Model testing functions, (v)
Model diagnostics functions, (vi) Prediction production and presentation
functions, (vii) Response transformation functions, and (viii)
Miscellaneous functions (for further details see 'asremlPlus-package' in
help). A history of the fitting of a sequence of models is kept in a data
frame. Procedures are available for choosing models that conform to the
hierarchy or marginality principle and for displaying predictions for
significant terms in tables and graphs. The 'asreml' package provides a
computationally efficient algorithm for fitting mixed models using
Residual Maximum Likelihood. It is a commercial package that can be
purchased from 'VSNi' <https://www.vsni.co.uk/> as 'asreml-R', who will
supply a zip file for local installation/updating (see
<https://asreml.kb.vsni.co.uk/>). It is not needed for functions that are
methods for 'alldiffs' and 'data.frame' objects. The package 'asremPlus'
can also be installed from <http://chris.brien.name/rpackages/>.

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
