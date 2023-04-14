%global __brp_check_rpaths %{nil}
%global packname  ComICS
%global packver   1.0.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.4
Release:          3%{?dist}%{?buildtag}
Summary:          Computational Methods for Immune Cell-Type Subsets

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.1
Requires:         R-core >= 3.1.1
BuildArch:        noarch
BuildRequires:    R-CRAN-glmnet 
BuildRequires:    R-stats 
Requires:         R-CRAN-glmnet 
Requires:         R-stats 

%description
Provided are Computational methods for Immune Cell-type Subsets,
including:(1) DCQ (Digital Cell Quantifier) to infer global dynamic
changes in immune cell quantities within a complex tissue; and (2) VoCAL
(Variation of Cell-type Abundance Loci) a deconvolution-based method that
utilizes transcriptome data to infer the quantities of immune-cell types,
and then uses these quantitative traits to uncover the underlying DNA
loci.

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
