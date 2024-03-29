%global __brp_check_rpaths %{nil}
%global packname  WGScan
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          3%{?dist}%{?buildtag}
Summary:          A Genome-Wide Scan Statistic Framework for Whole-Genome SequenceData Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10.0
Requires:         R-core >= 2.10.0
BuildArch:        noarch
BuildRequires:    R-CRAN-SKAT 
BuildRequires:    R-Matrix 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-seqminer 
BuildRequires:    R-CRAN-data.table 
Requires:         R-CRAN-SKAT 
Requires:         R-Matrix 
Requires:         R-MASS 
Requires:         R-CRAN-seqminer 
Requires:         R-CRAN-data.table 

%description
Functions for the analysis of whole-genome sequencing studies to
simultaneously detect the existence, and estimate the locations of
association signals at genome-wide scale. The functions allow genome-wide
association scan, candidate region scan and single window test.

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
