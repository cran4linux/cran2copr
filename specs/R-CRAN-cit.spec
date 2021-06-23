%global __brp_check_rpaths %{nil}
%global packname  cit
%global packver   2.3.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.1
Release:          1%{?dist}%{?buildtag}
Summary:          Causal Inference Test

License:          Artistic-2.0
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    gsl-devel
BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0

%description
A likelihood-based hypothesis testing approach is implemented for
assessing causal mediation. Described in Millstein, Chen, and Breton
(2016), <DOI:10.1093/bioinformatics/btw135>, it could be used to test for
mediation of a known causal association between a DNA variant, the
'instrumental variable', and a clinical outcome or phenotype by gene
expression or DNA methylation, the potential mediator. Another example
would be testing mediation of the effect of a drug on a clinical outcome
by the molecular target. The hypothesis test generates a p-value or
permutation-based FDR value with confidence intervals to quantify
uncertainty in the causal inference. The outcome can be represented by
either a continuous or binary variable, the potential mediator is
continuous, and the instrumental variable can be continuous or binary and
is not limited to a single variable but may be a design matrix
representing multiple variables.

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
