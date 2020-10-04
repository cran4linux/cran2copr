%global packname  NBBttest
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          2%{?dist}%{?buildtag}
Summary:          Negative Binomial Beta t-Test

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
BuildRequires:    R-graphics 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-gplots 
Requires:         R-CRAN-gtools 
Requires:         R-stats 
Requires:         R-utils 
Requires:         R-graphics 
Requires:         R-grDevices 

%description
We constructed 'NBBttest' for identifying genes or RNA isoforms
differentially expressed between two conditions on RNA-seq count data.
Package 'NBBttest' can perform data quality check, data normalization,
differential analysis, annotation and graphic analysis. In differential
analysis, 'NBBttest' can identify differentially expressed genes and
differential RNA isoforms in alternative splicing sites and alternative
polyadenylation sites, differential sgRNA, and differential CRISPR
(clustered regularly interspaced short palindromic repeats) screening
genes. In graphic analysis, 'NBBttest' provides two types of heatmaps to
visualize differential expression at gene or isoform level using z-score
and n-score and creates pathway heatmap. 'NBBttest' can plot
differentially expressed exons within a specified gene. In addition,
'NBBttest' provides a tool for annotation of genes and exons. The methods
used in 'NBBttest' were new statistical methods developed from Tan and
others (2015) <doi:10.1371/journal.pone.0123658>. The statistical methods
are robust and very powerful in identifying genes or RNA isoforms
differentially expressed between two conditions in small samples.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;
[ -d %{packname}/src ] && find %{packname}/src -type f -exec \
  sed -i 's@/usr/bin/strip@/usr/bin/true@g' {} \; || true

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
find %{buildroot}%{rlibdir} -type f -exec sed -i "s@%{buildroot}@@g" {} \;

%files
%{rlibdir}/%{packname}
