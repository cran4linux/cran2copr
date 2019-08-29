%global packname  COMBIA
%global packver   1.0.6
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0.6
Release:          1%{?dist}
Summary:          Synergy/Antagonism Analyses of Drug Combinations

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


Requires:         perl >= 5.10.0
BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-hash 
BuildRequires:    R-lattice 
BuildRequires:    R-CRAN-latticeExtra 
BuildRequires:    R-CRAN-oro.nifti 
BuildRequires:    R-CRAN-gdata 
BuildRequires:    R-grDevices 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-hash 
Requires:         R-lattice 
Requires:         R-CRAN-latticeExtra 
Requires:         R-CRAN-oro.nifti 
Requires:         R-CRAN-gdata 
Requires:         R-grDevices 
Requires:         R-stats 
Requires:         R-utils 

%description
A comprehensive synergy/antagonism analyses of drug combinations with
quality graphics and data. The analyses can be performed by Bliss
independence and Loewe additivity models. 'COMBIA' provides improved
statistical analysis and makes only very weak assumption of data
variability while calculating bootstrap intervals (BIs). It is based on
heteroscedasticity controlled resampling (bootstrapping) and includes a
global (omnibus) test. Finally, package shows analyzed data, 2D and 3D
plots ready to use in research publications. 'COMBIA' does not require
manual data entry. Data can be directly input from wet lab experimental
platforms for example fluostar, automated robots etc. One only needs to
call a single function, analyzeCOMBO(), to perform all analysis (examples
are provided with sample data).

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
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/INDEX
