%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  iTOS
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          1%{?dist}%{?buildtag}
Summary:          Methods and Examples from Introduction to the Theory of Observational Studies

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-MASS 
BuildRequires:    R-CRAN-rcbalance 
BuildRequires:    R-CRAN-BiasedUrn 
BuildRequires:    R-CRAN-xtable 
Requires:         R-stats 
Requires:         R-CRAN-MASS 
Requires:         R-CRAN-rcbalance 
Requires:         R-CRAN-BiasedUrn 
Requires:         R-CRAN-xtable 

%description
Supplements for a book, "iTOS" = "Introduction to the Theory of
Observational Studies."  Data sets are 'aHDL' from Rosenbaum (2023a)
<doi:10.1111/biom.13558> and 'bingeM' from Rosenbaum (2023b)
<doi:10.1111/biom.13921>.  The function makematch() uses two-criteria
matching from Zhang et al. (2023) <doi:10.1080/01621459.2021.1981337> to
create the matched data 'bingeM' from 'binge'.  The makematch() function
also implements optimal matching (Rosenbaum (1989) <doi:10.2307/2290079>)
and matching with fine or near-fine balance (Rosenbaum et al. (2007)
<doi:10.1198/016214506000001059> and Yang et al (2012)
<doi:10.1111/j.1541-0420.2011.01691.x>).  The book makes use of two other
R packages, 'weightedRank' and 'tightenBlock'.

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
