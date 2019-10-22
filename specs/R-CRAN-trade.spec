%global packname  trade
%global packver   0.5.4
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.5.4
Release:          1%{?dist}
Summary:          Tools for Trade Practitioners

License:          Unlimited
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-antitrust >= 0.99.11
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-CRAN-antitrust >= 0.99.11
Requires:         R-methods 
Requires:         R-stats 

%description
A collection of tools for trade practitioners, including the ability to
calibrate different consumer demand systems and simulate the effects of
tariffs and quotas under different competitive regimes. These tools are
derived from Anderson et al. (2001) <doi:10.1016/S0047-2727(00)00085-2>
and Froeb et al. (2003) <doi:10.1016/S0304-4076(02)00166-5>.

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
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/trade_shiny
%{rlibdir}/%{packname}/INDEX
