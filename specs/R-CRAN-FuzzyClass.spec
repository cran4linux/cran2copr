%global __brp_check_rpaths %{nil}
%global packname  FuzzyClass
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Fuzzy and Non-Fuzzy Classifiers

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-caTools 
BuildRequires:    R-datasets 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-CRAN-e1071 
BuildRequires:    R-CRAN-EnvStats 
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-mlbench 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-CRAN-rootSolve 
BuildRequires:    R-CRAN-trapezoid 
Requires:         R-CRAN-caTools 
Requires:         R-datasets 
Requires:         R-CRAN-doParallel 
Requires:         R-CRAN-e1071 
Requires:         R-CRAN-EnvStats 
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-mlbench 
Requires:         R-parallel 
Requires:         R-CRAN-Rdpack 
Requires:         R-CRAN-rootSolve 
Requires:         R-CRAN-trapezoid 

%description
Provides classifiers that can be used for discrete variables and for
continuous variables based on the idea of Naive Bayes and Fuzzy Naive
Bayes considering some statistical distributions of articles published in
the literature developed in the LabTEVE and LEAPIG research laboratories.
Among the proposed classification methods is a with the Gamma
distribution, proposed by Moraes, Soares and Machado (2018)
<doi:10.1142/9789813273238_0088>.

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
