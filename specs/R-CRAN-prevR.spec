%global packname  prevR
%global packver   3.4.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          3.4.0
Release:          2%{?dist}
Summary:          Estimating Regional Trends of a Prevalence from a DHS

License:          CeCILL
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.10
Requires:         R-core >= 2.10
BuildArch:        noarch
BuildRequires:    R-CRAN-rgdal >= 0.7
BuildRequires:    R-CRAN-sp 
BuildRequires:    R-CRAN-ggplot2 
BuildRequires:    R-CRAN-directlabels 
BuildRequires:    R-CRAN-GenKern 
BuildRequires:    R-CRAN-fields 
BuildRequires:    R-CRAN-gstat 
BuildRequires:    R-foreign 
BuildRequires:    R-CRAN-maptools 
BuildRequires:    R-methods 
Requires:         R-CRAN-rgdal >= 0.7
Requires:         R-CRAN-sp 
Requires:         R-CRAN-ggplot2 
Requires:         R-CRAN-directlabels 
Requires:         R-CRAN-GenKern 
Requires:         R-CRAN-fields 
Requires:         R-CRAN-gstat 
Requires:         R-foreign 
Requires:         R-CRAN-maptools 
Requires:         R-methods 

%description
Spatial estimation of a prevalence surface or a relative risks surface,
using data from a Demographic and Health Survey (DHS) or an analog survey,
see Larmarange et al. (2011) <doi:10.4000/cybergeo.24606>.

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
%doc %{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/NAMESPACE
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/R
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/po
%{rlibdir}/%{packname}/INDEX
