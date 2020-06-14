%global packname  astrochron
%global packver   0.9
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.9
Release:          2%{?dist}
Summary:          A Computational Tool for Astrochronology

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildRequires:    R-CRAN-multitaper 
BuildRequires:    R-CRAN-IDPmisc 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-doParallel 
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-iterators 
BuildRequires:    R-CRAN-foreach 
Requires:         R-CRAN-multitaper 
Requires:         R-CRAN-IDPmisc 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-doParallel 
Requires:         R-parallel 
Requires:         R-CRAN-iterators 
Requires:         R-CRAN-foreach 

%description
Routines for astrochronologic testing, astronomical time scale
construction, and time series analysis. Also included are a range of
statistical analysis and modeling routines that are relevant to time scale
development and paleoclimate analysis.

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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
