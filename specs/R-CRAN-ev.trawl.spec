%global packname  ev.trawl
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Extreme Value Trawls

License:          MIT + file LICENSE
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-testthat 
BuildRequires:    R-CRAN-fExtremes 
BuildRequires:    R-CRAN-hypergeo 
BuildRequires:    R-stats 
BuildRequires:    R-CRAN-ghyp 
BuildRequires:    R-CRAN-evir 
BuildRequires:    R-CRAN-eva 
Requires:         R-CRAN-testthat 
Requires:         R-CRAN-fExtremes 
Requires:         R-CRAN-hypergeo 
Requires:         R-stats 
Requires:         R-CRAN-ghyp 
Requires:         R-CRAN-evir 
Requires:         R-CRAN-eva 

%description
Implementation of trawl processes and an extension of such processes into
a univariate latent model for extreme values. Inference, simulation and
initialization tools are available. See Noven et al. (2018)
<DOI:10.21314/JEM.2018.179> which can be found on arXiv
(<arXiv:1511.08190>) .

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
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/INDEX
