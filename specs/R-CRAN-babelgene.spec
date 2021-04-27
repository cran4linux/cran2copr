%global packname  babelgene
%global packver   21.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          21.4
Release:          1%{?dist}%{?buildtag}
Summary:          Gene Orthologs for Model Organisms in a Tidy Data Format

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.3
Requires:         R-core >= 3.3
BuildArch:        noarch
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-rlang 
Requires:         R-CRAN-dplyr 
Requires:         R-methods 
Requires:         R-CRAN-rlang 

%description
Genomic analysis of model organisms often requires the use of databases
based on human data or making comparisons to patient-derived resources.
This requires converting genes between human and non-human analogues. The
babelgene R package provides predicted gene orthologs/homologs for
frequently studied model organisms in an R-friendly tidy/long format. The
package integrates orthology assertion predictions sourced from multiple
databases as compiled by the HGNC Comparison of Orthology Predictions
(HCOP) (Wright et al. 2005 <doi:10.1007/s00335-005-0103-2>, Eyre et al.
2007 <doi:10.1093/bib/bbl030>, Seal et al. 2011 <doi:10.1093/nar/gkq892>).

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
