%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BLOQ
%global packver   0.1-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Methods to Impute and Analyze Data with BLOQ Observations

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-maxLik 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-maxLik 
Requires:         R-CRAN-mvtnorm 

%description
Provides methods for estimating the area under the concentration versus
time curve (AUC) and its standard error in the presence of Below the Limit
of Quantification (BLOQ) observations. Two approaches are implemented:
direct estimation using censored maximum likelihood, and a two-step
approach that first imputes BLOQ values using various methods and then
computes the AUC using the imputed data. Technical details are described
in Barnett et al. (2020), "Methods for Non-Compartmental Pharmacokinetic
Analysis With Observations Below the Limit of Quantification," Statistics
in Biopharmaceutical Research. <doi:10.1080/19466315.2019.1701546>.

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
