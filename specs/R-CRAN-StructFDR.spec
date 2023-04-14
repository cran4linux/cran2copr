%global __brp_check_rpaths %{nil}
%global packname  StructFDR
%global packver   1.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3
Release:          3%{?dist}%{?buildtag}
Summary:          False Discovery Control Procedure Integrating the PriorStructure Information

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-nlme 
BuildRequires:    R-CRAN-ape 
BuildRequires:    R-cluster 
BuildRequires:    R-CRAN-dirmult 
BuildRequires:    R-CRAN-matrixStats 
Requires:         R-nlme 
Requires:         R-CRAN-ape 
Requires:         R-cluster 
Requires:         R-CRAN-dirmult 
Requires:         R-CRAN-matrixStats 

%description
Perform more powerful false discovery control (FDR) for microbiome data,
taking into account the prior phylogenetic relationship among bacteria
species.  As a general methodology, it is applicable to any type of
(genomic) data with prior structure information.

%prep
%setup -q -c -n %{packname}


%build

%install

mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}

test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%{rlibdir}/%{packname}
