%global packname  RichR
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Enrichment for Diseases in a Set of Genes

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-reshape2 
BuildRequires:    R-CRAN-magrittr 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-metap 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-reshape2 
Requires:         R-CRAN-magrittr 
Requires:         R-stats 
Requires:         R-CRAN-metap 

%description
It provides a list of genes associated to diseases (g2d$clean and
g2d$complete) based on the following 4 publications (GS2D, Fontaine (2016)
<doi:10.18547/gcb.2016.vol2.iss1.e33>, DisGeNET, Pinero (2016)
<doi:10.1093/nar/gkw943> Berto2016, Berto (2016)
<doi:10.3389/fgene.2016.00031> and PsyGeNET, Sacristan (2015)
<doi:10.1093/bioinformatics/btv301>). Those lists were combined and
manually curated to have matching disease names.  When provided a list of
gene names, it calculates the disease enrichment of the gene set. The
enrichment is calculated using proportion test and Fisher's exact test.
Adjusted fdr p-values are returned alongside with p-values combined using
the Fisher's method.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
