%global packname  mrds
%global packver   2.2.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.2
Release:          2%{?dist}
Summary:          Mark-Recapture Distance Sampling

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0
Requires:         R-core >= 3.0
BuildArch:        noarch
BuildRequires:    R-CRAN-optimx >= 2013.8.6
BuildRequires:    R-mgcv 
BuildRequires:    R-CRAN-numDeriv 
BuildRequires:    R-CRAN-Rsolnp 
Requires:         R-CRAN-optimx >= 2013.8.6
Requires:         R-mgcv 
Requires:         R-CRAN-numDeriv 
Requires:         R-CRAN-Rsolnp 

%description
Animal abundance estimation via conventional, multiple covariate and
mark-recapture distance sampling (CDS/MCDS/MRDS). Detection function
fitting is performed via maximum likelihood. Also included are diagnostics
and plotting for fitted detection functions. Abundance estimation is via a
Horvitz-Thompson-like estimator.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/ONEWS
%{rlibdir}/%{packname}/INDEX
