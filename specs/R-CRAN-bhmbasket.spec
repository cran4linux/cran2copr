%global __brp_check_rpaths %{nil}
%global packname  bhmbasket
%global packver   0.9.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9.4
Release:          1%{?dist}%{?buildtag}
Summary:          Bayesian Hierarchical Models for Basket Trials

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-R2jags >= 0.7.1
BuildRequires:    R-CRAN-foreach 
BuildRequires:    R-CRAN-doRNG 
Requires:         R-CRAN-R2jags >= 0.7.1
Requires:         R-CRAN-foreach 
Requires:         R-CRAN-doRNG 

%description
Provides functions for the evaluation of basket trial designs with binary
endpoints. Operating characteristics of a basket trial design are assessed
by simulating trial data according to scenarios, analyzing the data with
Bayesian hierarchical models (BHMs), and assessing decision probabilities
on stratum and trial-level based on Go / No-go decision making. The
package is build for high flexibility regarding decision rules, number of
interim analyses, number of strata, and recruitment. The BHMs proposed by
Berry et al. (2013) <doi:10.1177/1740774513497539> and Neuenschwander et
al. (2016) <doi:10.1002/pst.1730>, as well as a model that combines both
approaches are implemented. Functions are provided to implement Bayesian
decision rules as for example proposed by Fisch et al. (2015)
<doi:10.1177/2168479014533970>. In addition, posterior point estimates
(mean/median) and credible intervals for response rates and some model
parameters can be calculated. For simulated trial data, bias and mean
squared errors of posterior point estimates for response rates can be
provided.

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
