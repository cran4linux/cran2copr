%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  surveySimR
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Estimation of Population Total under Complex Sampling Design

License:          GPL (>= 2.0)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-CRAN-moments 
BuildRequires:    R-stats 
Requires:         R-CRAN-shiny 
Requires:         R-CRAN-moments 
Requires:         R-stats 

%description
Sample surveys use scientific methods to draw inferences about population
parameters by observing a representative part of the population, called
sample. The SRSWOR (Simple Random Sampling Without Replacement) is one of
the most widely used probability sampling designs, wherein every unit has
an equal chance of being selected and units are not repeated.This function
draws multiple SRSWOR samples from a finite population and estimates the
population parameter i.e. total of HT, Ratio, and Regression estimators.
Repeated simulations (e.g., 500 times) are used to assess and compare
estimators using metrics such as percent relative bias (%%RB), percent
relative root means square error (%%RRMSE).For details on sampling
methodology, see, Cochran (1977) "Sampling Techniques"
<https://archive.org/details/samplingtechniqu0000coch_t4x6>.

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
