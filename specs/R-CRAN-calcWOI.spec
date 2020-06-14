%global packname  calcWOI
%global packver   1.0.3
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.3
Release:          2%{?dist}
Summary:          Calculates the Wavelet-Based Organization Index

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.5.0
Requires:         R-core >= 3.5.0
BuildRequires:    R-CRAN-wavethresh >= 4.5
BuildRequires:    R-CRAN-LS2W >= 1.3.4
BuildRequires:    R-CRAN-dualtrees >= 0.1.4
Requires:         R-CRAN-wavethresh >= 4.5
Requires:         R-CRAN-LS2W >= 1.3.4
Requires:         R-CRAN-dualtrees >= 0.1.4

%description
Calculates the wavelet-based organization index following Brune et al
(2018) (<doi:10.1002/qj.3409>), the modified wavelet-based organization
index and the local wavelet-based organization index of an arbitrary 2D
array using Wavelet Transforms of the LS2W package by Eckley et al (2010)
(<doi:10.1111/j.1467-9876.2009.00721.x>) and Eckley and Nason (2011)
(<doi:10.18637/jss.v043.i03>). In Version 1.0.3 the calculation of LW is
added.

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
%{rlibdir}/%{packname}/libs
