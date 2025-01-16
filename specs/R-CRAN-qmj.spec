%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  qmj
%global packver   0.2.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          1%{?dist}%{?buildtag}
Summary:          Quality Scores for the Russell 3000

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-quantmod >= 0.4.3
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-reticulate 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-quantmod >= 0.4.3
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-reticulate 
Requires:         R-CRAN-rlang 

%description
Produces quality scores for each of the US companies from the Russell
3000, following the approach described in "Quality Minus Junk" (Asness,
Frazzini, & Pedersen, 2013)
<http://www.aqr.com/library/working-papers/quality-minus-junk>. The
package includes datasets for users who wish to view the most recently
uploaded quality scores. It also provides tools to automatically gather
relevant financials and stock price information, allowing users to update
their data and customize their universe for further analysis.

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
