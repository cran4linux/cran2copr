%global __brp_check_rpaths %{nil}
%global packname  LncPath
%global packver   1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Identifying the Pathways Regulated by LncRNA Sets of Interest

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.1
Requires:         R-core >= 3.2.1
BuildArch:        noarch
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-stats 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
Requires:         R-CRAN-igraph 
Requires:         R-stats 
Requires:         R-graphics 
Requires:         R-utils 
Requires:         R-grDevices 

%description
Identifies pathways synergisticly regulated by the interested lncRNA(long
non-coding RNA) sets based on a lncRNA-mRNA(messenger RNA) interaction
network. 1) The lncRNA-mRNA interaction network was built from the
protein-protein interactions and the lncRNA-mRNA co-expression
relationships in 28 RNA-Seq data sets. 2) The interested lncRNAs can be
mapped into networks as seed nodes and a random walk strategy will be
performed to evaluate the rate of each coding genes influenced by the seed
lncRNAs. 3) Pathways regulated by the lncRNA set will be evaluated by a
weighted Kolmogorov-Smirnov statistic as an ES Score. 4) The p value and
false discovery rate value will also be calculated through a permutation
analysis. 5) The running score of each pathway can be plotted and the heat
map of each pathway can also be plotted if an expression profile is
provided. 6) The rank and scores of the gene list of each pathway can be
printed.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
