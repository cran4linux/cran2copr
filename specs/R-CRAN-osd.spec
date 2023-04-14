%global __brp_check_rpaths %{nil}
%global packname  osd
%global packver   0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1
Release:          3%{?dist}%{?buildtag}
Summary:          Orthogonal Signal Deconvolution for Spectra Deconvolution inGC-MS and GCxGC-MS Data

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-JADE 
BuildRequires:    R-CRAN-nnls 
Requires:         R-CRAN-JADE 
Requires:         R-CRAN-nnls 

%description
Compound deconvolution for chromatographic data, including gas
chromatography - mass spectrometry (GC-MS) and comprehensive gas
chromatography - mass spectrometry (GCxGC-MS). The package includes
functions to perform independent component analysis - orthogonal signal
deconvolution (ICA-OSD), independent component regression (ICR),
multivariate curve resolution (MCR-ALS) and orthogonal signal
deconvolution (OSD) alone.

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
