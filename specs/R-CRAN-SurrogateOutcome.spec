%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  SurrogateOutcome
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          1%{?dist}%{?buildtag}
Summary:          Estimation of the Proportion of Treatment Effect Explained by Surrogate Outcome Information

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-survival 
Requires:         R-stats 
Requires:         R-CRAN-survival 

%description
Estimates the proportion of treatment effect on a censored primary outcome
that is explained by the treatment effect on a censored surrogate
outcome/event. All methods are described in detail in Parast, et al (2020)
"Assessing the Value of a Censored Surrogate Outcome"
<doi:10.1007/s10985-019-09473-1> and Wang et al (2025) "Model-free
Approach to Evaluate a Censored Intermediate Outcome as a Surrogate for
Overall Survival" <doi:10.1002/sim.70268>.  A tutorial for this package
can be found at <https://www.laylaparast.com/surrogateoutcome>.

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
