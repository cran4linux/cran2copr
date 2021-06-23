%global __brp_check_rpaths %{nil}
%global packname  MGMS2
%global packver   1.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.2
Release:          3%{?dist}%{?buildtag}
Summary:          'MGMS2' for Polymicrobial Samples

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-MALDIquant 
BuildRequires:    R-CRAN-MALDIquantForeign 
Requires:         R-CRAN-MALDIquant 
Requires:         R-CRAN-MALDIquantForeign 

%description
A glycolipid mass spectrometry technology has the potential to accurately
identify individual bacterial species from polymicrobial samples. To
develop bacterial identification algorithms (e.g. machine learning) using
this glycolipid technology, it is necessary to generate a large number of
various in-silico polymicrobial mass spectra that are similar to real mass
spectra. 'MGMS2' (Membrane Glycolipid Mass Spectrum Simulator) generates
such in-silico mass spectra, considering errors in m/z (mass-to-charge
ratio) and variances of intensity values, occasions of missing signature
ions, and noise peaks. It estimates summary statistics of monomicrobial
mass spectra for each strain or species and simulates polymicrobial
glycolipid mass spectra using the summary statistics of monomicrobial mass
spectra. References: Ryu, S.Y., Wendt, G.A., Chandler, C.E., Ernst, R.K.
and Goodlett, D.R. (2019) <doi:10.1021/acs.analchem.9b03340> "Model-based
Spectral Library Approach for Bacterial Identification via Membrane
Glycolipids." Gibb, S. and Strimmer, K. (2012)
<doi:10.1093/bioinformatics/bts447> "MALDIquant: a versatile R package for
the analysis of mass spectrometry data."

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
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
