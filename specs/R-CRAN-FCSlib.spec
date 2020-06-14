%global packname  FCSlib
%global packver   1.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.0
Release:          2%{?dist}
Summary:          A Collection of Fluorescence Fluctuation Spectroscopy Methods

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildArch:        noarch
BuildRequires:    R-CRAN-tiff 
Requires:         R-CRAN-tiff 

%description
A set of tools for fluorescence fluctuation spectroscopy data analysis
performance is provided in this package. It includes techniques such as
single-point fluorescence correlation spectroscopy, autocorrelation and
pair correlation functions, number & brightness (raster line scan) and a
novel, recently developed method by Hinde and co-workers, pair correlation
of molecular brightness (doi:10.1038/ncomms11047). A set of simulations
and real experimental data is used for the examples of each function
provided in this package. For an in-depth description of the basics behind
each function here included and a detailed step-by-step guide on how to
use them on your own data, please refer to the Supplementary Material file
provided at (<https://github.com/RPintoC/FCSlib_Sup_Data>).

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
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
