%global packname  baseline
%global packver   1.3-0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.3.0
Release:          2%{?dist}
Summary:          Baseline Correction of Spectra

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.15
Requires:         R-core >= 2.15
BuildArch:        noarch
BuildRequires:    R-graphics 
BuildRequires:    R-CRAN-SparseM 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-methods 
BuildRequires:    R-CRAN-limSolve 
Requires:         R-graphics 
Requires:         R-CRAN-SparseM 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-methods 
Requires:         R-CRAN-limSolve 

%description
Collection of baseline correction algorithms, along with a framework and a
Tcl/Tk enabled GUI for optimising baseline algorithm parameters. Typical
use of the package is for removing background effects from spectra
originating from various types of spectroscopy and spectrometry, possibly
optimizing this with regard to regression or classification results.
Correction methods include polynomial fitting, weighted local smoothers
and many more.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
