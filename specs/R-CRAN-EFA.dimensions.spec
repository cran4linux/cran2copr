%global __brp_check_rpaths %{nil}
%global packname  EFA.dimensions
%global packver   0.1.7.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.7.2
Release:          1%{?dist}%{?buildtag}
Summary:          Exploratory Factor Analysis Functions for Assessing Dimensionality

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-psych 
BuildRequires:    R-CRAN-polycor 
BuildRequires:    R-CRAN-EFAtools 
Requires:         R-stats 
Requires:         R-CRAN-psych 
Requires:         R-CRAN-polycor 
Requires:         R-CRAN-EFAtools 

%description
Functions for eleven procedures for determining the number of factors,
including functions for parallel analysis and the minimum average partial
test. There are functions for conducting principal components analysis,
principal axis factor analysis, maximum likelihood factor analysis, image
factor analysis, and extension factor analysis, all of which can take raw
data or correlation matrices as input and with options for conducting the
analyses using Pearson correlations, Kendall correlations, Spearman
correlations, gamma correlations, or polychoric correlations. Varimax
rotation, promax rotation, and Procrustes rotations can be performed.
Additional functions focus on the factorability of a correlation matrix,
the congruences between factors from different datasets, the assessment of
local independence, and the assessment of factor solution complexity.
O'Connor (2000, <doi:10.3758/bf03200807>); O'Connor (2001,
<doi:10.1177/01466216010251011>); Auerswald & Moshagen (2019,
<doi:10.1037/met0000200>); Fabrigar & Wegener (2012,
ISBN:978-0-19-973417-7); Field, Miles, & Field (2012,
ISBN:978-1-4462-0045-2).

%prep
%setup -q -c -n %{packname}

# fix end of executable files
find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
# prevent binary stripping
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true
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
