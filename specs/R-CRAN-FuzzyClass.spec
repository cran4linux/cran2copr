%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  FuzzyClass
%global packver   0.1.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.6
Release:          1%{?dist}%{?buildtag}
Summary:          Fuzzy and Non-Fuzzy Classifiers

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-caTools 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-EnvStats 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-rootSolve 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-trapezoid 
Requires:         R-CRAN-caTools 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-EnvStats 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-mvtnorm 
Requires:         R-parallel 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-rootSolve 
Requires:         R-stats 
Requires:         R-CRAN-trapezoid 

%description
It provides classifiers which can be used for discrete variables and for
continuous variables based on the Naive Bayes and Fuzzy Naive Bayes
hypothesis. Those methods were developed by researchers belong to the
'Laboratory of Technologies for Virtual Teaching and Statistics (LabTEVE)'
and 'Laboratory of Applied Statistics to Image Processing and
Geoprocessing (LEAPIG)' at 'Federal University of Paraiba, Brazil'. They
considered some statistical distributions and their papers were published
in the scientific literature, as for instance, the Gaussian classifier
using fuzzy parameters, proposed by 'Moraes, Ferreira and Machado' (2021)
<doi:10.1007/s40815-020-00936-4>.

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
