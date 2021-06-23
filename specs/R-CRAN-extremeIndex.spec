%global __brp_check_rpaths %{nil}
%global packname  extremeIndex
%global packver   0.0.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.2
Release:          3%{?dist}%{?buildtag}
Summary:          Forecast Verification for Extreme Events

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.3
Requires:         R-core >= 3.2.3
BuildArch:        noarch
BuildRequires:    R-CRAN-goftest 
BuildRequires:    R-boot 
BuildRequires:    R-CRAN-evd 
BuildRequires:    R-CRAN-gmm 
BuildRequires:    R-CRAN-evir 
Requires:         R-CRAN-goftest 
Requires:         R-boot 
Requires:         R-CRAN-evd 
Requires:         R-CRAN-gmm 
Requires:         R-CRAN-evir 

%description
An index measuring the amount of information brought by forecasts for
extreme events, subject to calibration, is computed. This index is
originally designed for weather or climate forecasts, but it may be used
in other forecasting contexts. This is the implementation of the index in
Taillardat et al. (2019) <arXiv:1905.04022>.

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
