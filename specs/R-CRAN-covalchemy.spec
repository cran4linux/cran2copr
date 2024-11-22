%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  covalchemy
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}%{?buildtag}
Summary:          Constructing Joint Distributions with Control Over Statistical Properties

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-interp 
BuildRequires:    R-CRAN-clue 
BuildRequires:    R-CRAN-ggExtra 
BuildRequires:    R-CRAN-gridExtra 
BuildRequires:    R-CRAN-DescTools 
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-interp 
Requires:         R-CRAN-clue 
Requires:         R-CRAN-ggExtra 
Requires:         R-CRAN-gridExtra 
Requires:         R-CRAN-DescTools 
Requires:         R-CRAN-MASS 

%description
Synthesizing joint distributions from marginal densities, focusing on
controlling key statistical properties such as correlation for continuous
data, mutual information for categorical data, and inducing Simpson's
Paradox. Generate datasets with specified correlation structures for
continuous variables, adjust mutual information between categorical
variables, and manipulate subgroup correlations to intentionally create
Simpson's Paradox. Joe (1997) <doi:10.1201/b13150> Sklar (1959)
<https://en.wikipedia.org/wiki/Sklar%%27s_theorem>.

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
