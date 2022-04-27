%global __brp_check_rpaths %{nil}
%global packname  TripleR
%global packver   1.5.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.4
Release:          1%{?dist}%{?buildtag}
Summary:          Social Relation Model (SRM) Analyses for Single or Multiple Groups

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 >= 0.9.3
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-plyr 
Requires:         R-CRAN-ggplot2 >= 0.9.3
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-plyr 

%description
Social Relation Model (SRM) analyses for single or multiple round-robin
groups are performed. These analyses are either based on one manifest
variable, one latent construct measured by two manifest variables, two
manifest variables and their bivariate relations, or two latent constructs
each measured by two manifest variables. Within-group t-tests for variance
components and covariances are provided for single groups. For multiple
groups two types of significance tests are provided: between-groups
t-tests (as in SOREMO) and enhanced standard errors based on Lashley and
Bond (1997) <DOI:10.1037/1082-989X.2.3.278>. Handling for missing values
is provided.

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
