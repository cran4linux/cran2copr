%global __brp_check_rpaths %{nil}
%global packname  sigora
%global packver   3.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Signature Overrepresentation Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-slam 
Requires:         R-stats 
Requires:         R-CRAN-slam 

%description
Pathway Analysis is statistically linking observations on the molecular
level to biological processes or pathways on the systems(i.e., organism,
organ, tissue, cell) level. Traditionally, pathway analysis methods regard
pathways as collections of single genes and treat all genes in a pathway
as equally informative. However, this can lead to identifying spurious
pathways as statistically significant since components are often shared
amongst pathways. SIGORA seeks to avoid this pitfall by focusing on genes
or gene pairs that are (as a combination) specific to a single pathway. In
relying on such pathway gene-pair signatures (Pathway-GPS), SIGORA
inherently uses the status of other genes in the experimental context to
identify the most relevant pathways. The current version allows for
pathway analysis of human and mouse datasets. In addition, it contains
pre-computed Pathway-GPS data for pathways in the KEGG and Reactome
pathway repositories and mechanisms for extracting GPS for user-supplied
repositories.

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
