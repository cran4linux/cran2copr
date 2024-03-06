%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  BElikelihood
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Likelihood Method for Evaluating Bioequivalence

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-mvtnorm 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-mvtnorm 

%description
A likelihood method is implemented to present evidence for evaluating
bioequivalence (BE). The functions use bioequivalence data [area under the
blood concentration-time curve (AUC) and peak concentration (Cmax)] from
various crossover designs commonly used in BE studies including a fully
replicated, a partially replicated design, and a conventional 2x2
crossover design. They will calculate the profile likelihoods for the mean
difference, total standard deviation ratio, and within subject standard
deviation ratio for a test and a reference drug. A plot of a standardized
profile likelihood can be generated along with the maximum likelihood
estimate and likelihood intervals, which present evidence for
bioequivalence. See Liping Du and Leena Choi (2015)
<doi:10.1002/pst.1661>.

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
