%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  ThurMod
%global packver   1.1.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.11
Release:          1%{?dist}%{?buildtag}
Summary:          Thurstonian CFA and Thurstonian IRT Modeling

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-matrixStats 
BuildRequires:    R-CRAN-lavaan 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-matrixStats 
Requires:         R-CRAN-lavaan 

%description
Fit Thurstonian forced-choice models (CFA (simple and factor) and IRT) in
R. This package allows for the analysis of item response modeling (IRT) as
well as confirmatory factor analysis (CFA) in the Thurstonian framework.
Currently, estimation can be performed by 'Mplus' and 'lavaan'.
References: Brown & Maydeu-Olivares (2011) <doi:10.1177/0013164410375112>;
Jansen, M. T., & Schulze, R. (in review). The Thurstonian linked block
design: Improving Thurstonian modeling for paired comparison and ranking
data.; Maydeu-Olivares & Böckenholt (2005)
<doi:10.1037/1082-989X.10.3.285>.

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
