%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  nonmem2rx
%global packver   0.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          'nonmem2rx' Converts 'NONMEM' Models to 'rxode2'

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-rxode2 > 2.0.13
BuildRequires:    R-CRAN-checkmate 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-dparser 
BuildRequires:    R-CRAN-lotri 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-cli 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-qs 
BuildRequires:    R-CRAN-xml2 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-ggforce 
BuildRequires:    R-CRAN-crayon 
BuildRequires:    R-CRAN-rxode2parse 
Requires:         R-CRAN-rxode2 > 2.0.13
Requires:         R-CRAN-checkmate 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-dparser 
Requires:         R-CRAN-lotri 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-cli 
Requires:         R-tools 
Requires:         R-utils 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-qs 
Requires:         R-CRAN-xml2 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-ggforce 
Requires:         R-CRAN-crayon 

%description
'NONMEM' has been a tool for running nonlinear mixed effects models since
the 80s and is still used today (Bauer 2019 <doi:10.1002/psp4.12404>).
This tool allows you to convert 'NONMEM' models to 'rxode2' (Wang, Hallow
and James (2016) <doi:10.1002/psp4.12052>) and with simple models
'nlmixr2' syntax (Fidler et al (2019) <doi:10.1002/psp4.12445>). The
'nlmixr2' syntax requires the residual specification to be included and it
is not always translated. If available, the 'rxode2' model will read in
the 'NONMEM' data and compare the simulation for the population model
('PRED') individual model ('IPRED') and residual model ('IWRES') to
immediately show how well the translation is performing. This saves the
model development time for people who are creating an 'rxode2' model
manually.  Additionally, this package reads in all the information to
allow simulation with uncertainty (that is the number of observations, the
number of subjects, and the covariance matrix) with a 'rxode2' model.
This is complementary to the 'babelmixr2' package that translates
'nlmixr2' models to 'NONMEM' and can convert the objects converted from
'nonmem2rx' to a full 'nlmixr2' fit.

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
