%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  gtWAS
%global packver   1.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.1
Release:          1%{?dist}%{?buildtag}
Summary:          Genome and Transcriptome Wide Association Study

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch

%description
Quantitative trait loci mapping and genome wide association analysis are
used to find candidate molecular marker or region associated with
phenotype based on linkage analysis and linkage disequilibrium. Gene
expression quantitative trait loci mapping is used to find candidate
molecular marker or region associated with gene expression. In this
package, we applied the method in Liu W. (2011)
<doi:10.1007/s00122-011-1631-7> and Gusev A. (2016) <doi:10.1038/ng.3506>
to genome and transcriptome wide association study, which is aimed at
revealing the association relationship between phenotype and molecular
markers, expression levels, molecular markers nested within different
related expression effect and expression effect nested within different
related molecular marker effect. F test based on full and reduced model
are performed to obtain p value or likelihood ratio statistic. The best
linear model can be obtained by stepwise regression analysis.

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
