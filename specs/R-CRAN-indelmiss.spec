%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  indelmiss
%global packver   1.0.10
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.10
Release:          1%{?dist}%{?buildtag}
Summary:          Insertion Deletion Analysis While Accounting for Possible Missing Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-ape >= 3.2
BuildRequires:    R-CRAN-numDeriv >= 2012.9.1
BuildRequires:    R-CRAN-phangorn >= 1.99.13
BuildRequires:    R-CRAN-Rcpp >= 0.11.2
Requires:         R-CRAN-ape >= 3.2
Requires:         R-CRAN-numDeriv >= 2012.9.1
Requires:         R-CRAN-phangorn >= 1.99.13
Requires:         R-CRAN-Rcpp >= 0.11.2

%description
Genome-wide gene insertion and deletion rates can be modelled in a maximum
likelihood framework with the additional flexibility of modelling
potential missing data using the models included within. These models
simultaneously estimate insertion and deletion (indel) rates of gene
families and proportions of "missing" data for (multiple) taxa of
interest. The likelihood framework is utilized for parameter estimation. A
phylogenetic tree of the taxa and gene presence/absence patterns (with
data ordered by the tips of the tree) are required. See Dang et al. (2016)
<doi:10.1534/genetics.116.191973> for more details.

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
