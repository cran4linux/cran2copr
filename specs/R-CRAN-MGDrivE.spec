%global packname  MGDrivE
%global packver   1.5.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.5.0
Release:          3%{?dist}
Summary:          Mosquito Gene Drive Explorer

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildRequires:    R-CRAN-Rdpack >= 0.7
BuildRequires:    R-CRAN-R6 
BuildRequires:    R-CRAN-Rcpp 
BuildRequires:    R-grDevices 
BuildRequires:    R-graphics 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-CRAN-Rdpack >= 0.7
Requires:         R-CRAN-R6 
Requires:         R-CRAN-Rcpp 
Requires:         R-grDevices 
Requires:         R-graphics 
Requires:         R-stats 
Requires:         R-utils 

%description
Provides a model designed to be a reliable testbed where various gene
drive interventions for mosquito-borne diseases control. It is being
developed to accommodate the use of various mosquito-specific gene drive
systems within a population dynamics framework that allows migration of
individuals between patches in landscape. Previous work developing the
population dynamics can be found in Deredec et al. (2001)
<doi:10.1073/pnas.1110717108> and Hancock & Godfray (2007)
<doi:10.1186/1475-2875-6-98>, and extensions to accommodate basic CRISPR
homing dynamics in Marshall et al. (2017)
<doi:10.1038/s41598-017-02744-7>.

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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/REFERENCES.bib
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/libs
