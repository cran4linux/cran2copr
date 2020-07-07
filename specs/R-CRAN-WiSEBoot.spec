%global packname  WiSEBoot
%global packver   1.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.4.0
Release:          3%{?dist}
Summary:          Wild Scale-Enhanced Bootstrap

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-CRAN-wavethresh 
BuildRequires:    R-CRAN-FAdist 
Requires:         R-CRAN-wavethresh 
Requires:         R-CRAN-FAdist 

%description
Perform the Wild Scale-Enhanced (WiSE) bootstrap.  Specifically, the user
may supply a single or multiple equally-spaced time series and use the
WiSE bootstrap to select a wavelet-smoothed model.  Conversely, a
pre-selected smooth level may also be specified for the time series.
Quantities such as the bootstrap sample of wavelet coefficients, smoothed
bootstrap samples, and specific hypothesis testing and confidence region
results of the wavelet coefficients may be obtained.  Additional functions
are available to the user which help format the time series before
analysis.  This methodology is recommended to aid in model selection and
signal extraction. Note: This package specifically uses wavelet bases in
the WiSE bootstrap methodology, but the theoretical construct is much more
versatile.

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
%doc %{rlibdir}/%{packname}/doc
%{rlibdir}/%{packname}/INDEX
