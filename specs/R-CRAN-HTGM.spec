%global __brp_check_rpaths %{nil}
%global __requires_exclude ^libmpi
%global packname  HTGM
%global packver   1.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.2
Release:          1%{?dist}%{?buildtag}
Summary:          High Throughput 'GoMiner'

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 4.2.0
Requires:         R-core >= 4.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-minimalistGODB 
BuildRequires:    R-CRAN-GoMiner 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-gplots 
BuildRequires:    R-CRAN-vprint 
Requires:         R-CRAN-minimalistGODB 
Requires:         R-CRAN-GoMiner 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-CRAN-gplots 
Requires:         R-CRAN-vprint 

%description
Two papers published in the early 2000's (Zeeberg, B.R., Feng, W., Wang,
G. et al. (2003) <doi:10.1186/gb-2003-4-4-r28>) and (Zeeberg, B.R., Qin,
H., Narashimhan, S., et al. (2005) <doi:10.1186/1471-2105-6-168>)
implement 'GoMiner' and 'High Throughput GoMiner' ('HTGM') to map lists of
genes to the Gene Ontology (GO) <https://geneontology.org>. Until
recently, these were hosted on a server at The National Cancer Institute
(NCI). In order to continue providing these services to the bio-medical
community, I have developed stand-alone versions. The current package
'HTGM' builds upon my recent package 'GoMiner'. The output of 'GoMiner' is
a heatmap showing the relationship of a single list of genes and the
significant categories into which they map. 'High Throughput GoMiner'
('HTGM') integrates the results of the individual 'GoMiner' analyses. The
output of 'HTGM' is a heatmap showing the relationship of the significant
categories derived from each gene list. The heatmap has only 2 axes, so
the identity of the genes are unfortunately "integrated out of the
equation." Because the graphic for the heatmap is implemented in Scalable
Vector Graphics (SVG) technology, it is relatively easy to hyperlink each
picture element to the relevant list of genes. By clicking on the desired
picture element, the user can recover the "lost" genes.

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
