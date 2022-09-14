%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  semmcci
%global packver   1.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.1
Release:          1%{?dist}%{?buildtag}
Summary:          Monte Carlo Confidence Intervals in Structural Equation Modeling

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-lavaan 
BuildRequires:    R-methods 
Requires:         R-stats 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-lavaan 
Requires:         R-methods 

%description
Monte Carlo confidence intervals for free and defined parameters in models
fitted in the structural equation modeling package 'lavaan' can be
generated using the 'semmcci' package. 'semmcci' has two main functions,
namely, MC() and MCStd(). The output of 'lavaan' is passed as the first
argument to the MC() function to generate Monte Carlo confidence
intervals. Monte Carlo confidence intervals for the standardized estimates
can also be generated by passing the output of the MC() function to the
MCStd() function. Preacher and Selig (2012)
<doi:10.1080/19312458.2012.679848>.

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
