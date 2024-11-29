%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  monolix2rx
%global packver   0.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.4
Release:          1%{?dist}%{?buildtag}
Summary:          Converts 'Monolix' Models to 'rxode2'

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-rxode2 >= 3.0.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-CRAN-dparser 
BuildRequires:    R-CRAN-withr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggforce 
BuildRequires:    R-CRAN-stringi 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-lotri 
BuildRequires:    R-CRAN-magrittr 
Requires:         R-CRAN-rxode2 >= 3.0.0
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-cli 
Requires:         R-CRAN-dparser 
Requires:         R-CRAN-withr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggforce 
Requires:         R-CRAN-stringi 
Requires:         R-CRAN-crayon 
Requires:         R-CRAN-lotri 
Requires:         R-CRAN-magrittr 

%description
'Monolix' is a tool for running mixed effects model using 'saem'. This
tool allows you to convert 'Monolix' models to 'rxode2' (Wang, Hallow and
James (2016) <doi:10.1002/psp4.12052>) using the form compatible with
'nlmixr2' (Fidler et al (2019) <doi:10.1002/psp4.12445>). If available,
the 'rxode2' model will read in the 'Monolix' data and compare the
simulation for the population model individual model and residual model to
immediately show how well the translation is performing. This saves the
model development time for people who are creating an 'rxode2' model
manually.  Additionally, this package reads in all the information to
allow simulation with uncertainty (that is the number of observations, the
number of subjects, and the covariance matrix) with a 'rxode2' model.
This is complementary to the 'babelmixr2' package that translates
'nlmixr2' models to 'Monolix' and can convert the objects converted from
'monolix2rx' to a full 'nlmixr2' fit. While not required, you can
get/install the 'lixoftConnectors' package in the 'Monolix' installation,
as described at the following url
<https://monolixsuite.slp-software.com/r-functions/2024R1/installation-and-initialization>.
When 'lixoftConnectors' is available, 'Monolix' can be used to load its
model library instead manually setting up text files (which only works
with old versions of 'Monolix').

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
