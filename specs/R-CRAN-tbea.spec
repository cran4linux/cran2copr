%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  tbea
%global packver   1.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.0
Release:          1%{?dist}%{?buildtag}
Summary:          Pre- And Post-Processing in Bayesian Evolutionary Analyses

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-Rfit 
BuildRequires:    R-CRAN-boot 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-coda 
Requires:         R-CRAN-ape 
Requires:         R-CRAN-Rfit 
Requires:         R-CRAN-boot 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-CRAN-coda 

%description
Functions are provided for prior specification in divergence time
estimation using fossils as well as other kinds of data. It provides tools
for interacting with the input and output of Bayesian platforms in
evolutionary biology such as 'BEAST2', 'MrBayes', 'RevBayes', or
'MCMCTree'. It Implements a simple measure similarity between probability
density functions for comparing prior and posterior Bayesian densities, as
well as code for calculating the combination of distributions using
conflation of Hill (2008). Functions for estimating the origination time
in collections of distributions using the x-intercept (e.g., Draper and
Smith, 1998) and stratigraphic intervals (Marshall 2010) are also
available. Hill, T. 2008. "Conflations of probability distributions".
Transactions of the American Mathematical Society, 363:3351-3372.
<doi:10.48550/arXiv.0808.1808>, Draper, N. R. and Smith, H. 1998. "Applied
Regression Analysis". 1--706. Wiley Interscience, New York.
<DOI:10.1002/9781118625590>, Marshall, C. R. 2010. "Using confidence
intervals to quantify the uncertainty in the end-points of stratigraphic
ranges". Quantitative Methods in Paleobiology, 291--316.
<DOI:10.1017/S1089332600001911>.

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
