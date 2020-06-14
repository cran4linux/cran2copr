%global packname  bSims
%global packver   0.2-1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.2.1
Release:          2%{?dist}
Summary:          Bird Point Count Simulator

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-intrval 
BuildRequires:    R-CRAN-mefa4 
BuildRequires:    R-MASS 
BuildRequires:    R-CRAN-deldir 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-pbapply 
Requires:         R-CRAN-intrval 
Requires:         R-CRAN-mefa4 
Requires:         R-MASS 
Requires:         R-CRAN-deldir 
Requires:         R-parallel 
Requires:         R-CRAN-pbapply 

%description
A highly scientific and utterly addictive bird point count simulator to
test statistical assumptions, aid survey design, and have fun while doing
it. The simulations follow time-removal and distance sampling models based
on Matsuoka et al. (2012) <doi:10.1525/auk.2012.11190>, Solymos et al.
(2013) <doi:10.1111/2041-210X.12106>, and Solymos et al. (2018)
<doi:10.1650/CONDOR-18-32.1>, and sound attenuation experiments by Yip et
al. (2017) <doi:10.1650/CONDOR-16-93.1>.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/shiny
%{rlibdir}/%{packname}/INDEX
