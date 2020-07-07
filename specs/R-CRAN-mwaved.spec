%global packname  mwaved
%global packver   1.1.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.1.7
Release:          3%{?dist}
Summary:          Multichannel Wavelet Deconvolution with Additive Long MemoryNoise

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    fftw-devel >= 3.3.4
Requires:         fftw
BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-CRAN-shiny 
BuildRequires:    R-grid 
Requires:         R-CRAN-Rcpp 
Requires:         R-CRAN-shiny 
Requires:         R-grid 

%description
Computes the Wavelet deconvolution estimate of a common signal present in
multiple channels that have possible different levels of blur and long
memory additive error, see Kulik, Sapatinas and Wishart (2015),
<doi:10.1016/j.acha.2014.04.004>.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/mWaveDDemo
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
