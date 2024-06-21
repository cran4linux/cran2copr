%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BANAM
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Analysis of the Network Autocorrelation Model

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-CRAN-BFpack 
BuildRequires:    R-CRAN-Matrix 
BuildRequires:    R-CRAN-extraDistr 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-mvtnorm 
BuildRequires:    R-CRAN-rARPACK 
BuildRequires:    R-CRAN-tmvtnorm 
BuildRequires:    R-utils 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-sna 
BuildRequires:    R-CRAN-bain 
Requires:         R-CRAN-BFpack 
Requires:         R-CRAN-Matrix 
Requires:         R-CRAN-extraDistr 
Requires:         R-CRAN-matrixcalc 
Requires:         R-CRAN-mvtnorm 
Requires:         R-CRAN-rARPACK 
Requires:         R-CRAN-tmvtnorm 
Requires:         R-utils 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-sna 
Requires:         R-CRAN-bain 

%description
The network autocorrelation model (NAM) can be used for studying the
degree of social influence regarding an outcome variable based on one or
more known networks. The degree of social influence is quantified via the
network autocorrelation parameters. In case of a single network, the
Bayesian methods of Dittrich, Leenders, and Mulder (2017)
<DOI:10.1016/j.socnet.2016.09.002> and Dittrich, Leenders, and Mulder
(2019) <DOI:10.1177/0049124117729712> are implemented using a normal,
flat, or independence Jeffreys prior for the network autocorrelation. In
the case of multiple networks, the Bayesian methods of Dittrich, Leenders,
and Mulder (2020) <DOI:10.1177/0081175020913899> are implemented using a
multivariate normal prior for the network autocorrelation parameters. Flat
priors are implemented for estimating the coefficients. For Bayesian
testing of equality and order-constrained hypotheses, the default Bayes
factor of Gu, Mulder, and Hoijtink, (2018) <DOI:10.1111/bmsp.12110> is
used with the posterior mean and posterior covariance matrix of the NAM
parameters based on flat priors as input.

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
