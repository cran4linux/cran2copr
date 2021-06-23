%global __brp_check_rpaths %{nil}
%global packname  lmem.qtler
%global packver   0.1.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.1
Release:          3%{?dist}%{?buildtag}
Summary:          Linear Mixed Effects Models for QTL Mapping for Multienvironmentand Multitrait Analysis

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-qtl 
BuildRequires:    R-CRAN-lme4 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-pastecs 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-graphics 
BuildRequires:    R-utils 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
Requires:         R-CRAN-qtl 
Requires:         R-CRAN-lme4 
Requires:         R-lattice 
Requires:         R-CRAN-pastecs 
Requires:         R-CRAN-stringr 
Requires:         R-graphics 
Requires:         R-utils 
Requires:         R-grDevices 
Requires:         R-stats 

%description
Performs QTL mapping analysis for balanced and for multi-environment and
multi-trait analysis using mixed models. Balanced population, single
trait, single environment QTL mapping is performed through
marker-regression (Haley and Knott (1992) <DOI:10.1038/hdy.1992.131>,
Martinez and Curnow (1992) <DOI:10.1007/BF00222330>, while
multi-environment and multi-trait QTL mapping is performed through linear
mixed models. These functions could use any of the following populations:
double haploid, F2, recombinant inbred lines, back-cross, and 4-way
crosses. Performs a Single Marker Analysis, a Single Interval Mapping, or
a Composite Interval Mapping analysis, and then constructs a final model
with all of the relevant QTL.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
