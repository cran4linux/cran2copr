%global packname  ARDL
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          2%{?dist}
Summary:          ARDL, ECM and Bounds-Test for Cointegration

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.2.0
Requires:         R-core >= 3.2.0
BuildArch:        noarch
BuildRequires:    R-CRAN-aod 
BuildRequires:    R-CRAN-dplyr 
BuildRequires:    R-CRAN-dynlm 
BuildRequires:    R-CRAN-lmtest 
BuildRequires:    R-CRAN-msm 
BuildRequires:    R-CRAN-stringr 
BuildRequires:    R-CRAN-zoo 
Requires:         R-CRAN-aod 
Requires:         R-CRAN-dplyr 
Requires:         R-CRAN-dynlm 
Requires:         R-CRAN-lmtest 
Requires:         R-CRAN-msm 
Requires:         R-CRAN-stringr 
Requires:         R-CRAN-zoo 

%description
Creates complex autoregressive distributed lag (ARDL) models providing
just the order and automatically constructs the underlying unrestricted
and restricted error correction model (ECM). It also performs the
bounds-test for cointegration as described in Pesaran et al. (2001)
<doi:10.1002/jae.616> and provides the multipliers and the cointegrating
equation.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
