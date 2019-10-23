%global packname  SDEFSR
%global packver   0.7.2
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          0.7.2
Release:          1%{?dist}
Summary:          Subgroup Discovery with Evolutionary Fuzzy Systems

License:          LGPL (>= 3)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 3.0.0
Requires:         R-core >= 3.0.0
BuildArch:        noarch
BuildRequires:    R-grDevices 
BuildRequires:    R-methods 
BuildRequires:    R-parallel 
BuildRequires:    R-stats 
BuildRequires:    R-utils 
Requires:         R-grDevices 
Requires:         R-methods 
Requires:         R-parallel 
Requires:         R-stats 
Requires:         R-utils 

%description
Implementation of evolutionary fuzzy systems for the data mining task
called "subgroup discovery". In particular, the algorithms presented in
this package are: M. J. del Jesus, P. Gonzalez, F. Herrera, M. Mesonero
(2007) <doi:10.1109/TFUZZ.2006.890662> M. J. del Jesus, P. Gonzalez, F.
Herrera (2007) <doi:10.1109/MCDM.2007.369416> C. J. Carmona, P. Gonzalez,
M. J. del Jesus, F. Herrera (2010) <doi:10.1109/TFUZZ.2010.2060200> C. J.
Carmona, V. Ruiz-Rodado, M. J. del Jesus, A. Weber, M. Grootveld, P.
González, D. Elizondo (2015) <doi:10.1016/j.ins.2014.11.030> It also
provide a Shiny App to ease the analysis. The algorithms work with data
sets provided in KEEL, ARFF and CSV format and also with data.frame
objects.

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
%doc %{rlibdir}/%{packname}/shiny
%{rlibdir}/%{packname}/INDEX
