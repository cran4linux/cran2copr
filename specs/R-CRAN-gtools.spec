%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gtools
%global packver   3.9.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.9.5
Release:          1%{?dist}%{?buildtag}
Summary:          Various R Programming Tools

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-methods 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-methods 
Requires:         R-stats 
Requires:         R-utils 

%description
Functions to assist in R programming, including: - assist in developing,
updating, and maintaining R and R packages ('ask', 'checkRVersion',
'getDependencies', 'keywords', 'scat'), - calculate the logit and inverse
logit transformations ('logit', 'inv.logit'), - test if a value is
missing, empty or contains only NA and NULL values ('invalid'), -
manipulate R's .Last function ('addLast'), - define macros ('defmacro'), -
detect odd and even integers ('odd', 'even'), - convert strings containing
non-ASCII characters (like single quotes) to plain ASCII ('ASCIIfy'), -
perform a binary search ('binsearch'), - sort strings containing both
numeric and character components ('mixedsort'), - create a factor variable
from the quantiles of a continuous variable ('quantcut'), - enumerate
permutations and combinations ('combinations', 'permutation'), - calculate
and convert between fold-change and log-ratio ('foldchange',
'logratio2foldchange', 'foldchange2logratio'), - calculate probabilities
and generate random numbers from Dirichlet distributions ('rdirichlet',
'ddirichlet'), - apply a function over adjacent subsets of a vector
('running'), - modify the TCP_NODELAY ('de-Nagle') flag for socket
objects, - efficient 'rbind' of data frames, even if the column names
don't match ('smartbind'), - generate significance stars from p-values
('stars.pval'), - convert characters to/from ASCII codes ('asc', 'chr'), -
convert character vector to ASCII representation ('ASCIIfy'), - apply
title capitalization rules to a character vector ('capwords').

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
