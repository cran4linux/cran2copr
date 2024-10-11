%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  fitODBOD
%global packver   1.5.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.3
Release:          1%{?dist}%{?buildtag}
Summary:          Modeling Over Dispersed Binomial Outcome Data Using BMD and ABD

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.0.0
Requires:         R-core >= 4.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-bbmle 
BuildRequires:    R-CRAN-hypergeo 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-Rdpack 
BuildRequires:    R-stats 
Requires:         R-CRAN-bbmle 
Requires:         R-CRAN-hypergeo 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-Rdpack 
Requires:         R-stats 

%description
Contains Probability Mass Functions, Cumulative Mass Functions, Negative
Log Likelihood value, parameter estimation and modeling data using
Binomial Mixture Distributions (BMD) (Manoj et al (2013)
<doi:10.5539/ijsp.v2n2p24>) and Alternate Binomial Distributions (ABD)
(Paul (1985) <doi:10.1080/03610928508828990>), also Journal article to use
the package(<doi:10.21105/joss.01505>).

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
