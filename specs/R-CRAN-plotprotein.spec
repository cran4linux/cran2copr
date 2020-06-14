%global packname  plotprotein
%global packver   1.0
%global rlibdir   /usr/local/lib/R/library

Name:             R-CRAN-%{packname}
Version:          1.0
Release:          2%{?dist}
Summary:          Development of Visualization Tools for Protein Sequence

License:          GPL-3
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packver}#/%{packname}_%{packver}.tar.gz


BuildRequires:    R-devel
Requires:         R-core
BuildArch:        noarch
BuildRequires:    R-CRAN-XML 
BuildRequires:    R-CRAN-plyr 
BuildRequires:    R-CRAN-plotrix 
BuildRequires:    R-CRAN-seqinr 
BuildRequires:    R-CRAN-ade4 
Requires:         R-CRAN-XML 
Requires:         R-CRAN-plyr 
Requires:         R-CRAN-plotrix 
Requires:         R-CRAN-seqinr 
Requires:         R-CRAN-ade4 

%description
The image of the amino acid transform on the protein level is drawn, and
the automatic routing of the functional elements such as the domain and
the mutation site is completed.

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
%{rlibdir}/%{packname}/INDEX
