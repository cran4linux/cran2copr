%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  phyloraster
%global packver   2.3.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.3.0
Release:          1%{?dist}%{?buildtag}
Summary:          Evolutionary Diversity Metrics for Raster Data

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-purrr 
BuildRequires:    R-CRAN-SESraster 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-terra 
Requires:         R-CRAN-ape 
Requires:         R-methods 
Requires:         R-CRAN-purrr 
Requires:         R-CRAN-SESraster 
Requires:         R-stats 
Requires:         R-CRAN-terra 

%description
Phylogenetic Diversity (PD, Faith 1992), Evolutionary Distinctiveness (ED,
Isaac et al. 2007), Phylogenetic Endemism (PE, Rosauer et al. 2009; Laffan
et al. 2016), and Weighted Endemism (WE, Laffan et al. 2016) for
presence-absence raster.  Faith, D. P. (1992)
<doi:10.1016/0006-3207(92)91201-3> Isaac, N. J. et al. (2007)
<doi:10.1371/journal.pone.0000296> Laffan, S. W. et al. (2016)
<doi:10.1111/2041-210X.12513> Rosauer, D. et al. (2009)
<doi:10.1111/j.1365-294X.2009.04311.x>.

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
