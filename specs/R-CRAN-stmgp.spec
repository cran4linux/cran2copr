%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  stmgp
%global packver   1.0.4.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4.1
Release:          1%{?dist}%{?buildtag}
Summary:          Rapid and Accurate Genetic Prediction Modeling for Genome-Wide Association or Whole-Genome Sequencing Study Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-MASS 

%description
Rapidly build accurate genetic prediction models for genome-wide
association or whole-genome sequencing study data by smooth-threshold
multivariate genetic prediction (STMGP) method. Variable selection is
performed using marginal association test p-values with an optimal p-value
cutoff selected by Cp-type criterion. Quantitative and binary traits are
modeled respectively via linear and logistic regression models. A function
that works through PLINK software (Purcell et al. 2007
<DOI:10.1086/519795>, Chang et al. 2015 <DOI:10.1186/s13742-015-0047-8>)
<https://www.cog-genomics.org/plink2> is provided. Covariates can be
included in regression model.

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
