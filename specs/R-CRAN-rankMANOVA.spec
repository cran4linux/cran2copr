%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  rankMANOVA
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Rank-Based Tests for Multivariate Data in Nonparametric Factorial Designs

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.5.0
Requires:         R-core >= 4.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS >= 7.3.43
BuildRequires:    R-parallel 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-multcomp 
Requires:         R-CRAN-MASS >= 7.3.43
Requires:         R-parallel 
Requires:         R-methods 
Requires:         R-CRAN-multcomp 

%description
Implemented are an ANOVA-type test statistic for testing hypotheses
formulated in Mann-Whitney-type effects in nonparametric factorial
designs. Statistical inference is based on a wild or a sample-specific
bootstrap approach as described in 'Dobler et al. (2019)
<doi:10.1007/s10463-019-00717-3>'. The unweighted treatment effects
considered do not depend on sample sizes and allow for transitive
ordering. The package thus provides an extension of the univariate
'rankFD' package to multivariate data.

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
