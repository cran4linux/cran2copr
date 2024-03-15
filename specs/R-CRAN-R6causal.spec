%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  R6causal
%global packver   0.8.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.8.3
Release:          1%{?dist}%{?buildtag}
Summary:          R6 Class for Structural Causal Models

License:          AGPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-causaleffect 
BuildRequires:    R-CRAN-cfid 
BuildRequires:    R-CRAN-data.table 
BuildRequires:    R-CRAN-dosearch 
BuildRequires:    R-CRAN-glue 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-MASS 
Requires:         R-CRAN-causaleffect 
Requires:         R-CRAN-cfid 
Requires:         R-CRAN-data.table 
Requires:         R-CRAN-dosearch 
Requires:         R-CRAN-glue 
Requires:         R-CRAN-igraph 
Requires:         R-CRAN-R6 
Requires:         R-stats 
Requires:         R-CRAN-MASS 

%description
The implemented R6 class 'SCM' aims to simplify working with structural
causal models. The missing data mechanism can be defined as a part of the
structural model. The class contains methods for 1) defining a structural
causal model via functions, text or conditional probability tables, 2)
printing basic information on the model, 3) plotting the graph for the
model using packages 'igraph' or 'qgraph', 4) simulating data from the
model, 5) applying an intervention, 6) checking the identifiability of a
query using the R packages 'causaleffect' and 'dosearch', 7) defining the
missing data mechanism, 8) simulating incomplete data from the model
according to the specified missing data mechanism and 9) checking the
identifiability in a missing data problem using the R package 'dosearch'.
In addition, there are functions for running experiments and doing
counterfactual inference using simulation.

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
