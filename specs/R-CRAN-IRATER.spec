%global __brp_check_rpaths %{nil}
%global packname  IRATER
%global packver   0.0.1
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.0.1
Release:          3%{?dist}%{?buildtag}
Summary:          A R Interface for the Instantaneous RATEs (IRATE) Model

License:          GPL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.1
Requires:         R-core >= 3.0.1
BuildArch:        noarch
BuildRequires:    R-CRAN-coda 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-R2admb 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-stats 
Requires:         R-CRAN-coda 
Requires:         R-lattice 
Requires:         R-CRAN-R2admb 
Requires:         R-CRAN-plyr 
Requires:         R-stats 

%description
A R interface to setup, run and read IRATE model runs to assess band
recovery (conventional tagging) data (i.e. age-dependent or independent
fishing and natural mortality rates).

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
%doc %{rlibdir}/%{packname}/IRATE.examples
%doc %{rlibdir}/%{packname}/tplfiles
%{rlibdir}/%{packname}/INDEX
