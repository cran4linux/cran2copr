%global __brp_check_rpaths %{nil}
%global packname  CeRNASeek
%global packver   2.1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.1.3
Release:          3%{?dist}%{?buildtag}
Summary:          Identification and Analysis of ceRNA Regulation

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-gtools 
BuildRequires:    R-CRAN-igraph 
BuildRequires:    R-survival 
BuildRequires:    R-parallel 
Requires:         R-CRAN-gtools 
Requires:         R-CRAN-igraph 
Requires:         R-survival 
Requires:         R-parallel 

%description
Provides several functions to identify and analyse miRNA sponge, including
popular methods for identifying miRNA sponge interactions, two types of
global ceRNA regulation prediction methods and four types of
context-specific prediction methods( Li Y et al.(2017)
<doi:10.1093/bib/bbx137>), which are based on miRNA-messenger RNA
regulation alone, or by integrating heterogeneous data, respectively. In
addition, For predictive ceRNA relationship pairs, this package provides
several downstream analysis algorithms, including regulatory network
analysis and functional annotation analysis, as well as survival prognosis
analysis based on expression of ceRNA ternary pair.

%prep
%setup -q -c -n %{packname}

find -type f -executable -exec grep -Iq . {} \; -exec sed -i -e '$a\' {} \;

%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
