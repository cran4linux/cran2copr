%global packname  dynamac
%global packver   0.1.11
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.11
Release:          3%{?dist}%{?buildtag}
Summary:          Dynamic Simulation and Testing for Single-Equation ARDL Models

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.1
Requires:         R-core >= 3.0.1
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-lmtest 
Requires:         R-MASS 
Requires:         R-CRAN-lmtest 

%description
While autoregressive distributed lag (ARDL) models allow for extremely
flexible dynamics, interpreting substantive significance of complex lag
structures remains difficult. This package is designed to assist users in
dynamically simulating and plotting the results of various ARDL models. It
also contains post-estimation diagnostics, including a test for
cointegration when estimating the error-correction variant of the
autoregressive distributed lag model (Pesaran, Shin, and Smith 2001
<doi:10.1002/jae.616>).

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
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/dynamac-manual.pdf
%{rlibdir}/%{packname}/INDEX
