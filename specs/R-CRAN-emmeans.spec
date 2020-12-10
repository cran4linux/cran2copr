%global packname  emmeans
%global packver   1.5.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.3
Release:          1%{?dist}%{?buildtag}
Summary:          Estimated Marginal Means, aka Least-Squares Means

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-xtable >= 1.8.2
BuildRequires:    R-CRAN-estimability >= 1.3
BuildRequires:    R-graphics 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-xtable >= 1.8.2
Requires:         R-CRAN-estimability >= 1.3
Requires:         R-graphics 
Requires:         R-methods 
Requires:         R-CRAN-numDeriv 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-mvtnorm 

%description
Obtain estimated marginal means (EMMs) for many linear, generalized
linear, and mixed models. Compute contrasts or linear functions of EMMs,
trends, and comparisons of slopes. Plots and other displays. Least-squares
means are discussed, and the term "estimated marginal means" is suggested,
in Searle, Speed, and Milliken (1980) Population marginal means in the
linear model: An alternative to least squares means, The American
Statistician 34(4), 216-221 <doi:10.1080/00031305.1980.10483031>.

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
