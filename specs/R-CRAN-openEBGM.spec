%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  openEBGM
%global packver   0.9.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.1
Release:          1%{?dist}%{?buildtag}
Summary:          EBGM Disproportionality Scores for Adverse Event Data Mining

License:          GPL-2 | GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildArch:        noarch
BuildRequires:    R-stats >= 3.2.3
BuildRequires:    R-CRAN-ggplot2 >= 2.2.1
BuildRequires:    R-CRAN-data.table >= 1.10.0
Requires:         R-stats >= 3.2.3
Requires:         R-CRAN-ggplot2 >= 2.2.1
Requires:         R-CRAN-data.table >= 1.10.0

%description
An implementation of DuMouchel's (1999)
<doi:10.1080/00031305.1999.10474456> Bayesian data mining method for the
market basket problem. Calculates Empirical Bayes Geometric Mean (EBGM)
and posterior quantile scores using the Gamma-Poisson Shrinker (GPS) model
to find unusually large cell counts in large, sparse contingency tables.
Can be used to find unusually high reporting rates of adverse events
associated with products. In general, can be used to mine any database
where the co-occurrence of two variables or items is of interest. Also
calculates relative and proportional reporting ratios. Builds on the work
of the 'PhViD' package, from which much of the code is derived. Some of
the added features include stratification to adjust for confounding
variables and data squashing to improve computational efficiency. Includes
an implementation of the EM algorithm for hyperparameter estimation
loosely derived from the 'mederrRank' package.

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
