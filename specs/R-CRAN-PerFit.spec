%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  PerFit
%global packver   1.4.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.7
Release:          1%{?dist}%{?buildtag}
Summary:          Person Fit

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-ltm 
BuildRequires:    R-CRAN-mirt 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-fda 
BuildRequires:    R-CRAN-Hmisc 
BuildRequires:    R-CRAN-irtoys 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-Matrix 
Requires:         R-CRAN-ltm 
Requires:         R-CRAN-mirt 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-CRAN-fda 
Requires:         R-CRAN-Hmisc 
Requires:         R-CRAN-irtoys 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-Matrix 

%description
Several person-fit statistics (PFSs; Meijer and Sijtsma, 2001,
<doi:10.1177/01466210122031957>) are offered. These statistics allow
assessing whether individual response patterns to tests or questionnaires
are (im)plausible given the other respondents in the sample or given a
specified item response theory model. Some PFSs apply to dichotomous data,
such as the likelihood-based PFSs (lz, lz*) and the group-based PFSs
(personal biserial correlation, caution index, (normed) number of Guttman
errors, agreement/disagreement/dependability statistics, U3, ZU3, NCI,
Ht). PFSs suitable to polytomous data include extensions of lz, U3, and
(normed) number of Guttman errors.

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
