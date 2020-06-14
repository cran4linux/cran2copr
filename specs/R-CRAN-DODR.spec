%global packname  DODR
%global packver   0.99.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.99.2
Release:          2%{?dist}
Summary:          Detection of Differential Rhythmicity

License:          GPL-2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-Matrix 
BuildRequires:    R-CRAN-Rfit 
BuildRequires:    R-CRAN-npsm 
BuildRequires:    R-parallel 
BuildRequires:    R-methods 
BuildRequires:    R-stats 
Requires:         R-Matrix 
Requires:         R-CRAN-Rfit 
Requires:         R-CRAN-npsm 
Requires:         R-parallel 
Requires:         R-methods 
Requires:         R-stats 

%description
Detect Differences in rhythmic time series. Using linear least squares and
the robust semi-parametric rfit() method. Differences in harmonic fitting
could be detected as well as differences in scale of the noise
distribution.

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
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/INDEX
