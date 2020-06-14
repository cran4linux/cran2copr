%global packname  dlmap
%global packver   1.13
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.13
Release:          2%{?dist}
Summary:          Detection Localization Mapping for QTL

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-qtl 
BuildRequires:    R-CRAN-ibdreg 
BuildRequires:    R-CRAN-wgaim 
BuildRequires:    R-nlme 
BuildRequires:    R-mgcv 
Requires:         R-CRAN-qtl 
Requires:         R-CRAN-ibdreg 
Requires:         R-CRAN-wgaim 
Requires:         R-nlme 
Requires:         R-mgcv 

%description
QTL mapping in a mixed model framework with separate detection and
localization stages. The first stage detects the number of QTL on each
chromosome based on the genetic variation due to grouped markers on the
chromosome; the second stage uses this information to determine the most
likely QTL positions. The mixed model can accommodate general fixed and
random effects, including spatial effects in field trials and pedigree
effects. Applicable to backcrosses, doubled haploids, recombinant inbred
lines, F2 intercrosses, and association mapping populations.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
