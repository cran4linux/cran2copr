%global __brp_check_rpaths %{nil}
%global packname  WhatIf
%global packver   1.5-10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.10
Release:          1%{?dist}%{?buildtag}
Summary:          Software for Evaluating Counterfactuals

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.3.1
Requires:         R-core >= 2.3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-lpSolve 
BuildRequires:    R-CRAN-pbmcapply 
BuildRequires:    R-parallel 
Requires:         R-CRAN-lpSolve 
Requires:         R-CRAN-pbmcapply 
Requires:         R-parallel 

%description
Inferences about counterfactuals are essential for prediction, answering
what if questions, and estimating causal effects. However, when the
counterfactuals posed are too far from the data at hand, conclusions drawn
from well-specified statistical analyses become based largely on
speculation hidden in convenient modeling assumptions that few would be
willing to defend. Unfortunately, standard statistical approaches assume
the veracity of the model rather than revealing the degree of
model-dependence, which makes this problem hard to detect. WhatIf offers
easy-to-apply methods to evaluate counterfactuals that do not require
sensitivity testing over specified classes of models. If an analysis fails
the tests offered here, then we know that substantive inferences will be
sensitive to at least some modeling choices that are not based on
empirical evidence, no matter what method of inference one chooses to use.
WhatIf implements the methods for evaluating counterfactuals discussed in
Gary King and Langche Zeng, 2006, "The Dangers of Extreme
Counterfactuals," Political Analysis 14 (2) <DOI:10.1093/pan/mpj004>; and
Gary King and Langche Zeng, 2007, "When Can History Be Our Guide? The
Pitfalls of Counterfactual Inference," International Studies Quarterly 51
(March) <DOI:10.1111/j.1468-2478.2007.00445.x>.

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
