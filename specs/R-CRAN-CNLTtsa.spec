%global __brp_check_rpaths %{nil}
%global packname  CNLTtsa
%global packver   0.1-2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.2
Release:          3%{?dist}%{?buildtag}
Summary:          Complex-Valued Wavelet Lifting for Univariate and Bivariate TimeSeries Analysis

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1
Requires:         R-core >= 3.1
BuildArch:        noarch
BuildRequires:    R-CRAN-adlift 
BuildRequires:    R-CRAN-nlt 
BuildRequires:    R-CRAN-CNLTreg 
BuildRequires:    R-CRAN-fields 
Requires:         R-CRAN-adlift 
Requires:         R-CRAN-nlt 
Requires:         R-CRAN-CNLTreg 
Requires:         R-CRAN-fields 

%description
Implementations of recent complex-valued wavelet spectral procedures for
analysis of irregularly sampled signals, see Hamilton et al (2018)
<doi:10.1080/00401706.2017.1281846>.

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
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
