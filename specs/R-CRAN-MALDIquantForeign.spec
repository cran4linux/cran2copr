%global packname  MALDIquantForeign
%global packver   0.12
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.12
Release:          3%{?dist}
Summary:          Import/Export Routines for 'MALDIquant'

License:          GPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.2
Requires:         R-core >= 3.2.2
BuildArch:        noarch
BuildRequires:    R-CRAN-readMzXmlData >= 2.7
BuildRequires:    R-CRAN-readBrukerFlexData >= 1.7
BuildRequires:    R-CRAN-MALDIquant >= 1.16.4
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-base64enc 
BuildRequires:    R-CRAN-digest 
BuildRequires:    R-CRAN-XML 
Requires:         R-CRAN-readMzXmlData >= 2.7
Requires:         R-CRAN-readBrukerFlexData >= 1.7
Requires:         R-CRAN-MALDIquant >= 1.16.4
Requires:         R-methods 
Requires:         R-CRAN-base64enc 
Requires:         R-CRAN-digest 
Requires:         R-CRAN-XML 

%description
Functions for reading (tab, csv, Bruker fid, Ciphergen XML, mzXML, mzML,
imzML, Analyze 7.5, CDF, mMass MSD) and writing (tab, csv, mMass MSD,
mzML, imzML) different file formats of mass spectrometry data into/from
'MALDIquant' objects.

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
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/exampledata
%{rlibdir}/%{packname}/INDEX
