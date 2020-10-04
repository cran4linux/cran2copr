%global packname  ISM
%global packver   0.1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.1.0
Release:          3%{?dist}%{?buildtag}
Summary:          Interpretive Structural Modelling (ISM)

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-xlsx 
BuildRequires:    R-CRAN-rJava 
BuildRequires:    R-CRAN-xlsxjars 
Requires:         R-CRAN-xlsx 
Requires:         R-CRAN-rJava 
Requires:         R-CRAN-xlsxjars 

%description
The development of ISM was made by Warfield in 1974. ISM is the process of
collaborating distinct or related essentials into a simplified and an
organized format. Hence, ISM is a methodology that seeks the
interrelationships among the various elements considered and endows with a
hierarchical and multilevel structure. To run this package user needs to
provide a matrix (VAXO) converted into 0's and 1's. Warfield,J.N. (1974)
<doi:10.1109/TSMC.1974.5408524> Warfield,J.N. (1974, E-ISSN:2168-2909).

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
%doc %{rlibdir}/%{packname}/ISM_ReadMe.html
%{rlibdir}/%{packname}/INDEX
