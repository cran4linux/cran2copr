%global __brp_check_rpaths %{nil}
%global packname  CRABS
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Congruent Rate Analyses in Birth-Death Scenarios

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-CRAN-deSolve 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-tibble 
BuildRequires:    R-CRAN-colorspace 
BuildRequires:    R-CRAN-patchwork 
BuildRequires:    R-CRAN-latex2exp 
BuildRequires:    R-CRAN-tidyr 
BuildRequires:    R-CRAN-pracma 
BuildRequires:    R-CRAN-ape 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-magrittr 
Requires:         R-CRAN-deSolve 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-tibble 
Requires:         R-CRAN-colorspace 
Requires:         R-CRAN-patchwork 
Requires:         R-CRAN-latex2exp 
Requires:         R-CRAN-tidyr 
Requires:         R-CRAN-pracma 
Requires:         R-CRAN-ape 

%description
Features tools for exploring congruent phylogenetic birth-death models. It
can construct the pulled speciation- and net-diversification rates from a
reference model. Given alternative speciation- or extinction rates, it can
construct new models that are congruent with the reference model.
Functionality is included to sample new rate functions, and to visualize
the distribution of one congruence class. See also Louca & Pennell (2020)
<doi:10.1038/s41586-020-2176-1>.

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
