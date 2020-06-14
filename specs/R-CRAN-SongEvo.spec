%global packname  SongEvo
%global packver   1.0.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.0
Release:          2%{?dist}
Summary:          An Individual-Based Model of Bird Song Evolution

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.1.0
Requires:         R-core >= 3.1.0
BuildArch:        noarch
BuildRequires:    R-boot 
BuildRequires:    R-CRAN-geosphere 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-sp 
Requires:         R-boot 
Requires:         R-CRAN-geosphere 
Requires:         R-lattice 
Requires:         R-CRAN-sp 

%description
Simulates the cultural evolution of quantitative traits of bird song.
'SongEvo' is an individual- (agent-) based model. 'SongEvo' is
spatially-explicit and can be parameterized with, and tested against,
measured song data. Functions are available for model implementation,
sensitivity analyses, parameter optimization, model validation, and
hypothesis testing.

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
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/examples
%doc %{rlibdir}/%{packname}/profTests
%doc %{rlibdir}/%{packname}/slowTests
%{rlibdir}/%{packname}/INDEX
