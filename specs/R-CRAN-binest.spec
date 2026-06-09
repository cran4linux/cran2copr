%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  binest
%global packver   0.2-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Estimation of Group Means and SDs from Binned Count Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-splines 
BuildRequires:    R-stats 
Requires:         R-splines 
Requires:         R-stats 

%description
Estimates group-level means and standard deviations from binned
(coarsened) count data, where the within-bin scores are unobserved.  The
package implements three methods that share a common output structure:
bin_means() (a fast estimator that assumes within-district normality and
uses pooled bin proportions to derive bin-conditional truncated-normal
expectations), mle_hetop() (maximum likelihood for the heteroskedastic
ordered probit model of Reardon, Shear, Castellano and Ho 2017
<doi:10.3102/1076998616666279>), and fh_hetop() (the Bayesian Fay-Herriot
variant of Lockwood, Castellano and Shear 2018
<doi:10.3102/1076998618795124>).  The mle_hetop() and fh_hetop() functions
are forked from the 'HETOP' package by J. R. Lockwood ('CRAN', last
released 2019).  mle_hetop() has been modified to speed up the runtime via
a vectorized inner loop and to remove two user-facing arguments (fixedcuts
and svals) that some users found confusing; cutpoints and starting values
are now derived internally from the data.

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
