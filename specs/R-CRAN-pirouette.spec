%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  pirouette
%global packver   1.6.5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.6.5
Release:          1%{?dist}%{?buildtag}
Summary:          Create a Bayesian Posterior from a Phylogeny

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-beautier >= 2.6.2
BuildRequires:    R-CRAN-mauricer >= 2.5
BuildRequires:    R-CRAN-beastier >= 2.4.6
BuildRequires:    R-CRAN-babette >= 2.1.1
BuildRequires:    R-CRAN-tracerer >= 2.0.2
BuildRequires:    R-CRAN-mcbette >= 1.7
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-CRAN-DDD 
BuildRequires:    R-CRAN-forcats 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-nodeSub 
BuildRequires:    R-CRAN-phangorn 
BuildRequires:    R-CRAN-phytools 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-pryr 
BuildRequires:    R-CRAN-readr 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-TESS 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-xtable 
Requires:         R-CRAN-beautier >= 2.6.2
Requires:         R-CRAN-mauricer >= 2.5
Requires:         R-CRAN-beastier >= 2.4.6
Requires:         R-CRAN-babette >= 2.1.1
Requires:         R-CRAN-tracerer >= 2.0.2
Requires:         R-CRAN-mcbette >= 1.7
Requires:         R-CRAN-ape 
Requires:         R-CRAN-DDD 
Requires:         R-CRAN-forcats 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-nodeSub 
Requires:         R-CRAN-phangorn 
Requires:         R-CRAN-phytools 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-pryr 
Requires:         R-CRAN-readr 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-TESS 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-xtable 

%description
Theoretical biologists are interested in measuring the extent at which we
can measure the truth. This package allows to create a Bayesian posterior
from a phylogeny that depicts the true evolutionary relationships. The
given and true phylogeny can than be compared to the posterior
phylogenies. Richèl J. C. Bilderbeek, Giovanni Laudanno, Rampal S. Etienne
(2020) "Quantifying the impact of an inference model in Bayesian
phylogenetics" <doi:10.1111/2041-210X.13514>.

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
