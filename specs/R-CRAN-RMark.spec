%global packname  RMark
%global packver   2.2.7
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          2.2.7
Release:          2%{?dist}
Summary:          R Code for Mark Analysis

License:          GPL (>= 2)
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel >= 2.13.0
Requires:         R-core >= 2.13.0
BuildArch:        noarch
BuildRequires:    R-parallel 
BuildRequires:    R-CRAN-matrixcalc 
BuildRequires:    R-CRAN-msm 
BuildRequires:    R-CRAN-coda 
Requires:         R-parallel 
Requires:         R-CRAN-matrixcalc 
Requires:         R-CRAN-msm 
Requires:         R-CRAN-coda 

%description
An interface to the software package MARK that constructs input files for
MARK and extracts the output. MARK was developed by Gary White and is
freely available at <http://www.phidot.org/software/mark/downloads/> but
is not open source.

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
%doc %{rlibdir}/%{packname}/DerivedPar.txt
%{rlibdir}/%{packname}/extdata
%doc %{rlibdir}/%{packname}/MarkModels.pdf
%doc %{rlibdir}/%{packname}/models.txt
%doc %{rlibdir}/%{packname}/parameters.txt
%doc %{rlibdir}/%{packname}/README.txt
%{rlibdir}/%{packname}/INDEX
