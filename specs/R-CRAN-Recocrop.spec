%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  Recocrop
%global packver   0.4-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.4.2
Release:          1%{?dist}%{?buildtag}
Summary:          Estimating Environmental Suitability for Plants

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-terra >= 1.8.5
BuildRequires:    R-methods >= 0.2.2
BuildRequires:    R-CRAN-Rcpp >= 0.12.4
BuildRequires:    R-CRAN-meteor 
Requires:         R-CRAN-terra >= 1.8.5
Requires:         R-methods >= 0.2.2
Requires:         R-CRAN-Rcpp >= 0.12.4
Requires:         R-CRAN-meteor 

%description
The ecocrop model estimates environmental suitability for plants using a
limiting factor approach for plant growth following Hackett (1991)
<doi:10.1007/BF00045728>. The implementation in this package is fast and
flexible: it allows for the use of any (environmental) predictor variable.
Predictors can be either static (for example, soil pH) or dynamic (for
example, monthly precipitation).

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
