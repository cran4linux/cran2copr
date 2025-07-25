%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  synthpop
%global packver   1.9-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.9.2
Release:          1%{?dist}%{?buildtag}
Summary:          Generating Synthetic Versions of Sensitive Microdata for Statistical Disclosure Control

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-nnet 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-rpart 
BuildRequires:    R-CRAN-party 
BuildRequires:    R-CRAN-foreign 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-proto 
BuildRequires:    R-CRAN-polspline 
BuildRequires:    R-CRAN-randomForest 
BuildRequires:    R-CRAN-ranger 
BuildRequires:    R-CRAN-classInt 
BuildRequires:    R-CRAN-mipfp 
BuildRequires:    R-CRAN-survival 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-rmutil 
BuildRequires:    R-CRAN-broman 
BuildRequires:    R-CRAN-forcats 
Requires:         R-CRAN-lattice 
Requires:         R-CRAN-MASS 
Requires:         R-methods 
Requires:         R-CRAN-nnet 
Requires:         R-CRAN-ggplot2 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-rpart 
Requires:         R-CRAN-party 
Requires:         R-CRAN-foreign 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-proto 
Requires:         R-CRAN-polspline 
Requires:         R-CRAN-randomForest 
Requires:         R-CRAN-ranger 
Requires:         R-CRAN-classInt 
Requires:         R-CRAN-mipfp 
Requires:         R-CRAN-survival 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-rmutil 
Requires:         R-CRAN-broman 
Requires:         R-CRAN-forcats 

%description
A tool for producing synthetic versions of microdata containing
confidential information so that they are safe to be released to users for
exploratory analysis. The key objective of generating synthetic data is to
replace sensitive original values with synthetic ones causing minimal
distortion of the statistical information contained in the data set.
Variables, which can be categorical or continuous, are synthesised
one-by-one using sequential modelling. Replacements are generated by
drawing from conditional distributions fitted to the original data using
parametric or classification and regression trees models. Data are
synthesised via the function syn() which can be largely automated, if
default settings are used, or with methods defined by the user. Optional
parameters can be used to influence the disclosure risk and the analytical
quality of the synthesised data. For a description of the implemented
method see Nowok, Raab and Dibben (2016) <doi:10.18637/jss.v074.i11>.
Functions to assess identity and attribute disclosure for the original and
for the synthetic data are included in the package, and their use is
illustrated in a vignette on disclosure (Practical Privacy Metrics for
Synthetic Data).

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
