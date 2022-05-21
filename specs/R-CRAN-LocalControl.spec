%global __brp_check_rpaths %{nil}
%global packname  LocalControl
%global packver   1.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.3
Release:          1%{?dist}%{?buildtag}
Summary:          Nonparametric Methods for Generating High Quality Comparative Effectiveness Evidence

License:          Apache License 2.0 | file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-gss 
BuildRequires:    R-CRAN-cluster 
BuildRequires:    R-CRAN-lattice 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-gss 
Requires:         R-CRAN-cluster 
Requires:         R-CRAN-lattice 
Requires:         R-stats 
Requires:         R-graphics 

%description
Implements novel nonparametric approaches to address biases and
confounding when comparing treatments or exposures in observational
studies of outcomes. While designed and appropriate for use in studies
involving medicine and the life sciences, the package can be used in other
situations involving outcomes with multiple confounders. The package
implements a family of methods for non-parametric bias correction when
comparing treatments in observational studies, including survival analysis
settings, where competing risks and/or censoring may be present. The
approach extends to bias-corrected personalized predictions of treatment
outcome differences, and analysis of heterogeneity of treatment
effect-sizes across patient subgroups. For further details, please see:
Lauve NR, Nelson SJ, Young SS, Obenchain RL, Lambert CG. LocalControl: An
R Package for Comparative Safety and Effectiveness Research. Journal of
Statistical Software. 2020. p. 1–32. Available from
<doi:10.18637/jss.v096.i04>.

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
