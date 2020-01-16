%global packname  lightr
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          1%{?dist}
Summary:          Read Spectrometric Data and Metadata

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-xml2 >= 1.0.0
BuildRequires:    R-CRAN-pbmcapply 
Requires:         R-CRAN-xml2 >= 1.0.0
Requires:         R-CRAN-pbmcapply 

%description
Parse various reflectance/transmittance/absorbance spectra file formats to
extract spectral data and metadata, as described in Gruson, White & Maia
(2019) <doi:10.21105/joss.01857>. This package has been peer-reviewed by
rOpenSci (v. 0.1).

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/lightr.bib
%{rlibdir}/%{packname}/testdata
%{rlibdir}/%{packname}/testdata_sources.txt
%doc %{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/INDEX
