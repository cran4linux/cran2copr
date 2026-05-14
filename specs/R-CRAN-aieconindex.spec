%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  aieconindex
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}%{?buildtag}
Summary:          Access the 'Anthropic Economic Index' Dataset

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.1.0
Requires:         R-core >= 4.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-cli >= 3.6.0
BuildRequires:    R-CRAN-httr2 >= 1.0.0
BuildRequires:    R-CRAN-jsonlite 
BuildRequires:    R-stats 
BuildRequires:    R-tools 
BuildRequires:    R-utils 
Requires:         R-CRAN-cli >= 3.6.0
Requires:         R-CRAN-httr2 >= 1.0.0
Requires:         R-CRAN-jsonlite 
Requires:         R-stats 
Requires:         R-tools 
Requires:         R-utils 

%description
Provides clean, tidy access to the 'Anthropic Economic Index' (AEI)
dataset hosted on 'Hugging Face'
<https://huggingface.co/datasets/Anthropic/EconomicIndex>. The AEI is a
recurring release from 'Anthropic' that maps usage of the 'Claude' family
of large language models to occupations and tasks using the 'O*NET'
taxonomy and the 'Standard Occupational Classification' system, following
the methodology of Handa et al. (2025) <doi:10.48550/arXiv.2503.04761> and
the privacy-preserving system 'Clio' of Tamkin et al. (2024)
<doi:10.48550/arXiv.2412.13678>. Functions list available releases, fetch
raw and enriched usage tables, retrieve task statements, request
hierarchies, and country-level breakdowns, compare two releases, join the
index to user-supplied data on a shared key, and compute
usage-concentration metrics (Herfindahl-Hirschman Index, top-N
concentration ratios, Shannon entropy). Data is cached locally for
subsequent calls. Reproducibility helpers produce 'BibTeX' or plain-text
citations that include the methodological source paper. This product uses
the 'Anthropic Economic Index' data (released under CC-BY by 'Anthropic')
but is not endorsed or certified by 'Anthropic'.

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
