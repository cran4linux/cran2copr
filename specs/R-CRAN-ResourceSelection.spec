%global packname  ResourceSelection
%global packver   0.3-5
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.3.5
Release:          1%{?dist}
Summary:          Resource Selection (Probability) Functions for Use-AvailabilityData

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.13.0
Requires:         R-core >= 2.13.0
BuildArch:        noarch
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-pbapply 
BuildRequires:    R-Matrix 
Requires:         R-MASS 
Requires:         R-CRAN-pbapply 
Requires:         R-Matrix 

%description
Resource Selection (Probability) Functions for use-availability wildlife
data based on weighted distributions as described in Lele and Keim (2006)
<doi:10.1890/0012-9658(2006)87%5B3021:WDAEOR%5D2.0.CO;2>, Lele (2009)
<doi:10.2193/2007-535>, and Solymos & Lele (2016)
<doi:10.1111/2041-210X.12432>.

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
